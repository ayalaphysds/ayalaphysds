#!/usr/bin/env python3
"""
generate_banners.py - Generate high-fidelity Star Trek LCARS profile banners
for both dark and light modes.
"""

from pathlib import Path

def generate_banner(theme: str) -> str:
    is_dark = theme == "dark"

    # Color tokens
    bg_gradient_start = "#06080F" if is_dark else "#F8FAFC"
    bg_gradient_end = "#0D1322" if is_dark else "#E2E8F0"
    
    lcars_amber = "#FF9900" if is_dark else "#D97706"
    lcars_orange = "#FF6600" if is_dark else "#EA580C"
    lcars_cyan = "#38BDF8" if is_dark else "#0284C7"
    lcars_blue = "#60A5FA" if is_dark else "#2563EB"
    lcars_magenta = "#CC6699" if is_dark else "#A21CAF"
    lcars_gold = "#FFCC00" if is_dark else "#CA8A04"
    
    text_primary = "#FFFFFF" if is_dark else "#0F172A"
    text_secondary = "#94A3B8" if is_dark else "#475569"
    text_accent = "#38BDF8" if is_dark else "#0284C7"
    border_color = "#1E293B" if is_dark else "#CBD5E1"
    grid_color = "#152033" if is_dark else "#E2E8F0"
    star_color = "#FFFFFF" if is_dark else "#94A3B8"
    star_opacity = "0.6" if is_dark else "0.3"
    
    tag_bg = "rgba(56, 189, 248, 0.12)" if is_dark else "rgba(2, 132, 199, 0.1)"
    tag_border = "rgba(56, 189, 248, 0.35)" if is_dark else "rgba(2, 132, 199, 0.3)"
    tag_text = "#7DD3FC" if is_dark else "#0369A1"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 320" width="1000" height="320" role="img" aria-label="Sebastián Ayala - Star Trek LCARS Banner">
  <defs>
    <linearGradient id="bg-grad-{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_gradient_start}"/>
      <stop offset="100%" stop-color="{bg_gradient_end}"/>
    </linearGradient>
    
    <linearGradient id="lcars-flow-{theme}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{lcars_amber}"/>
      <stop offset="40%" stop-color="{lcars_orange}"/>
      <stop offset="70%" stop-color="{lcars_magenta}"/>
      <stop offset="100%" stop-color="{lcars_cyan}"/>
    </linearGradient>

    <linearGradient id="delta-grad-{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{lcars_gold}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{lcars_amber}" stop-opacity="0.4"/>
    </linearGradient>

    <filter id="glow-{theme}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <pattern id="grid-pat-{theme}" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_color}" stroke-width="0.8" stroke-dasharray="2,4"/>
    </pattern>
  </defs>

  <!-- Outer Rounded Shell -->
  <rect width="1000" height="320" rx="16" fill="url(#bg-grad-{theme})"/>
  <rect width="1000" height="320" rx="16" fill="url(#grid-pat-{theme})" opacity="0.6"/>
  <rect x="1" y="1" width="998" height="318" rx="15" fill="none" stroke="{border_color}" stroke-width="1.5"/>

  <!-- Starfleet Sensor Grid & Starfield Dots -->
  <g opacity="{star_opacity}">
    <circle cx="280" cy="65" r="1.2" fill="{star_color}"/>
    <circle cx="340" cy="140" r="1" fill="{star_color}"/>
    <circle cx="490" cy="50" r="1.5" fill="{star_color}"/>
    <circle cx="580" cy="190" r="1" fill="{star_color}"/>
    <circle cx="720" cy="85" r="1.8" fill="{star_color}"/>
    <circle cx="810" cy="160" r="1.2" fill="{star_color}"/>
    <circle cx="890" cy="95" r="1" fill="{star_color}"/>
    <circle cx="940" cy="220" r="1.4" fill="{star_color}"/>
    <circle cx="650" cy="110" r="1" fill="{star_color}"/>
    <circle cx="420" cy="240" r="1.2" fill="{star_color}"/>
  </g>

  <!-- ================= LCARS ARCHITECTURAL FRAMEWORK ================= -->
  
  <!-- Top Horizontal Header LCARS Bar -->
  <path d="M 170 20 L 760 20 A 10 10 0 0 1 770 30 L 770 42 A 6 6 0 0 1 764 48 L 170 48 Z" fill="{lcars_amber}"/>
  
  <!-- Left Classic LCARS Elbow Bracket (Top-to-Side) -->
  <path d="M 30 75 
           A 35 35 0 0 1 65 40 
           L 155 40 
           L 155 48 
           L 75 48 
           A 25 25 0 0 0 50 73 
           L 50 245 
           A 25 25 0 0 0 75 270 
           L 155 270 
           L 155 278 
           L 65 278 
           A 35 35 0 0 1 30 243 
           Z" fill="{lcars_amber}"/>

  <!-- Top Segmented LCARS Header Blocks -->
  <rect x="780" y="20" width="70" height="28" rx="4" fill="{lcars_orange}"/>
  <rect x="858" y="20" width="60" height="28" rx="4" fill="{lcars_magenta}"/>
  <rect x="926" y="20" width="44" height="28" rx="4" fill="{lcars_cyan}"/>

  <!-- LCARS Code Pill Cuts inside Top Bar -->
  <text x="180" y="38" font-family="monospace" font-size="12" font-weight="800" fill="#000000" letter-spacing="1.5">LCARS-4701</text>
  <text x="310" y="38" font-family="monospace" font-size="11" font-weight="700" fill="#000000" letter-spacing="1">FEDERATION SCIENCE &amp; ANALYTICS DIRECTORY</text>
  <text x="790" y="38" font-family="monospace" font-size="10.5" font-weight="700" fill="#000000">SEC-001</text>
  <text x="866" y="38" font-family="monospace" font-size="10.5" font-weight="700" fill="#000000">OR-DIV</text>
  <text x="933" y="38" font-family="monospace" font-size="10.5" font-weight="700" fill="#000000">DS-9</text>

  <!-- Left Spine Navigation Tactile Blocks -->
  <rect x="30" y="90" width="70" height="30" rx="6" fill="{lcars_cyan}"/>
  <text x="40" y="110" font-family="monospace" font-size="11" font-weight="700" fill="#000000">01 // OR</text>

  <rect x="30" y="128" width="70" height="30" rx="6" fill="{lcars_magenta}"/>
  <text x="40" y="148" font-family="monospace" font-size="11" font-weight="700" fill="#000000">02 // PHYS</text>

  <rect x="30" y="166" width="70" height="30" rx="6" fill="{lcars_orange}"/>
  <text x="40" y="186" font-family="monospace" font-size="11" font-weight="700" fill="#000000">03 // MILP</text>

  <rect x="30" y="204" width="70" height="30" rx="6" fill="{lcars_gold}"/>
  <text x="40" y="224" font-family="monospace" font-size="11" font-weight="700" fill="#000000">04 // ML</text>

  <!-- Bottom LCARS Horizontal Tray -->
  <path d="M 170 270 L 680 270 A 10 10 0 0 1 690 280 L 690 292 A 6 6 0 0 1 684 298 L 170 298 Z" fill="{lcars_cyan}"/>
  <rect x="700" y="270" width="130" height="28" rx="4" fill="{lcars_magenta}"/>
  <rect x="838" y="270" width="132" height="28" rx="4" fill="{lcars_amber}"/>

  <text x="180" y="288" font-family="monospace" font-size="11" font-weight="700" fill="#000000" letter-spacing="1">STARDATE: 78432.9 // OPTICAL DATA NETWORK: ONLINE</text>
  <text x="710" y="288" font-family="monospace" font-size="10.5" font-weight="700" fill="#000000">WARP FACTOR: 9.8</text>
  <text x="846" y="288" font-family="monospace" font-size="10.5" font-weight="700" fill="#000000">STATUS: COMBAT READY</text>

  <!-- ================= HERO CONTENT & TYPOGRAPHY ================= -->

  <!-- Top Metadata Breadcrumb -->
  <text x="125" y="86" font-family="monospace" font-size="11" font-weight="700" fill="{lcars_amber}" letter-spacing="2">
    USS ENTERPRISE // ADVANCED QUANTITATIVE SYSTEMS
  </text>

  <!-- Candidate Name -->
  <text x="125" y="130" font-family="ui-sans-serif, system-ui, -apple-system, sans-serif" font-size="38" font-weight="900" fill="{text_primary}" letter-spacing="2.5">
    SEBASTIÁN AYALA
  </text>

  <!-- Professional Sub-Title -->
  <text x="126" y="160" font-family="ui-sans-serif, system-ui, -apple-system, sans-serif" font-size="17" font-weight="700" fill="{text_accent}" letter-spacing="1">
    PHYSICIST &amp; DATA SCIENTIST  ·  OPERATIONS RESEARCH &amp; APPLIED ML
  </text>

  <!-- Core Proposition / Mission statement -->
  <text x="126" y="188" font-family="ui-sans-serif, system-ui, -apple-system, sans-serif" font-size="13" font-weight="500" fill="{text_secondary}">
    Transforming complex physical systems &amp; operational entropy into deterministic, optimal business decisions.
  </text>

  <!-- Pill Specialization Badges -->
  <!-- Pill 1: MILP -->
  <g transform="translate(126, 210)">
    <rect width="180" height="28" rx="14" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1.2"/>
    <text x="14" y="18" font-family="monospace" font-size="11" font-weight="700" fill="{tag_text}">📐 MILP &amp; SciPy HiGHS</text>
  </g>

  <!-- Pill 2: Complex Systems -->
  <g transform="translate(316, 210)">
    <rect width="215" height="28" rx="14" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1.2"/>
    <text x="14" y="18" font-family="monospace" font-size="11" font-weight="700" fill="{tag_text}">⚛️ Complex Systems &amp; Monte Carlo</text>
  </g>

  <!-- Pill 3: Supply Chain -->
  <g transform="translate(541, 210)">
    <rect width="195" height="28" rx="14" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1.2"/>
    <text x="14" y="18" font-family="monospace" font-size="11" font-weight="700" fill="{tag_text}">📊 Supply Chain &amp; Pricing Models</text>
  </g>

  <!-- ================= STARFLEET ARTWORK (RIGHT WING) ================= -->
  <!-- Starfleet Command Delta Insignia Vector -->
  <g transform="translate(850, 150) scale(0.95)" filter="url(#glow-{theme})">
    <!-- Orbital trajectory rings -->
    <ellipse cx="0" cy="0" rx="75" ry="32" fill="none" stroke="{lcars_cyan}" stroke-width="1.2" stroke-dasharray="4,3" transform="rotate(-25)"/>
    <ellipse cx="0" cy="0" rx="90" ry="22" fill="none" stroke="{lcars_amber}" stroke-width="1" stroke-dasharray="2,4" transform="rotate(35)"/>
    
    <!-- Outer Starfleet Delta Frame -->
    <path d="M 0 -65 
             C 18 -15, 42 25, 48 55 
             C 32 45, 10 40, 0 46 
             C -10 40, -32 45, -48 55 
             C -42 25, -18 -15, 0 -65 Z" 
          fill="url(#delta-grad-{theme})" stroke="{lcars_gold}" stroke-width="2"/>
    
    <!-- Inner Science Division Emblem (Two interlocking ellipses / atom symbol) -->
    <ellipse cx="0" cy="0" rx="14" ry="7" fill="none" stroke="#000000" stroke-width="2.5" transform="rotate(-30)"/>
    <ellipse cx="0" cy="0" rx="14" ry="7" fill="none" stroke="#000000" stroke-width="2.5" transform="rotate(30)"/>
    <circle cx="0" cy="0" r="3" fill="#000000"/>
  </g>

  <!-- Decorative Telemetry Lines and Crosshairs -->
  <line x1="745" y1="95" x2="775" y2="95" stroke="{lcars_cyan}" stroke-width="1.5" opacity="0.6"/>
  <line x1="760" y1="80" x2="760" y2="110" stroke="{lcars_cyan}" stroke-width="1.5" opacity="0.6"/>
  <text x="740" y="125" font-family="monospace" font-size="9" font-weight="700" fill="{lcars_cyan}" opacity="0.75">GRID: SECTOR 001</text>
  <text x="740" y="137" font-family="monospace" font-size="9" font-weight="700" fill="{lcars_cyan}" opacity="0.75">SCAN: OPTIMAL</text>

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
