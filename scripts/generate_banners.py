#!/usr/bin/env python3
"""
generate_banners.py - Generate high-end, professional Star Trek LCARS profile banners
designed for quantitative Data Science & Operations Research recruitment.
"""

from pathlib import Path

def generate_banner(theme: str) -> str:
    is_dark = theme == "dark"

    # Refined professional color palette
    bg_gradient_start = "#080B11" if is_dark else "#F8FAFC"
    bg_gradient_end = "#0F172A" if is_dark else "#EDF2F7"
    
    lcars_amber = "#F59E0B" if is_dark else "#D97706"
    lcars_orange = "#EA580C" if is_dark else "#C2410C"
    lcars_cyan = "#38BDF8" if is_dark else "#0284C7"
    lcars_blue = "#60A5FA" if is_dark else "#2563EB"
    lcars_purple = "#8B5CF6" if is_dark else "#7C3AED"
    lcars_gold = "#FBBF24" if is_dark else "#B45309"
    
    text_primary = "#F8FAFC" if is_dark else "#0F172A"
    text_secondary = "#94A3B8" if is_dark else "#475569"
    text_accent = "#38BDF8" if is_dark else "#0284C7"
    border_color = "#1E293B" if is_dark else "#CBD5E1"
    grid_color = "#151F33" if is_dark else "#E2E8F0"
    
    pill_bg = "rgba(56, 189, 248, 0.08)" if is_dark else "rgba(2, 132, 199, 0.08)"
    pill_border = "rgba(56, 189, 248, 0.3)" if is_dark else "rgba(2, 132, 199, 0.25)"
    pill_text = "#7DD3FC" if is_dark else "#0369A1"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 320" width="1000" height="320" role="img" aria-label="Sebastián Ayala - Professional LCARS Data Science Banner">
  <defs>
    <linearGradient id="bg-grad-{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_gradient_start}"/>
      <stop offset="100%" stop-color="{bg_gradient_end}"/>
    </linearGradient>

    <linearGradient id="delta-grad-{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{lcars_gold}" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="{lcars_amber}" stop-opacity="0.35"/>
    </linearGradient>

    <pattern id="grid-pat-{theme}" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="{grid_color}" stroke-width="0.75" stroke-dasharray="2,4"/>
    </pattern>

    <filter id="soft-glow-{theme}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="1000" height="320" rx="14" fill="url(#bg-grad-{theme})"/>
  <rect width="1000" height="320" rx="14" fill="url(#grid-pat-{theme})" opacity="0.6"/>
  <rect x="1" y="1" width="998" height="318" rx="13" fill="none" stroke="{border_color}" stroke-width="1.2"/>

  <!-- Subtle Mathematical Coordinate Axes in Background -->
  <g opacity="{0.4 if is_dark else 0.2}">
    <line x1="720" y1="50" x2="950" y2="50" stroke="{lcars_cyan}" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="720" y1="270" x2="950" y2="270" stroke="{lcars_cyan}" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="720" y1="50" x2="720" y2="270" stroke="{lcars_cyan}" stroke-width="1" stroke-dasharray="4,4"/>
  </g>

  <!-- ================= LCARS ARCHITECTURAL FRAMEWORK ================= -->

  <!-- Top Horizontal LCARS Header Bar -->
  <path d="M 160 18 L 730 18 A 8 8 0 0 1 738 26 L 738 40 A 6 6 0 0 1 732 46 L 160 46 Z" fill="{lcars_amber}"/>

  <!-- Left Classic LCARS Elbow Bracket (Continuous L-Frame) -->
  <path d="M 28 68 
           A 32 32 0 0 1 60 36 
           L 148 36 
           L 148 44 
           L 70 44 
           A 22 22 0 0 0 48 66 
           L 48 252 
           A 22 22 0 0 0 70 274 
           L 148 274 
           L 148 282 
           L 60 282 
           A 32 32 0 0 1 28 250 
           Z" fill="{lcars_amber}"/>

  <!-- Top Segmented LCARS Header Blocks -->
  <rect x="748" y="18" width="75" height="28" rx="4" fill="{lcars_orange}"/>
  <rect x="831" y="18" width="85" height="28" rx="4" fill="{lcars_purple}"/>
  <rect x="924" y="18" width="48" height="28" rx="4" fill="{lcars_cyan}"/>

  <!-- Top Bar Monospace Text Elements -->
  <text x="172" y="36" font-family="ui-monospace, monospace" font-size="12" font-weight="800" fill="#000000" letter-spacing="1.5">LCARS-SYS-4701</text>
  <text x="312" y="36" font-family="ui-monospace, monospace" font-size="11" font-weight="700" fill="#000000" letter-spacing="1">QUANTITATIVE MODELING &amp; OPERATIONS RESEARCH</text>
  <text x="758" y="36" font-family="ui-monospace, monospace" font-size="10.5" font-weight="700" fill="#000000">OR-DEPT</text>
  <text x="842" y="36" font-family="ui-monospace, monospace" font-size="10.5" font-weight="700" fill="#000000">PHYS-MODEL</text>
  <text x="933" y="36" font-family="ui-monospace, monospace" font-size="10.5" font-weight="700" fill="#000000">MILP</text>

  <!-- Left Spine Navigation Blocks -->
  <rect x="28" y="84" width="72" height="28" rx="4" fill="{lcars_cyan}"/>
  <text x="36" y="103" font-family="ui-monospace, monospace" font-size="10" font-weight="800" fill="#000000">01 // MILP</text>

  <rect x="28" y="120" width="72" height="28" rx="4" fill="{lcars_purple}"/>
  <text x="36" y="139" font-family="ui-monospace, monospace" font-size="10" font-weight="800" fill="#000000">02 // PHYS</text>

  <rect x="28" y="156" width="72" height="28" rx="4" fill="{lcars_orange}"/>
  <text x="36" y="175" font-family="ui-monospace, monospace" font-size="10" font-weight="800" fill="#000000">03 // STAT</text>

  <rect x="28" y="192" width="72" height="28" rx="4" fill="{lcars_gold}"/>
  <text x="36" y="211" font-family="ui-monospace, monospace" font-size="10" font-weight="800" fill="#000000">04 // PROD</text>

  <!-- Bottom LCARS Horizontal Tray -->
  <path d="M 160 274 L 660 274 A 8 8 0 0 1 668 282 L 668 296 A 6 6 0 0 1 662 302 L 160 302 Z" fill="{lcars_cyan}"/>
  <rect x="678" y="274" width="144" height="28" rx="4" fill="{lcars_purple}"/>
  <rect x="830" y="274" width="142" height="28" rx="4" fill="{lcars_amber}"/>

  <text x="172" y="292" font-family="ui-monospace, monospace" font-size="10.5" font-weight="700" fill="#000000" letter-spacing="1">SYSTEM SPEC: SA-704-PHYS // OPTICAL DATA NETWORK: NOMINAL</text>
  <text x="688" y="292" font-family="ui-monospace, monospace" font-size="10.5" font-weight="700" fill="#000000">OPTIMALITY: 100%</text>
  <text x="840" y="292" font-family="ui-monospace, monospace" font-size="10.5" font-weight="700" fill="#000000">STATUS: PRODUCTION READY</text>

  <!-- ================= MAIN CONTENT & PROFESSIONAL TYPOGRAPHY ================= -->

  <!-- Top Metadata Breadcrumb -->
  <text x="124" y="84" font-family="ui-monospace, monospace" font-size="11.5" font-weight="700" fill="{lcars_amber}" letter-spacing="2">
    LCARS ADVANCED ANALYTICS DIRECTORY // SECTOR 001
  </text>

  <!-- Full Candidate Name -->
  <text x="124" y="128" font-family="ui-sans-serif, system-ui, -apple-system, sans-serif" font-size="38" font-weight="900" fill="{text_primary}" letter-spacing="2">
    SEBASTIÁN AYALA
  </text>

  <!-- Professional Title -->
  <text x="125" y="158" font-family="ui-sans-serif, system-ui, -apple-system, sans-serif" font-size="16.5" font-weight="700" fill="{text_accent}" letter-spacing="1">
    PHYSICIST &amp; DATA SCIENTIST  ·  OPERATIONS RESEARCH &amp; APPLIED ML
  </text>

  <!-- Concise Professional Summary -->
  <text x="125" y="186" font-family="ui-sans-serif, system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="{text_secondary}">
    Applying the mathematical rigor of complex physical systems to mixed-integer linear programming (MILP),
  </text>
  <text x="125" y="204" font-family="ui-sans-serif, system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="{text_secondary}">
    pricing dispersion modeling, and high-scale operational decision support.
  </text>

  <!-- Professional Capability Badges -->
  <!-- Pill 1: MILP Optimization -->
  <g transform="translate(125, 222)">
    <rect width="186" height="28" rx="6" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1.2"/>
    <text x="14" y="18" font-family="ui-monospace, monospace" font-size="11" font-weight="700" fill="{pill_text}">📐 MILP &amp; SciPy HiGHS</text>
  </g>

  <!-- Pill 2: Complex Systems -->
  <g transform="translate(321, 222)">
    <rect width="210" height="28" rx="6" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1.2"/>
    <text x="14" y="18" font-family="ui-monospace, monospace" font-size="11" font-weight="700" fill="{pill_text}">⚛️ Complex Physical Systems</text>
  </g>

  <!-- Pill 3: Supply Chain & Pricing -->
  <g transform="translate(541, 222)">
    <rect width="195" height="28" rx="6" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1.2"/>
    <text x="14" y="18" font-family="ui-monospace, monospace" font-size="11" font-weight="700" fill="{pill_text}">📊 Supply Chain &amp; Pricing</text>
  </g>

  <!-- ================= TECHNICAL GRAPHIC: VECTOR MATHEMATICAL CONVERGENCE ================= -->
  <g transform="translate(850, 155)">
    <!-- Mathematical Coordinate Rings / Pareto Frontier -->
    <ellipse cx="0" cy="0" rx="72" ry="32" fill="none" stroke="{lcars_cyan}" stroke-width="1.2" stroke-dasharray="3,3" opacity="0.7" transform="rotate(-20)"/>
    <ellipse cx="0" cy="0" rx="84" ry="24" fill="none" stroke="{lcars_amber}" stroke-width="1" stroke-dasharray="2,4" opacity="0.6" transform="rotate(35)"/>
    
    <!-- Geometric Starfleet Science Delta (Clean Precision Vector) -->
    <path d="M 0 -58 
             C 16 -12, 38 24, 44 50 
             C 28 42, 10 38, 0 42 
             C -10 38, -28 42, -44 50 
             C -38 24, -16 -12, 0 -58 Z" 
          fill="url(#delta-grad-{theme})" stroke="{lcars_gold}" stroke-width="1.8"/>

    <!-- Inner Mathematical Optimization Vector Symbol (Convergence Point) -->
    <circle cx="0" cy="8" r="4" fill="{lcars_cyan}"/>
    <circle cx="0" cy="8" r="10" fill="none" stroke="{lcars_cyan}" stroke-width="1.2" opacity="0.8"/>
  </g>

  <!-- Telemetry Readouts (Right Column) -->
  <g transform="translate(735, 95)" opacity="0.85">
    <line x1="0" y1="0" x2="25" y2="0" stroke="{lcars_cyan}" stroke-width="1.2"/>
    <line x1="0" y1="0" x2="0" y2="25" stroke="{lcars_cyan}" stroke-width="1.2"/>
    <text x="32" y="12" font-family="ui-monospace, monospace" font-size="9" font-weight="700" fill="{lcars_cyan}">CONVERGENCE: EXACT</text>
    <text x="32" y="24" font-family="ui-monospace, monospace" font-size="9" font-weight="700" fill="{lcars_cyan}">DUAL GAP: 0.00%</text>
  </g>

</svg>"""
    return svg

def main():
    assets_dir = Path("assets")
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    for theme in ("dark", "light"):
        content = generate_banner(theme)
        out_path = assets_dir / f"banner-{theme}.svg"
        out_path.write_text(content, encoding="utf-8")
        print(f"Generated {out_path}")

if __name__ == "__main__":
    main()
