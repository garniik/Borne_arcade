import difflib
import re
from dataclasses import dataclass
from pathlib import Path

from ollama_wrapper_iut import OllamaWrapper


@dataclass(frozen=True)
class Edit:
    file_path: Path
    new_text: str


_IGNORE_DIRS = {".git", "__pycache__", "node_modules", ".vscode", ".idea", "build", "dist", "venv"}


def _is_ignored(path: Path) -> bool:
    return any(part in _IGNORE_DIRS for part in path.parts)


def _iter_java_files(repo_root: Path):
    for p in repo_root.rglob("*.java"):
        if p.is_file() and not _is_ignored(p):
            yield p


def _make_prompt(*, file_path: Path, kind: str, signature: str, context: str) -> str:
    return f"""
Tu génères un commentaire Javadoc pour un élément Java ({kind}).

Contraintes STRICTES:
- Réponds UNIQUEMENT avec le bloc Javadoc complet (commence par /** et finit par */).
- Français, concis, technique.
- Utilise @param, @return, @throws uniquement si pertinent.
- Ne pas inventer de comportements non visibles dans la signature/contexte.

Fichier: {file_path.as_posix()}
Signature: {signature}

Contexte (extrait):
{context}
""".strip()


def _generate_javadoc(wrapper: OllamaWrapper, *, model_llm: str, file_path: Path, kind: str, signature: str, context: str) -> str:
    prompt = _make_prompt(file_path=file_path, kind=kind, signature=signature, context=context)
    r = wrapper.generate_text(model=model_llm, prompt=prompt)
    text = (r.response or "").strip()
    return text


def _apply_edits(edits: list[Edit], *, apply: bool) -> None:
    for e in edits:
        old = e.file_path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=False)
        new = e.new_text.splitlines(keepends=False)
        diff = difflib.unified_diff(old, new, fromfile=str(e.file_path), tofile=str(e.file_path), lineterm="")
        print("\n".join(diff))
        if apply:
            e.file_path.write_text(e.new_text, encoding="utf-8")


_CLASS_RE = re.compile(r"^(\s*)(public\s+)?(final\s+)?(class|interface|enum)\s+(\w+)")
_METHOD_RE = re.compile(r"^(\s*)(public|protected)\s+[\w\<\>\[\]]+\s+(\w+)\s*\([^;]*\)\s*(throws\s+[^\{]+)?\{\s*$")


def process_file(wrapper: OllamaWrapper, *, model_llm: str, file_path: Path) -> Edit | None:
    text = file_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=False)

    changed = False

    def has_javadoc_before(line_index: int) -> bool:
        # Cherche un /** ... */ juste au-dessus (avec lignes vides possibles)
        i = line_index - 1
        while i >= 0 and lines[i].strip() == "":
            i -= 1
        if i >= 0 and lines[i].strip().endswith("*/"):
            # remonte jusqu'à /**
            while i >= 0 and "/**" not in lines[i]:
                i -= 1
            if i >= 0 and lines[i].strip().startswith("/**"):
                return True
        return False

    i = 0
    while i < len(lines):
        line = lines[i]

        m_class = _CLASS_RE.match(line)
        if m_class and not has_javadoc_before(i):
            indent = m_class.group(1) or ""
            signature = line.strip()
            context = "\n".join(lines[max(0, i - 3): min(len(lines), i + 8)])
            jd = _generate_javadoc(wrapper, model_llm=model_llm, file_path=file_path, kind="type", signature=signature, context=context)
            jd_lines = [indent + l if l.strip() else indent for l in jd.splitlines()]
            lines = lines[:i] + jd_lines + lines[i:]
            changed = True
            i += len(jd_lines) + 1
            continue

        m_meth = _METHOD_RE.match(line)
        if m_meth and not has_javadoc_before(i):
            indent = m_meth.group(1) or ""
            signature = line.strip()
            context = "\n".join(lines[max(0, i - 3): min(len(lines), i + 8)])
            jd = _generate_javadoc(wrapper, model_llm=model_llm, file_path=file_path, kind="méthode", signature=signature, context=context)
            jd_lines = [indent + l if l.strip() else indent for l in jd.splitlines()]
            lines = lines[:i] + jd_lines + lines[i:]
            changed = True
            i += len(jd_lines) + 1
            continue

        i += 1

    if not changed:
        return None

    return Edit(file_path=file_path, new_text="\n".join(lines) + "\n")


def run(*, wrapper: OllamaWrapper, model_llm: str, repo_root: Path, apply: bool) -> None:
    edits: list[Edit] = []
    for p in _iter_java_files(repo_root):
        e = process_file(wrapper, model_llm=model_llm, file_path=p)
        if e is not None:
            edits.append(e)

    print(f"\n📌 Javadoc Java: {len(edits)} fichiers modifiés (mode={'APPLY' if apply else 'DRY-RUN'})")
    _apply_edits(edits, apply=apply)
