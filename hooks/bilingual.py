"""MkDocs hook: turn the EN/VI pairs in the source .md into toggleable HTML.

The source file stays exactly as you write it (LaTeX colour lines, "EN / VI"
headings, 3-column tables). This hook rewrites it at build time into:

    <span class="bi"><span class="en">English</span><span class="vi">Tiếng Việt</span></span>

Headings keep only the English text in the heading itself; the Vietnamese text
goes into a data-vi attribute, so the sidebar / table of contents stay English.
CSS and JS (assets/bilingual.*) decide what is shown.

Opt-in per page: only pages whose front matter has `bilingual: true` are
converted. Every other page is passed through untouched.

Extra, easier syntax (instead of the LaTeX colour lines):

    EN: English sentence.
    VI: Câu tiếng Việt.

    - EN: A list item.
      VI: Một mục danh sách.

    | Command | Purpose (EN) | Mục đích (VI) |
    |---|---|---|
    | `ls` | List files | Liệt kê tệp |
"""

import html
import re

# One colour token: $\color{RoyalBlue}{\textbf{...}}$ (EN) or
# $\color{#374151}{\footnotesize\text{...}}$ (VI)
TOK = re.compile(
    r"\$\\color\{(RoyalBlue|#374151)\}\{(?:\\textbf|\\footnotesize\\text)\{(.*?)\}\}\$"
)
TOK_SRC = r"\$\\color\{(?:RoyalBlue|#374151)\}\{(?:\\textbf|\\footnotesize\\text)\{.*?\}\}\$"
# Consecutive tokens glued by <br> (the usual EN lines followed by VI lines)
GROUP = re.compile(TOK_SRC + r"(?:\s*<br>\s*" + TOK_SRC + r")*")
BOLD_WRAPPED = re.compile(r"\*\*(\$\\color[^$]*\$)\*\*")
PAREN_PAIR = re.compile(r"\(([^()/]*?) / ([^()]*?)\)")
# "EN: ..." line followed by "VI: ..." line (optionally as a list item)
EN_VI = re.compile(
    # group 1 = indentation (admonition / tab content) + optional list marker
    r"^([ \t]*(?:(?:[-*+]|\d+\.)[ \t]+)?)EN:[ \t]*(.+)\n[ \t]*VI:[ \t]*(.+)$", re.M
)

VIET = re.compile(
    "[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]",
    re.I,
)


def bi(en, vi, inline=False):
    cls = "bi bi-inline" if inline else "bi"
    if not vi:
        return f'<span class="{cls}"><span class="en">{en}</span></span>'
    return (
        f'<span class="{cls}"><span class="en">{en}</span>'
        f'<span class="vi">{vi}</span></span>'
    )


def split_bilingual(s):
    """Split 'English / Tiếng Việt' where English itself may contain ' / '."""
    parts = s.split(" / ")
    if len(parts) < 2:
        return None
    for i in range(1, len(parts)):
        left = " / ".join(parts[:i])
        right = " / ".join(parts[i:])
        if not VIET.search(left) and VIET.search(parts[i]):
            return left.strip(), right.strip()
    if len(parts) == 2:  # e.g. "Kernel Modules / Kernel module" (no diacritics)
        return parts[0].strip(), parts[1].strip()
    return None


def group_sub(m):
    en, vi = [], []
    for t in TOK.finditer(m.group(0)):
        (en if t.group(1) == "RoyalBlue" else vi).append(t.group(2).strip())
    return bi(" ".join(en), " ".join(vi))


def split_cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def paren_sub(m):
    en, vi = m.group(1), m.group(2)
    if VIET.search(vi):
        return "(" + bi(en, vi, inline=True) + ")"
    return m.group(0)


def convert_cell(cell):
    if "`" in cell:
        return PAREN_PAIR.sub(paren_sub, cell)
    sp = split_bilingual(cell)
    return bi(*sp) if sp else cell


def convert_table(block):
    rows = [split_cells(l) for l in block]
    # Layout C: | Command | Purpose (EN) | Mục đích (VI) |  with plain cells
    if (
        len(rows) >= 3
        and all(len(r) == 3 for r in rows)
        and rows[0][1].endswith("(EN)")
        and rows[0][2].endswith("(VI)")
    ):
        head = f"| {rows[0][0]} | {bi(rows[0][1][:-4].strip(), rows[0][2][:-4].strip())} |"
        data = [f"| {r[0]} | {bi(r[1], r[2])} |" for r in rows[2:]]
        return [head, "|---|---|"] + data
    # Layout A: | Command | EN cell | VI cell |  ->  | Command | EN/VI |
    if len(rows) >= 3 and all(len(r) == 3 for r in rows):
        data = []
        for r in rows[2:]:
            a, b = TOK.fullmatch(r[1]), TOK.fullmatch(r[2])
            if not (a and b and a.group(1) == "RoyalBlue" and b.group(1) == "#374151"):
                data = None
                break
            data.append(f"| {r[0]} | {bi(a.group(2).strip(), b.group(2).strip())} |")
        if data is not None:
            head = f"| {rows[0][0]} | {bi(rows[0][1], rows[0][2])} |"
            return [head, "|---|---|"] + data
    # Layout B: cells like "English / Tiếng Việt"
    out = []
    for k, r in enumerate(rows):
        if k == 1:
            out.append(block[1])
        else:
            out.append("| " + " | ".join(convert_cell(c) for c in r) + " |")
    return out


def convert_tables(lines):
    out, i = [], 0
    while i < len(lines):
        if lines[i].startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            out.extend(convert_table(lines[i:j]))
            i = j
        else:
            out.append(lines[i])
            i += 1
    return out


def convert_line(line):
    m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
    if m:
        sp = split_bilingual(m.group(2))
        if sp:
            en, vi = sp
            return (
                f'{m.group(1)} {en}<span class="vi-h" '
                f'data-vi="{html.escape(vi, quote=True)}"></span>'
            )
        return line
    m = re.match(r"^\*\*(.+?)\*\*$", line)
    if m:
        inner = m.group(1)
        colon = ":" if inner.endswith(":") else ""
        sp = split_bilingual(inner.rstrip(":"))
        if sp:
            return bi(f"<strong>{sp[0]}{colon}</strong>", f"{sp[1]}{colon}")
    return line


def convert_chunk(lines):
    # The "English: blue · Tiếng Việt: xám" legend is meaningless on the site.
    lines = [l for l in lines if "English: blue" not in l]
    text = BOLD_WRAPPED.sub(r"\1", "\n".join(lines))
    lines = convert_tables(text.split("\n"))
    lines = [convert_line(l) for l in lines]
    text = EN_VI.sub(
        lambda m: (m.group(1) or "") + bi(m.group(2).strip(), m.group(3).strip()),
        "\n".join(lines),
    )
    return GROUP.sub(group_sub, text).split("\n")


def on_page_markdown(markdown, page, config, files):
    # Opt-in: only pages with `bilingual: true` in their front matter.
    if not (getattr(page, "meta", None) or {}).get("bilingual"):
        return markdown
    out, chunk, fence = [], [], False

    def flush():
        if chunk:
            out.extend(convert_chunk(chunk))
            chunk.clear()

    for line in markdown.split("\n"):
        if line.lstrip().startswith("```"):
            if not fence:
                flush()
            fence = not fence
            out.append(line)
        elif fence:
            out.append(line)
        else:
            chunk.append(line)
    flush()
    return "\n".join(out)
