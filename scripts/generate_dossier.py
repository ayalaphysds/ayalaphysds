#!/usr/bin/env python3
"""
generate_dossier.py - Generate high-end, professional Star Trek LCARS Officer
Dossier SVGs designed for quantitative Data Science & Operations Research recruitment.
"""

from pathlib import Path

def generate_dossier(theme: str) -> str:
    is_dark = theme == "dark"

    # Refined palette
    bg_shell = "#090C13" if is_dark else "#F1F5F9"
    card_bg = "#0E1420" if is_dark else "#FFFFFF"
    card_border = "#1E293B" if is_dark else "#CBD5E1"
    
    lcars_amber = "#F59E0B" if is_dark else "#D97706"
    lcars_orange = "#EA580C" if is_dark else "#C2410C"
    lcars_cyan = "#38BDF8" if is_dark else "#0284C7"
    lcars_purple = "#8B5CF6" if is_dark else "#7C3AED"
    lcars_gold = "#FBBF24" if is_dark else "#B45309"
    lcars_blue = "#60A5FA" if is_dark else "#2563EB"
    lcars_green = "#10B981" if is_dark else "#059669"
    
    text_primary = "#F8FAFC" if is_dark else "#0F172A"
    text_secondary = "#94A3B8" if is_dark else "#475569"
    text_cyan = "#38BDF8" if is_dark else "#0284C7"
    text_amber = "#F59E0B" if is_dark else "#B45309"
    text_purple = "#A78BFA" if is_dark else "#7C3AED"
    text_muted = "#64748B" if is_dark else "#94A3B8"
    divider_line = "#1E293B" if is_dark else "#E2E8F0"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 410" width="960" height="410" role="img" aria-label="LCARS Personnel Dossier - Sebastián Ayala">
  <defs>
    <linearGradient id="bar-grad-{theme}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{lcars_cyan}"/>
      <stop offset="100%" stop-color="{lcars_purple}"/>
    </linearGradient>
  </defs>

  <!-- Outer Console Terminal Frame -->
  <rect width="960" height="410" rx="14" fill="{bg_shell}"/>
  <rect x="2" y="2" width="956" height="406" rx="13" fill="none" stroke="{lcars_amber}" stroke-width="1.6" opacity="0.85"/>

  <!-- Top Bar: LCARS Pill Tabs and Terminal Heading -->
  <circle cx="34" cy="28" r="5" fill="{lcars_amber}"/>
  <circle cx="50" cy="28" r="5" fill="{lcars_cyan}"/>
  <circle cx="66" cy="28" r="5" fill="{lcars_purple}"/>

  <text x="88" y="32" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="12.5" font-weight="700" letter-spacing="1.5">
    LCARS-SYS-4701 // EXECUTIVE DOSSIER: SEBASTIÁN AYALA · PHYSICIST &amp; DATA SCIENTIST
  </text>
  <text x="930" y="32" text-anchor="end" fill="{lcars_green}" font-family="ui-monospace, monospace" font-size="11" font-weight="700" letter-spacing="1">
    ● TELEMETRY: OPTIMAL (SOLVER CONVERGED)
  </text>

  <!-- Top Dividing Line -->
  <path d="M 22 46 L 938 46" stroke="{divider_line}" stroke-width="1.2"/>

  <!-- ================= LEFT LCARS ELBOW & CONTROL SPINE ================= -->
  <!-- Classic LCARS Elbow Bracket -->
  <path d="M 22 58 
           L 92 58 
           A 12 12 0 0 1 104 70 
           L 104 82 
           A 8 8 0 0 1 96 90 
           L 42 90 
           A 6 6 0 0 0 36 96 
           L 36 380 
           A 6 6 0 0 0 42 386 
           L 96 386 
           A 8 8 0 0 1 104 394 
           L 104 396 
           A 10 10 0 0 1 94 402 
           L 22 402 
           A 10 10 0 0 1 12 392 
           L 12 68 
           A 10 10 0 0 1 22 58 Z" 
        fill="{lcars_amber}"/>

  <!-- Tactical Spine Nav Blocks -->
  <rect x="44" y="104" width="60" height="24" rx="4" fill="{lcars_cyan}"/>
  <text x="50" y="120" font-family="ui-monospace, monospace" font-size="9" font-weight="800" fill="#000000">01 // DOS</text>

  <rect x="44" y="134" width="60" height="24" rx="4" fill="{lcars_purple}"/>
  <text x="50" y="150" font-family="ui-monospace, monospace" font-size="9" font-weight="800" fill="#000000">02 // OR</text>

  <rect x="44" y="164" width="60" height="24" rx="4" fill="{lcars_orange}"/>
  <text x="50" y="180" font-family="ui-monospace, monospace" font-size="9" font-weight="800" fill="#000000">03 // MILP</text>

  <rect x="44" y="194" width="60" height="24" rx="4" fill="{lcars_gold}"/>
  <text x="50" y="210" font-family="ui-monospace, monospace" font-size="9" font-weight="800" fill="#000000">04 // PHYS</text>

  <rect x="44" y="224" width="60" height="24" rx="4" fill="{lcars_cyan}"/>
  <text x="50" y="240" font-family="ui-monospace, monospace" font-size="9" font-weight="800" fill="#000000">05 // ML</text>

  <rect x="44" y="254" width="60" height="24" rx="4" fill="{lcars_purple}"/>
  <text x="50" y="270" font-family="ui-monospace, monospace" font-size="9" font-weight="800" fill="#000000">06 // STAT</text>

  <rect x="44" y="284" width="60" height="24" rx="4" fill="{lcars_amber}"/>
  <text x="50" y="300" font-family="ui-monospace, monospace" font-size="9" font-weight="800" fill="#000000">07 // LIVE</text>

  <!-- ================= MAIN CONSOLE: CANDIDATE DOSSIER (CENTER) ================= -->
  <rect x="116" y="58" width="536" height="336" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>

  <!-- Command Line Prompt -->
  <text x="136" y="88" fill="{text_cyan}" font-family="ui-monospace, monospace" font-size="15" font-weight="800">
    ❯ cat /proc/quantitative_profile.json
  </text>

  <!-- Name & Professional Title -->
  <text x="136" y="116" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="16" font-weight="700">
    sebastián_ayala
  </text>
  <text x="286" y="116" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="15">—</text>
  <text x="306" y="116" fill="{text_amber}" font-family="ui-monospace, monospace" font-size="14.5" font-weight="700">
    Physicist &amp; Data Scientist
  </text>

  <!-- Academic Lineage & Focus -->
  <text x="136" y="142" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="12">background:</text>
  <text x="235" y="142" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="12" font-weight="600">
    B.S. Physics · Complex Systems &amp; Statistical Mechanics
  </text>

  <text x="136" y="164" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="12">specialty:</text>
  <text x="235" y="164" fill="{text_purple}" font-family="ui-monospace, monospace" font-size="12" font-weight="600">
    Operations Research (OR) · Mixed-Integer Linear Programming
  </text>

  <text x="136" y="186" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="12">location:</text>
  <text x="235" y="186" fill="{text_cyan}" font-family="ui-monospace, monospace" font-size="12">
    Cauquenes, Chile 🇨🇱 · LatAm / Global Remote
  </text>

  <!-- Inner Separator -->
  <path d="M 136 200 L 632 200" stroke="{divider_line}" stroke-width="1"/>

  <!-- Core Directive / Executive Value -->
  <text x="136" y="220" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="12">directive:</text>
  <text x="235" y="220" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="11.5">
    Applying physical modeling and mathematical optimization (MILP)
  </text>
  <text x="235" y="238" fill="{lcars_gold}" font-family="ui-monospace, monospace" font-size="11.5" font-weight="700">
    to resolve high-entropy operational bottlenecks &amp; pricing dispersion.
  </text>

  <!-- Sub-section: Core Disciplines -->
  <text x="136" y="272" fill="{text_cyan}" font-family="ui-monospace, monospace" font-size="13.5" font-weight="700">
    ❯ ls -la /disciplines/quantitative_core/
  </text>

  <text x="136" y="298" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="11.5" font-weight="700">drwx milp_optimization/</text>
  <text x="325" y="298" fill="{text_secondary}" font-family="ui-monospace, monospace" font-size="11.5">SciPy HiGHS · Linear &amp; Integer Programming</text>

  <text x="136" y="320" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="11.5" font-weight="700">drwx price_dispersion/</text>
  <text x="325" y="320" fill="{text_secondary}" font-family="ui-monospace, monospace" font-size="11.5">Statistical Mechanics · Resilient Econometrics</text>

  <text x="136" y="342" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="11.5" font-weight="700">drwx decision_cockpits/</text>
  <text x="325" y="342" fill="{text_secondary}" font-family="ui-monospace, monospace" font-size="11.5">Streamlit · Plotly · Executive Telemetry</text>

  <text x="136" y="364" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="11.5" font-weight="700">drwx enterprise_code/</text>
  <text x="325" y="364" fill="{text_secondary}" font-family="ui-monospace, monospace" font-size="11.5">Clean Architecture · Modularity · Testing</text>


  <!-- ================= RIGHT CONSOLE: MATHEMATICAL TELEMETRY ================= -->
  <rect x="668" y="58" width="270" height="336" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>

  <!-- Right Header -->
  <rect x="668" y="58" width="270" height="28" rx="8" fill="{lcars_purple}"/>
  <text x="680" y="77" font-family="ui-monospace, monospace" font-size="11" font-weight="800" fill="#FFFFFF" letter-spacing="1">
    MATHEMATICAL TELEMETRY // MATRIX
  </text>

  <!-- Metric Progress Bars (Clean Sci-Fi Telemetry) -->
  <g transform="translate(684, 102)">
    <!-- Metric 1: Math Rigor -->
    <text x="0" y="14" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="10" font-weight="700">MATHEMATICAL RIGOR</text>
    <text x="238" y="14" text-anchor="end" fill="{lcars_green}" font-family="ui-monospace, monospace" font-size="10.5" font-weight="800">99.2%</text>
    <rect x="0" y="20" width="238" height="6" rx="3" fill="#151E2E"/>
    <rect x="0" y="20" width="235" height="6" rx="3" fill="{lcars_green}"/>

    <!-- Metric 2: MILP Solver -->
    <text x="0" y="46" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="10" font-weight="700">MILP / HIGHS OPTIMALITY</text>
    <text x="238" y="46" text-anchor="end" fill="{lcars_cyan}" font-family="ui-monospace, monospace" font-size="10.5" font-weight="800">100.0%</text>
    <rect x="0" y="52" width="238" height="6" rx="3" fill="#151E2E"/>
    <rect x="0" y="52" width="238" height="6" rx="3" fill="{lcars_cyan}"/>

    <!-- Metric 3: Complex Systems -->
    <text x="0" y="78" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="10" font-weight="700">STOCHASTIC &amp; MONTE CARLO</text>
    <text x="238" y="78" text-anchor="end" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="10.5" font-weight="800">94.8%</text>
    <rect x="0" y="84" width="238" height="6" rx="3" fill="#151E2E"/>
    <rect x="0" y="84" width="225" height="6" rx="3" fill="{lcars_amber}"/>

    <!-- Metric 4: Production Architecture -->
    <text x="0" y="110" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="10" font-weight="700">CLEAN CODE ARCHITECTURE</text>
    <text x="238" y="110" text-anchor="end" fill="{lcars_purple}" font-family="ui-monospace, monospace" font-size="10.5" font-weight="800">96.0%</text>
    <rect x="0" y="116" width="238" height="6" rx="3" fill="#151E2E"/>
    <rect x="0" y="116" width="228" height="6" rx="3" fill="{lcars_purple}"/>
  </g>

  <!-- Optimization Diagnostic Summary Box -->
  <g transform="translate(684, 240)">
    <rect width="238" height="138" rx="6" fill="#090E17" stroke="{card_border}" stroke-width="1"/>
    
    <text x="12" y="24" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="11" font-weight="700">
      DIAGNOSTIC STATUS:
    </text>
    <text x="12" y="46" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="10.5">
      • Solver Engine: SciPy HiGHS Exact
    </text>
    <text x="12" y="66" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="10.5">
      • Dual Optimality Gap: 0.00%
    </text>
    <text x="12" y="86" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="10.5">
      • Constraints: Linear &amp; Integer Relaxed
    </text>
    <text x="12" y="106" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="10.5">
      • Decision Horizon: High-Scale Industrial
    </text>
    <text x="12" y="126" fill="{lcars_green}" font-family="ui-monospace, monospace" font-size="10.5" font-weight="700">
      • Verification: DETERMINISTIC
    </text>
  </g>

</svg>"""
    return svg

def main():
    assets_dir = Path("assets")
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    for theme in ("dark", "light"):
        content = generate_dossier(theme)
        out_path = assets_dir / f"lcars-whoami-{theme}.svg"
        out_path.write_text(content, encoding="utf-8")
        print(f"Generated {out_path}")
        
    (assets_dir / "lcars-whoami.svg").write_text(generate_dossier("dark"), encoding="utf-8")
    print("Generated default assets/lcars-whoami.svg")

if __name__ == "__main__":
    main()
