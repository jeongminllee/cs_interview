from __future__ import annotations

import re
from collections import Counter
from pathlib import Path


ROOT = Path("wiki/cs/engineer_info_processing")
SKIP_FILES = {
    ROOT / "index.md",
    ROOT / "my_study_log.md",
}


LITERAL_REPLACEMENTS = {
    # High-confidence technical OCR fixes.
    "S0L": "SQL",
    "S0Q": "SQL",
    "D3MS": "DBMS",
    "D8MS": "DBMS",
    "D6MS": "DBMS",
    "Funchon": "Function",
    "Fuction": "Function",
    "Functon": "Function",
    "Transacton": "Transaction",
    "Oata": "Data",
    "CcnKI": "Control",
    "Ti>99«": "Trigger",
    "Siatic": "static",
    "sialic": "static",
    "statlc": "static",
    "statk": "static",
    "prirrt": "print",
    "pnnt": "print",
    "pintf": "printf",
    "pubiic": "public",
    "publlc": "public",
    "retum": "return",
    "retrun": "return",
    "0NCS": "NCS",
    "0RED0": "REDO",
    "C0어자역번수": "지역변수",
    # Common Korean OCR confusions seen in this corpus.
    "데이티": "데이터",
    "다이터": "데이터",
    "3이터": "데이터",
    "데이타": "데이터",
    "트랜잭신": "트랜잭션",
    "트렌잭션": "트랜잭션",
    "트렌짝선": "트랜잭션",
    "스키 o|": "스키마",
    "스키 oI": "스키마",
    "싱괸": "상관",
    "긩우": "경우",
    "깅우": "경우",
    "기덥": "기법",
    "쟤직업": "재작업",
    "징보": "정보",
    "최적히": "최적화",
    "긘잣값": "결과값",
    "집겨 져 함 임 수 수": "집계 함수",
    "집계 함수匕": "집계 함수는",
    "비징상": "비정상",
    "징상": "정상",
    "수제비 t FINAL": "수제비 FINAL",
}


WORD_REPLACEMENTS = {
    r"\bS0L\b": "SQL",
    r"\bD3MS\b": "DBMS",
    r"\bD8MS\b": "DBMS",
    r"\bOCL\b": "DCL",
}


REGEX_REPLACEMENTS = [
    # Korean sentence ending spacing created by OCR/PDF extraction.
    (re.compile(r"합[ \t]*니[ \t]*다"), "합니다"),
    (re.compile(r"습[ \t]*니[ \t]*다"), "습니다"),
    (re.compile(r"입[ \t]*니[ \t]*다"), "입니다"),
    (re.compile(r"됩[ \t]*니[ \t]*다"), "됩니다"),
    (re.compile(r"했[ \t]*습[ \t]*니[ \t]*다"), "했습니다"),
    (re.compile(r"되[ \t]*었[ \t]*습[ \t]*니[ \t]*다"), "되었습니다"),
    (re.compile(r"있[ \t]*습[ \t]*니[ \t]*다"), "있습니다"),
    (re.compile(r"없[ \t]*습[ \t]*니[ \t]*다"), "없습니다"),
    (re.compile(r"같[ \t]*습[ \t]*니[ \t]*다"), "같습니다"),
    # Frequently split technical terms.
    (re.compile(r"데[ \t]*이[ \t]*터[ \t]*베[ \t]*이[ \t]*스"), "데이터베이스"),
    (re.compile(r"데[ \t]*이[ \t]*터"), "데이터"),
    (re.compile(r"트[ \t]*랜[ \t]*잭[ \t]*션"), "트랜잭션"),
    (re.compile(r"스[ \t]*키[ \t]*마"), "스키마"),
    (re.compile(r"정[ \t]*보[ \t]*처[ \t]*리[ \t]*기[ \t]*사"), "정보처리기사"),
    (re.compile(r"수[ \t]*제[ \t]*비"), "수제비"),
    # Mark replacement-character damage explicitly if present.
    (re.compile(r"^(?=.*[�])(.+)$", re.M), r"\1 [확인 필요]"),
]


