#!/usr/bin/env python3
"""
radar.py - Render Star Trek LCARS styled standalone SVG radar charts.
Standard library only (math, json, argparse, pathlib).

Generates both -dark.svg and -light.svg for seamless GitHub theme adaptation
via <picture> and prefers-color-scheme.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

THEMES = {
    "dark": {
        "grid": "#222d3d",
        "spoke": "#192231",
        "label": "#e2e8f0",
        "value": "#38bdf8",
        "title": "#ff9900",
        "fill": "#00b4d8",
        "stroke": "#38bdf8",
        "vertex": "#ffb020",
        "bg": "none",
        "sublabel": "#94a3b8",
        "accent": "#ff9900",
    },
    "light": {
        "grid": "#cbd5e1",
        "spoke": "#e2e8f0",
        "label": "#0f172a",
        "value": "#0284c7",
        "title": "#b45309",
        "fill": "#0284c7",
        "stroke": "#0284c7",
        "vertex": "#d97706",
        "bg": "none",
        "sublabel": "#64748b",
        "accent": "#d97706",
    },
}

FONT = "ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
LBL, VAL, TTL = 12.5, 10.5, 14.5


def ring(radius: float, n: int, start: float = -math.pi / 2):
    return [
        (
            radius * math.cos(start + i * 2 * math.pi / n),
            radius * math.sin(start + i * 2 * math.pi / n),
        )
        for i in range(n)
    ]


def text_width(s: str, font_size: float) -> float:
    return len(s) * font_size * 0.62


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def render(title: str, axes: list[tuple[str, float]], theme: str, size: int, rings: int, show_values: bool, animate: bool) -> str:
    c = THEMES[theme]
    n = len(axes)
    r = size / 2 - 12
    gap = 22

    vals = [max(0.0, min(100.0, v)) for _, v in axes]
    outer = ring(r, n)

    labels = []
    for i, (label, _) in enumerate(axes):
        ang = -math.pi / 2 + i * 2 * math.pi / n
        cosv, sinv = math.cos(ang), math.sin(ang)
        lx, ly = (r + gap) * cosv, (r + gap) * sinv
        anchor = "middle" if abs(cosv) < 0.25 else ("start" if cosv > 0 else "end")
        dy = 4 if abs(sinv) < 0.25 else (14 if sinv > 0 else -6)
        labels.append((lx, ly + dy, anchor, label, vals[i]))

    minx, maxx, miny, maxy = -r, r, -r, r
    for lx, ly, anchor, label, v in labels:
        w = max(text_width(label, LBL), text_width(f"{v:g}%", VAL) if show_values else 0.0)
        if anchor == "start":
            x0, x1 = lx, lx + w
        elif anchor == "end":
            x0, x1 = lx - w, lx
        else:
            x0, x1 = lx - w / 2, lx + w / 2
        y0 = ly - LBL
        y1 = ly + 4 + (VAL + 4 if show_values else 0)
        minx, maxx = min(minx, x0), max(maxx, x1)
        miny, maxy = min(miny, y0), max(maxy, y1)

    pad = 16
    title_h = TTL + 18 if title else 0
    W = round((maxx - minx) + 2 * pad)
    H = round((maxy - miny) + 2 * pad + title_h)
    ox, oy = -minx + pad, -miny + pad + title_h

    if title:
        need = round(text_width(title, TTL) + 3 * pad)
        if need > W:
            ox += (need - W) / 2
            W = need

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'role="img" aria-label="{esc(title) or "radar chart"}" font-family="{FONT}">'
    ]

    # LCARS-inspired header accent bar
    if title:
        parts.append(f'<rect x="{pad}" y="{pad}" width="6" height="{TTL + 4}" rx="2" fill="{c["accent"]}"/>')
        parts.append(
            f'<text x="{pad + 14}" y="{pad + TTL - 1:.0f}" text-anchor="start" '
            f'font-size="{TTL}" font-weight="700" letter-spacing="0.8" fill="{c["title"]}">'
            f'{esc(title)}</text>'
        )
        parts.append(
            f'<text x="{W - pad}" y="{pad + TTL - 2:.0f}" text-anchor="end" '
            f'font-size="9.5" font-family="monospace" letter-spacing="1" fill="{c["sublabel"]}">'
            f'LCARS-SENSOR-SCAN // 001</text>'
        )

    parts.append(f'<g transform="translate({ox:.1f},{oy:.1f})">')

    # Subtle radar pulse backdrop circle
    parts.append(f'<circle cx="0" cy="0" r="{r}" fill="none" stroke="{c["grid"]}" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.45"/>')

    # Concentric rings
    for k in range(rings, 0, -1):
        radius_k = r * k / rings
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in ring(radius_k, n))
        parts.append(
            f'<polygon points="{d}" fill="none" stroke="{c["grid"]}" '
            f'stroke-width="1.2" opacity="{0.35 + 0.55 * k / rings:.2f}"/>'
        )

    # Spokes
    for x, y in outer:
        parts.append(
            f'<line x1="0" y1="0" x2="{x:.1f}" y2="{y:.1f}" '
            f'stroke="{c["spoke"]}" stroke-width="1.2"/>'
        )

    # Central target crosshair
    parts.append(f'<circle cx="0" cy="0" r="3" fill="{c["accent"]}" opacity="0.6"/>')

    # Data shape with SMIL smooth zoom-in animation
    shape = [(px * v / 100, py * v / 100) for (px, py), v in zip(outer, vals)]
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in shape)
    parts.append("<g>")
    if animate:
        parts.append(
            '<animateTransform attributeName="transform" type="scale" '
            'values="0.05;1" dur="1.2s" calcMode="spline" keyTimes="0;1" '
            'keySplines="0.22 1 0.36 1" fill="freeze"/>'
        )
    # Polygon data area
    parts.append(
        f'<polygon points="{d}" fill="{c["fill"]}" fill-opacity="0.28" '
        f'stroke="{c["stroke"]}" stroke-width="2.6" stroke-linejoin="round"/>'
    )
    # Vertex dots
    for x, y in shape:
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="{c["vertex"]}" '
            f'stroke="{c["stroke"]}" stroke-width="1.5"/>'
        )
    parts.append("</g>")

    # Labels and metric values
    for lx, ly, anchor, label, v in labels:
        parts.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" '
            f'font-size="{LBL}" font-weight="600" fill="{c["label"]}">'
            f'{esc(label)}</text>'
        )
        if show_values:
            parts.append(
                f'<text x="{lx:.1f}" y="{ly + VAL + 3:.1f}" text-anchor="{anchor}" '
                f'font-size="{VAL}" font-weight="700" font-family="monospace" fill="{c["value"]}">'
                f'{v:g}%</text>'
            )

    parts.append("</g></svg>")
    return "".join(parts)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data", type=Path, required=True, help="Path to JSON file with skills axes")
    p.add_argument("-o", "--out", type=Path, required=True, help="Output file base (without extension)")
    p.add_argument("--title", help="Override chart title")
    p.add_argument("--size", type=int, default=420)
    p.add_argument("--rings", type=int, default=4)
    p.add_argument("--values", action="store_true", default=True, help="Show percentage values on axes")
    p.add_argument("--no-animate", dest="animate", action="store_false", default=True, help="Disable SMIL animation")
    args = p.parse_args()

    if not args.data.exists():
        sys.exit(f"Data file not found: {args.data}")

    d = json.loads(args.data.read_text(encoding="utf-8"))
    title = args.title if args.title is not None else d.get("title", "LCARS Sensor Array")
    axes = [(a["label"], float(a["value"])) for a in d["axes"]]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    for theme in ("dark", "light"):
        svg = render(title, axes, theme, args.size, args.rings, args.values, args.animate)
        dest = args.out.with_name(f"{args.out.name}-{theme}.svg")
        dest.write_text(svg, encoding="utf-8")
        print(f"Generated {dest} ({len(axes)} axes)")


if __name__ == "__main__":
    main()
