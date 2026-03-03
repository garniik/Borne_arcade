import ast
import difflib
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from ollama_wrapper_iut import OllamaWrapper


@dataclass(frozen=True)
class Edit:
    file_path: Path
    new_text: str


_IGNORE_DIRS = {".git", "__pycache__", "node_modules", ".vscode", ".idea", "build", "dist", "venv"}


def _is_ignored(path: Path) -> bool:
    return any(part in _IGNORE_DIRS for part in path.parts)


def _iter_python_files(repo_root: Path):
    for p in repo_root.rglob("*.py"):
        if p.is_file() and not _is_ignored(p):
            yield p


def _make_prompt(*, file_path: Path, symbol_kind: str, signature: str, body_preview: str) -> str:
    return f"""
Tu écris une docstring Python (format triple quotes) pour {symbol_kind}.

Contraintes STRICTES:
- Réponds UNIQUEMENT avec le contenu de la docstring (sans ``` et sans texte autour).
- Style concis, technique, en français.
- Ne mens pas: si tu ne sais pas, reste générique mais correct.
- Doit être compatible avec Python.

Contexte:
- Fichier: {file_path.as_posix()}
- Signature: {signature}

Corps (extrait):
{body_preview}
""".strip()


def _generate_docstring(wrapper: OllamaWrapper, *, model_llm: str, file_path: Path, symbol_kind: str, signature: str, body_preview: str) -> str:
    prompt = _make_prompt(file_path=file_path, symbol_kind=symbol_kind, signature=signature, body_preview=body_preview)
    r = wrapper.generate_text(model=model_llm, prompt=prompt)
    text = (r.response or "").strip()
    # Normalise: on force à ne pas inclure de triple quotes externes
    if text.startswith('"""') and text.endswith('"""'):
        text = text[3:-3].strip()
    return text


def _indent_block(text: str, indent: str) -> str:
    lines = text.splitlines() or [""]
    return "\n".join((indent + l) if l.strip() else indent for l in lines)


def _insert_docstring_in_block(lines: list[str], *, insert_at_1_indexed: int, indent: str, docstring_content: str) -> list[str]:
    ds_lines = ['"""' + docstring_content + '"""'] if "\n" not in docstring_content else ['"""', *docstring_content.splitlines(), '"""']
    ds_lines = [indent + l if l else indent for l in ds_lines]
    i0 = max(0, insert_at_1_indexed - 1)
    return lines[:i0] + ds_lines + lines[i0:]


def _apply_edits(edits: list[Edit], *, apply: bool) -> None:
    for e in edits:
        old = e.file_path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=False)
        new = e.new_text.splitlines(keepends=False)
        diff = difflib.unified_diff(old, new, fromfile=str(e.file_path), tofile=str(e.file_path), lineterm="")
        print("\n".join(diff))
        if apply:
            e.file_path.write_text(e.new_text, encoding="utf-8")


def _maybe_add_module_docstring(wrapper: OllamaWrapper, *, model_llm: str, file_path: Path, tree: ast.Module, lines: list[str]) -> Optional[list[str]]:
    if ast.get_docstring(tree) is not None:
        return None

    # Préserve shebang + encoding
    insert_at = 1
    if lines and lines[0].startswith("#!"):
        insert_at = 2
    if len(lines) >= insert_at and "coding" in lines[insert_at - 1]:
        insert_at += 1

    body_preview = "\n".join(lines[:120])
    doc = _generate_docstring(wrapper, model_llm=model_llm, file_path=file_path, symbol_kind="module", signature=file_path.name, body_preview=body_preview)
    new_lines = _insert_docstring_in_block(lines, insert_at_1_indexed=insert_at, indent="", docstring_content=doc)
    return new_lines


def _node_signature(file_path: Path, node: ast.AST) -> str:
    # Heuristique: on prend la ligne source de la def/class
    try:
        src = file_path.read_text(encoding="utf-8", errors="replace")
        seg = ast.get_source_segment(src, node)
        if isinstance(seg, str):
            return seg.splitlines()[0].strip()
    except Exception:
        pass
    if isinstance(node, ast.FunctionDef):
        return f"def {node.name}(…)"
    if isinstance(node, ast.AsyncFunctionDef):
        return f"async def {node.name}(…)"
    if isinstance(node, ast.ClassDef):
        return f"class {node.name}"
    return "<unknown>"


def _maybe_add_docstring_to_def(wrapper: OllamaWrapper, *, model_llm: str, file_path: Path, node: ast.AST, lines: list[str]) -> Optional[list[str]]:
    if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return None

    doc = ast.get_docstring(node)
    if doc is not None:
        return None

    if not hasattr(node, "body") or not node.body:
        return None

    first_stmt = node.body[0]

    # Emplacement: première ligne du corps
    insert_at = getattr(first_stmt, "lineno", None)
    if not isinstance(insert_at, int):
        return None

    # Indentation: on récupère l'indentation de la ligne du first statement
    line = lines[insert_at - 1] if 0 <= insert_at - 1 < len(lines) else ""
    indent = line[: len(line) - len(line.lstrip(" \t"))]

    body_preview_lines = []
    start = getattr(node, "lineno", 1)
    end = getattr(node, "end_lineno", min(len(lines), start + 60))
    for i in range(start - 1, min(len(lines), end)):
        body_preview_lines.append(lines[i])
    body_preview = "\n".join(body_preview_lines[:80])

    kind = "classe" if isinstance(node, ast.ClassDef) else "fonction"
    signature = _node_signature(file_path, node)
    ds = _generate_docstring(wrapper, model_llm=model_llm, file_path=file_path, symbol_kind=kind, signature=signature, body_preview=body_preview)

    return _insert_docstring_in_block(lines, insert_at_1_indexed=insert_at, indent=indent, docstring_content=ds)


def process_file(wrapper: OllamaWrapper, *, model_llm: str, file_path: Path) -> Optional[Edit]:
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines(keepends=False)
        tree = ast.parse(text)
    except Exception:
        return None

    changed = False

    new_lines = _maybe_add_module_docstring(wrapper, model_llm=model_llm, file_path=file_path, tree=tree, lines=lines)
    if new_lines is not None:
        lines = new_lines
        changed = True
        # Re-parse après modification (linenos peuvent changer)
        try:
            tree = ast.parse("\n".join(lines) + "\n")
        except Exception:
            return None

    # Ajout docstrings defs de niveau module uniquement (on reste conservatif)
    for node in list(tree.body):
        updated = _maybe_add_docstring_to_def(wrapper, model_llm=model_llm, file_path=file_path, node=node, lines=lines)
        if updated is not None:
            lines = updated
            changed = True
            try:
                tree = ast.parse("\n".join(lines) + "\n")
            except Exception:
                return None

    if not changed:
        return None

    return Edit(file_path=file_path, new_text="\n".join(lines) + "\n")


def run(*, wrapper: OllamaWrapper, model_llm: str, repo_root: Path, apply: bool) -> None:
    edits: list[Edit] = []
    for p in _iter_python_files(repo_root):
        e = process_file(wrapper, model_llm=model_llm, file_path=p)
        if e is not None:
            edits.append(e)

    print(f"\n📌 Docstrings Python: {len(edits)} fichiers modifiés (mode={'APPLY' if apply else 'DRY-RUN'})")
    _apply_edits(edits, apply=apply)