SUSPICIOUS_CHARS = set("«»§£™匕丄∑Ж")
SUSPICIOUS_PATTERNS = [
    re.compile(r"[A-Za-z][가-힣][A-Za-z]"),
    re.compile(r"[가-힣][A-Za-z]{2,}"),
    re.compile(r"[A-Za-z]{2,}[가-힣]"),
    re.compile(r"[0-9][가-힣][A-Za-z]"),
    re.compile(r"[|][가-힣]"),
    re.compile(r"[가-힣][|]"),
]


def needs_review_marker(line: str) -> bool:
    stripped = line.strip()
    if not stripped or stripped.endswith("[확인 필요]"):
        return False
    if stripped.startswith(("---", "type:", "title:", "description:", "tags:", "timestamp:", "status:", "#")):
        return False
    if stripped.startswith(("-", "*", "|")) and "](" in stripped:
        return False
    if re.search(r"^\s*(```|~~~)", line):
        return False
    if any(ch in stripped for ch in SUSPICIOUS_CHARS):
        return True
    if stripped.count("?") >= 2:
        return True
    return any(pattern.search(stripped) for pattern in SUSPICIOUS_PATTERNS)


FULLWIDTH = str.maketrans(
    {
        "；": ";",
        "，": ",",
        "．": ".",
        "：": ":",
        "（": "(",
        "）": ")",
        "［": "[",
        "］": "]",
        "｛": "{",
        "｝": "}",
        "＋": "+",
        "－": "-",
        "＝": "=",
        "％": "%",
        "＜": "<",
        "＞": ">",
        "〈": "<",
        "〉": ">",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "·": ".",
    }
)


FRAGMENT_RUN = re.compile(r"(?<!\S)((?:[가-힣]\s+){5,}[가-힣])(?!\S)")


def compact_fragment_runs(line: str) -> str:
    return FRAGMENT_RUN.sub(lambda m: m.group(1).replace(" ", ""), line)


def clean_text(text: str) -> tuple[str, Counter]:
    stats: Counter = Counter()

    new_text = text.translate(FULLWIDTH)
    if new_text != text:
        stats["normalized_punctuation"] += 1
    text = new_text

    for src, dst in LITERAL_REPLACEMENTS.items():
        count = text.count(src)
        if count:
            stats[f"literal:{src}->{dst}"] += count
            text = text.replace(src, dst)

    for pattern, dst in WORD_REPLACEMENTS.items():
        text, count = re.subn(pattern, dst, text)
        if count:
            stats[f"word:{pattern}->{dst}"] += count

    for pattern, dst in REGEX_REPLACEMENTS:
        text, count = pattern.subn(dst, text)
        if count:
            stats[f"regex:{pattern.pattern}->{dst}"] += count

    lines: list[str] = []
    compacted = 0
    marked = 0
    for line in text.splitlines():
        original = line
        line = re.sub(r"[ \t]+$", "", line)
        # Avoid compacting obvious code/table-ish lines.
        if not re.search(r"[{}();=<>]|\|", line):
            line = compact_fragment_runs(line)
        if needs_review_marker(line):
            line = f"{line} [확인 필요]"
            marked += 1
        if line != original:
            compacted += 1
        lines.append(line)

    text = "\n".join(lines)
    if text and not text.endswith("\n"):
        text += "\n"

    text, count = re.subn(r"\n{4,}", "\n\n\n", text)
    if count:
        stats["collapsed_blank_lines"] += count
    if compacted:
        stats["line_cleanup"] += compacted
    if marked:
        stats["marked_review_needed"] += marked

    return text, stats


def main() -> None:
    all_stats: Counter = Counter()
    changed_files: list[Path] = []

    for path in sorted(ROOT.rglob("*.md")):
        if path in SKIP_FILES:
            continue
        original = path.read_text(encoding="utf-8")
        cleaned, stats = clean_text(original)
        if cleaned != original:
            path.write_text(cleaned, encoding="utf-8", newline="\n")
            changed_files.append(path)
            all_stats.update(stats)

    print(f"changed_files {len(changed_files)}")
    print(f"total_md {len(list(ROOT.rglob('*.md')))}")
    print("\nTop changes:")
    for key, value in all_stats.most_common(100):
        print(f"{value:6} {key}")
    print("\nChanged file sample:")
    for path in changed_files[:40]:
        print(path)


if __name__ == "__main__":
    main()
