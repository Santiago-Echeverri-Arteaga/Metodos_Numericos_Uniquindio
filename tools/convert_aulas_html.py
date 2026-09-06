"""Convierte las páginas HTML autónomas de Aulas Virtuales a Markdown para GitHub."""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path


@dataclass
class Node:
    tag: str
    attrs: dict[str, str] = field(default_factory=dict)
    children: list[Node | str] = field(default_factory=list)


class TreeParser(HTMLParser):
    """Construye el subconjunto de DOM necesario sin dependencias externas."""

    void_tags = {"br", "hr", "img", "input", "meta", "link"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("document")
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = Node(tag, {key: value or "" for key, value in attrs})
        self.stack[-1].children.append(node)
        if tag not in self.void_tags:
            self.stack.append(node)

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self.void_tags:
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data: str) -> None:
        self.stack[-1].children.append(data)


def plain_text(node: Node | str) -> str:
    if isinstance(node, str):
        return node
    if node.tag in {"style", "script", "head"}:
        return ""
    separator = "\n" if node.tag in {"br", "p", "li", "tr", "div"} else ""
    return separator.join(plain_text(child) for child in node.children)


def compact(text: str) -> str:
    return re.sub(r"[ \t\r\f\v]+", " ", text).strip()


def render_inline(node: Node | str) -> str:
    if isinstance(node, str):
        return re.sub(r"\s+", " ", node)
    inner = "".join(render_inline(child) for child in node.children)
    if node.tag == "strong":
        return f"**{compact(inner)}**"
    if node.tag == "em":
        return f"*{compact(inner)}*"
    if node.tag == "code":
        value = compact(plain_text(node)).replace("`", "\\`")
        return f"`{value}`"
    if node.tag == "a":
        label = compact(inner)
        href = node.attrs.get("href", "")
        if not label:
            return ""
        if not href or href.startswith("#"):
            return label
        return f"[{label}]({href})"
    if node.tag == "br":
        return "<br>"
    if node.tag == "input" and node.attrs.get("type") == "checkbox":
        return "[x] " if "checked" in node.attrs else "[ ] "
    return inner


def descendants(node: Node, tag: str) -> list[Node]:
    found: list[Node] = []
    for child in node.children:
        if isinstance(child, Node):
            if child.tag == tag:
                found.append(child)
            found.extend(descendants(child, tag))
    return found


def render_table(node: Node) -> str:
    rows: list[list[str]] = []
    for row in descendants(node, "tr"):
        cells = [
            child
            for child in row.children
            if isinstance(child, Node) and child.tag in {"th", "td"}
        ]
        if cells:
            values = []
            for cell in cells:
                value = compact(render_inline(cell)).replace("|", "\\|")
                values.append(value or " ")
            rows.append(values)

    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [" "] * (width - len(row)) for row in rows]
    output = [
        "| " + " | ".join(rows[0]) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    output.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    return "\n".join(output) + "\n\n"


def render_list(node: Node, ordered: bool) -> str:
    lines: list[str] = []
    number = 1
    for child in node.children:
        if not isinstance(child, Node) or child.tag != "li":
            continue
        marker = f"{number}." if ordered else "-"
        value = compact(render_inline(child))
        lines.append(f"{marker} {value}")
        number += 1
    return "\n".join(lines) + "\n\n"


def render_block(node: Node | str) -> str:
    if isinstance(node, str):
        return ""
    if node.tag in {"head", "style", "script"}:
        return ""
    if node.tag in {"h1", "h2", "h3", "h4"}:
        level = int(node.tag[1])
        return f"{'#' * level} {compact(render_inline(node))}\n\n"
    if node.tag == "p":
        value = compact(render_inline(node))
        return f"{value}\n\n" if value else ""
    if node.tag == "blockquote":
        value = compact(render_inline(node))
        return "\n".join(f"> {line}" for line in value.splitlines()) + "\n\n"
    if node.tag == "pre":
        value = html.unescape(plain_text(node)).strip("\n")
        language = "python" if "python" in plain_text(node).lower() or "sourceCode" in str(node.attrs) else ""
        return f"```{language}\n{value}\n```\n\n"
    if node.tag == "table":
        return render_table(node)
    if node.tag == "ul":
        return render_list(node, ordered=False)
    if node.tag == "ol":
        return render_list(node, ordered=True)
    if node.tag == "hr":
        return "---\n\n"
    if node.tag == "footer":
        value = compact(render_inline(node))
        return f"---\n\n{value}\n" if value else ""
    return "".join(render_block(child) for child in node.children)


KNOWN_SOURCE_REPAIRS = {
    "03_unidad_3_algebra_lineal_numerica.html": {
        "| ` |   | x_aprox - x |\n| ` |   | r |": (
            "| Error absoluto `||x_aprox - x||` | Distancia a la solución exacta | "
            "Requiere conocer la solución exacta |\n"
            "| Norma del residuo `||r||` | Cumplimiento del sistema | Puede ser "
            "pequeña en sistemas mal condicionados |"
        ),
        "| Usar solo ` |   | x_{k+1}-x_k |": (
            "| Usar solo `||x_{k+1}-x_k||` | Puede confundir estancamiento con "
            "convergencia | Revisar también `||b-Ax||` |"
        ),
        "| Aceptar un valor propio sin residuo | La normalización no prueba corrección | Calcular ` |": (
            "| Aceptar un valor propio sin residuo | La normalización no prueba "
            "corrección | Calcular `||Av-λv||` |"
        ),
    },
    "04_unidad_4_ceros_y_minimizacion.html": {
        "| Cambio absoluto | ` | xₖ₊₁-xₖ |\n"
        "| Cambio relativo | ` | Δx |\n"
        "| Residuo | ` | f(xₖ) |\n"
        "| Intervalo | ` | b-a |": (
            "| Cambio absoluto | `|xₖ₊₁-xₖ|` | Estabilización en escala absoluta |\n"
            "| Cambio relativo | `|Δx|/(atol+rtol|x|)` | Estabilización respecto a "
            "la escala |\n"
            "| Residuo | `|f(xₖ)|` | Cumplimiento de la ecuación |\n"
            "| Intervalo | `|b-a|` | Cota geométrica en métodos con intervalo |"
        ),
    },
}


def repair_known_source_defects(source_name: str, markdown: str) -> str:
    """Repair table cells already truncated in the supplied Moodle HTML export."""
    for broken, corrected in KNOWN_SOURCE_REPAIRS.get(source_name, {}).items():
        if broken not in markdown:
            raise ValueError(f"No se encontró el fragmento esperado para reparar: {broken!r}")
        markdown = markdown.replace(broken, corrected)
    return markdown


def convert(source: Path, destination: Path) -> None:
    parser = TreeParser()
    parser.feed(source.read_text(encoding="utf-8-sig"))
    markdown = render_block(parser.root)
    markdown = repair_known_source_defects(source.name, markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"
    destination.write_text(markdown, encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()

    for source in sorted(args.directory.glob("*.html")):
        destination = source.with_suffix(".md")
        convert(source, destination)
        print(f"{source.name} -> {destination.name}")


if __name__ == "__main__":
    main()
