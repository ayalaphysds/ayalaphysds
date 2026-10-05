#!/usr/bin/env python3
"""
generate_dossier.py - Generate Star Trek LCARS Officer Terminal Dossier SVGs
for both dark and light modes.
"""

from pathlib import Path

def generate_dossier(theme: str) -> str:
    is_dark = theme == "dark"

    # Theme colors
    bg_shell = "#0A0D14" if is_dark else "#F1F5F9"
    card_bg = "#111622" if is_dark else "#FFFFFF"
    card_border = "#1E293B" if is_dark else "#CBD5E1"
    
    lcars_amber = "#FF9900" if is_dark else "#D97706"
    lcars_orange = "#FF6600" if is_dark else "#EA580C"
    lcars_cyan = "#38BDF8" if is_dark else "#0284C7"
    lcars_magenta = "#CC6699" if is_dark else "#A21CAF"
    lcars_gold = "#FFCC00" if is_dark else "#CA8A04"
    lcars_blue = "#60A5FA" if is_dark else "#2563EB"
    lcars_green = "#4ADE80" if is_dark else "#16A34A"
    
    text_primary = "#F8FAFC" if is_dark else "#0F172A"
    text_secondary = "#94A3B8" if is_dark else "#475569"
    text_cyan = "#38BDF8" if is_dark else "#0284C7"
    text_amber = "#FBBF24" if is_dark else "#B45309"
    text_purple = "#C084FC" if is_dark else "#7E22CE"
    text_muted = "#64748B" if is_dark else "#94A3B8"
    divider_line = "#1E293B" if is_dark else "#E2E8F0"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 410" width="960" height="410" role="img" aria-label="LCARS Personnel Dossier - Sebastián Ayala">
  <defs>
    <linearGradient id="elbow-flow-{theme}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{lcars_amber}"/>
      <stop offset="60%" stop-color="{lcars_orange}"/>
      <stop offset="100%" stop-color="{lcars_magenta}"/>
    </linearGradient>

    <linearGradient id="warp-core-{theme}" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="{lcars_cyan}" stop-opacity="0.2"/>
      <stop offset="50%" stop-color="{lcars_blue}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{lcars_cyan}" stop-opacity="0.2"/>
    </linearGradient>

    <filter id="core-glow-{theme}" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Outer Console Terminal Frame -->
  <rect width="960" height="410" rx="16" fill="{bg_shell}"/>
  <rect x="2" y="2" width="956" height="406" rx="15" fill="none" stroke="{lcars_amber}" stroke-width="1.8" opacity="0.85"/>

  <!-- Top Bar: LCARS Pill Tabs and Terminal Heading -->
  <circle cx="34" cy="30" r="5.5" fill="{lcars_amber}"/>
  <circle cx="52" cy="30" r="5.5" fill="{lcars_cyan}"/>
  <circle cx="70" cy="30" r="5.5" fill="{lcars_magenta}"/>

  <text x="96" y="35" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="13.5" font-weight="700" letter-spacing="1.5">
    LCARS-SYS-4701 // STARFLEET SCIENCE DIRECTORY // SECTOR 001
  </text>
  <text x="930" y="35" text-anchor="end" fill="{lcars_green}" font-family="ui-monospace, monospace" font-size="11.5" font-weight="700" letter-spacing="1">
    ● SUBSPACE LINK: STABLE (STARDATE 78432.9)
  </text>

  <!-- Top Dividing Line -->
  <path d="M 24 50 L 936 50" stroke="{divider_line}" stroke-width="1.5"/>

  <!-- ================= LEFT LCARS ELBOW & CONTROL SPINE ================= -->
  <!-- Classic LCARS Elbow Bracket -->
  <path d="M 24 64 
           L 94 64 
           A 14 14 0 0 1 108 78 
           L 108 90 
           A 8 8 0 0 1 100 98 
           L 44 98 
           A 6 6 0 0 0 38 104 
           L 38 376 
           A 6 6 0 0 0 44 382 
           L 100 382 
           A 8 8 0 0 1 108 390 
           L 108 392 
           A 10 10 0 0 1 98 402 
           L 24 402 
           A 10 10 0 0 1 14 392 
           L 14 74 
           A 10 10 0 0 1 24 64 Z" 
        fill="{lcars_amber}"/>

  <!-- Tactical Spine Nav Blocks -->
  <rect x="46" y="112" width="60" height="24" rx="4" fill="{lcars_cyan}"/>
  <text x="52" y="128" font-family="monospace" font-size="9.5" font-weight="800" fill="#000000">01 // DOS</text>

  <rect x="46" y="142" width="60" height="24" rx="4" fill="{lcars_magenta}"/>
  <text x="52" y="158" font-family="monospace" font-size="9.5" font-weight="800" fill="#000000">02 // DIR</text>

  <rect x="46" y="172" width="60" height="24" rx="4" fill="{lcars_orange}"/>
  <text x="52" y="188" font-family="monospace" font-size="9.5" font-weight="800" fill="#000000">03 // OPT</text>

  <rect x="46" y="202" width="60" height="24" rx="4" fill="{lcars_gold}"/>
  <text x="52" y="218" font-family="monospace" font-size="9.5" font-weight="800" fill="#000000">04 // OR</text>

  <rect x="46" y="232" width="60" height="24" rx="4" fill="{lcars_cyan}"/>
  <text x="52" y="248" font-family="monospace" font-size="9.5" font-weight="800" fill="#000000">05 // ML</text>

  <rect x="46" y="262" width="60" height="24" rx="4" fill="{lcars_magenta}"/>
  <text x="52" y="278" font-family="monospace" font-size="9.5" font-weight="800" fill="#000000">06 // STAT</text>

  <rect x="46" y="292" width="60" height="24" rx="4" fill="{lcars_amber}"/>
  <text x="52" y="308" font-family="monospace" font-size="9.5" font-weight="800" fill="#000000">07 // LIVE</text>

  <!-- ================= MAIN CONSOLE: OFFICER DOSSIER (CENTER) ================= -->
  <rect x="120" y="64" width="536" height="328" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>

  <!-- Command Line Prompt -->
  <text x="140" y="94" fill="{text_cyan}" font-family="ui-monospace, monospace" font-size="16" font-weight="800">
    ❯ cat /starfleet/personnel/sebastián_ayala.log
  </text>

  <!-- Officer Name & Role -->
  <text x="140" y="122" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="16" font-weight="700">
    sebastián_ayala
  </text>
  <text x="290" y="122" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="15">—</text>
  <text x="310" y="122" fill="{text_amber}" font-family="ui-monospace, monospace" font-size="14.5" font-weight="700">
    Physicist &amp; Data Scientist
  </text>

  <!-- Division & Academic Lineage -->
  <text x="140" y="148" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="12.5">specialty:</text>
  <text x="235" y="148" fill="{text_purple}" font-family="ui-monospace, monospace" font-size="12.5" font-weight="600">
    Operations Research (OR) · MILP Optimization
  </text>

  <text x="140" y="170" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="12.5">lineage:</text>
  <text x="235" y="170" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="12.5">
    Theoretical &amp; Applied Physics (Complex Systems &amp; Thermo)
  </text>

  <text x="140" y="192" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="12.5">coordinates:</text>
  <text x="235" y="192" fill="{text_cyan}" font-family="ui-monospace, monospace" font-size="12.5">
    Cauquenes, Chile 🇨🇱 · Sector 001
  </text>

  <!-- Inner Separator -->
  <path d="M 140 206 L 636 206" stroke="{divider_line}" stroke-width="1"/>

  <!-- Prime Directive / Mission Statement -->
  <text x="140" y="226" fill="{text_muted}" font-family="ui-monospace, monospace" font-size="12.5">mission:</text>
  <text x="235" y="226" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="12">
    Transforming high-entropy complex systems into
  </text>
  <text x="235" y="244" fill="{lcars_gold}" font-family="ui-monospace, monospace" font-size="12" font-weight="700">
    deterministic, optimal business decisions &amp; algorithms.
  </text>

  <!-- Sub-section: Specializations -->
  <text x="140" y="278" fill="{text_cyan}" font-family="ui-monospace, monospace" font-size="14.5" font-weight="700">
    ❯ ls -la /division/tactical_capabilities/
  </text>

  <text x="140" y="306" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="12" font-weight="700">drwx milp_optimization/</text>
  <text x="325" y="306" fill="{text_secondary}" font-family="ui-monospace, monospace" font-size="12">SciPy HiGHS · Linear Prog · Allocation</text>

  <text x="140" y="328" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="12" font-weight="700">drwx price_dispersion/</text>
  <text x="325" y="328" fill="{text_secondary}" font-family="ui-monospace, monospace" font-size="12">Statistical Mechanics · Resilient Pricing</text>

  <text x="140" y="350" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="12" font-weight="700">drwx decision_dashboards/</text>
  <text x="325" y="350" fill="{text_secondary}" font-family="ui-monospace, monospace" font-size="12">Streamlit · Plotly · Executive Telemetry</text>

  <text x="140" y="372" fill="{lcars_amber}" font-family="ui-monospace, monospace" font-size="12" font-weight="700">drwx production_pipelines/</text>
  <text x="325" y="372" fill="{text_secondary}" font-family="ui-monospace, monospace" font-size="12">Clean Architecture · CI/CD · Modularity</text>


  <!-- ================= RIGHT CONSOLE: WARP CORE & SENSOR ARRAY ================= -->
  <rect x="670" y="64" width="266" height="328" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>

  <!-- Right Header -->
  <rect x="670" y="64" width="266" height="28" rx="8" fill="{lcars_magenta}"/>
  <text x="682" y="83" font-family="ui-monospace, monospace" font-size="11" font-weight="800" fill="#000000" letter-spacing="1">
    WARP CORE // SENSOR TELEMETRY
  </text>

  <!-- Animated Warp Core Reactor Chamber -->
  <g transform="translate(710, 110)">
    <!-- Reactor housing frame -->
    <rect width="64" height="150" rx="8" fill="#0B0F19" stroke="{lcars_cyan}" stroke-width="1.5"/>
    
    <!-- Chamber ribs -->
    <line x1="0" y1="30" x2="64" y2="30" stroke="{card_border}" stroke-width="1.5"/>
    <line x1="0" y1="60" x2="64" y2="60" stroke="{card_border}" stroke-width="1.5"/>
    <line x1="0" y1="90" x2="64" y2="90" stroke="{card_border}" stroke-width="1.5"/>
    <line x1="0" y1="120" x2="64" y2="120" stroke="{card_border}" stroke-width="1.5"/>

    <!-- Pulsing plasma energy conduit -->
    <rect x="18" y="10" width="28" height="130" rx="4" fill="url(#warp-core-{theme})" filter="url(#core-glow-{theme})">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2s" repeatCount="indefinite"/>
    </rect>

    <!-- Energy core rings -->
    <circle cx="32" cy="75" r="14" fill="none" stroke="{lcars_gold}" stroke-width="2">
      <animate attributeName="r" values="8;18;8" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Tactical Metric Readouts (Right Column) -->
  <g transform="translate(786, 115)">
    <text x="0" y="15" fill="{text_muted}" font-family="monospace" font-size="9" font-weight="700">RIGOR &amp; MATH</text>
    <text x="0" y="30" fill="{lcars_green}" font-family="monospace" font-size="12" font-weight="800">98.5% NOMINAL</text>

    <text x="0" y="55" fill="{text_muted}" font-family="monospace" font-size="9" font-weight="700">MILP EFFICIENCY</text>
    <text x="0" y="70" fill="{lcars_cyan}" font-family="monospace" font-size="12" font-weight="800">HiGHS OPTIMAL</text>

    <text x="0" y="95" fill="{text_muted}" font-family="monospace" font-size="9" font-weight="700">CODE MODULARITY</text>
    <text x="0" y="110" fill="{lcars_gold}" font-family="monospace" font-size="12" font-weight="800">CLEAN ARCH</text>

    <text x="0" y="135" fill="{text_muted}" font-family="monospace" font-size="9" font-weight="700">WARP FACTOR</text>
    <text x="0" y="150" fill="{lcars_magenta}" font-family="monospace" font-size="12" font-weight="800">WARP 9.8</text>
  </g>

  <!-- Lower Tactical Diagnostic Strip -->
  <g transform="translate(684, 280)">
    <rect width="238" height="96" rx="6" fill="#0B0F19" stroke="{card_border}" stroke-width="1"/>
    
    <text x="12" y="24" fill="{lcars_amber}" font-family="monospace" font-size="11" font-weight="700">
      DIAGNOSTIC STATUS:
    </text>
    <text x="12" y="44" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="10.5">
      • Decision engines: VERIFIED
    </text>
    <text x="12" y="62" fill="{text_primary}" font-family="ui-monospace, monospace" font-size="10.5">
      • Supply constraints: BALANCED
    </text>
    <text x="12" y="80" fill="{lcars_green}" font-family="ui-monospace, monospace" font-size="10.5" font-weight="700">
      • Ready for Executive Briefing
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
        
    # Also save default lcars-whoami.svg as dark
    (assets_dir / "lcars-whoami.svg").write_text(generate_dossier("dark"), encoding="utf-8")
    print("Generated default assets/lcars-whoami.svg")

if __name__ == "__main__":
    main()
