"""Generate the profile README cards in one "glass navy" style.

Writes assets/<card>-glass.svg for: about, skills, journey, how-i-work.
The cards carry their own translucent navy surface, so the same image reads
well on GitHub's light and dark pages; no theme switching is needed.

Usage: python3 scripts/gen_cards.py
After changing a card, bump the file names (e.g. -glass-v2) in the README too:
raw.githubusercontent.com caches images for a while.
"""
from pathlib import Path
from xml.sax.saxutils import escape

# A token is a hex color, or (hex, opacity) for translucent layers.
GLASS = {
    "grad_from": "#093060", "grad_to": "#22468A", "surface_opacity": 0.92,
    "title": "#FFFFFF", "text": "#D5DEEA", "muted": "#A9B6D3", "sep": "#7F93B5",
    "accent": "#E2B394", "chip_fg": "#FFFFFF", "node": "#FFFFFF", "node_fg": "#093060",
    "tag_bg": "#B07152",
    "panel": ("#FFFFFF", 0.07), "border": ("#FFFFFF", 0.14), "rule": ("#FFFFFF", 0.14),
    "chip_bg": ("#FFFFFF", 0.14), "rail": ("#FFFFFF", 0.28),
}
T = GLASS

FONT = "'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
FADE = """.fade { animation: fade .8s ease-out both; }
    .d2 { animation-delay: .15s; } .d3 { animation-delay: .3s; } .d4 { animation-delay: .45s; }
    @keyframes fade { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: none; } }
    @media (prefers-reduced-motion: reduce) { .fade { animation: none; } }"""


def fill(key):
    tok = T[key]
    if isinstance(tok, tuple):
        return f'fill="{tok[0]}" fill-opacity="{tok[1]}"'
    return f'fill="{tok}"'


def stroke(key, width=1):
    tok = T[key]
    if isinstance(tok, tuple):
        return f'stroke="{tok[0]}" stroke-opacity="{tok[1]}" stroke-width="{width}"'
    return f'stroke="{tok}" stroke-width="{width}"'


def svg(w, h, label, css, body):
    defs = (f'<defs>'
            f'<linearGradient id="surface" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{T["grad_from"]}"/><stop offset="1" stop-color="{T["grad_to"]}"/>'
            f'</linearGradient>'
            f'<linearGradient id="sheen" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="#FFFFFF" stop-opacity=".12"/>'
            f'<stop offset=".45" stop-color="#FFFFFF" stop-opacity="0"/>'
            f'</linearGradient></defs>')
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">',
        f"  <style>\n    text {{ font-family: {FONT}; }}\n    {css}\n    {FADE}\n  </style>",
        f"  {defs}",
        f'  <rect width="{w}" height="{h}" rx="12" fill="url(#surface)" fill-opacity="{T["surface_opacity"]}"/>',
        f'  <rect width="{w}" height="{h}" rx="12" fill="url(#sheen)"/>',
        f'  <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="11.5" fill="none" stroke="#FFFFFF" stroke-opacity=".18"/>',
        *("  " + ln for ln in body),
        "</svg>",
    ]) + "\n"


def text_w(s, px):
    return len(s) * px * 0.6


def pill(x, y, w, h, paint, label, cls):
    return (f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="{h / 2}" {paint}/>'
            f'<text class="{cls}" x="{x + w / 2:.1f}" y="{y + h / 2 + 4.2:.1f}" text-anchor="middle">{escape(label)}</text>')


# ---------------------------------------------------------------- about
def about():
    css = f""".sum {{ font-size: 15px; fill: {T["text"]}; }}
    .b {{ font-weight: 700; fill: {T["title"]}; }}
    .label {{ font-size: 11px; font-weight: 700; fill: {T["accent"]}; letter-spacing: 1.5px; }}
    .name {{ font-size: 15px; font-weight: 700; fill: {T["title"]}; letter-spacing: .4px; }}
    .meta {{ font-size: 13px; fill: {T["muted"]}; }}
    .item {{ font-size: 14px; fill: {T["text"]}; }}"""
    panel = f'rx="10" {fill("panel")} {stroke("border")}'
    focus = ["Reliable, maintainable backend services and clean API design",
             "Service integrations, authentication and authorization",
             "Database design, data modeling and query performance",
             "Stable releases, production environments and troubleshooting",
             "AI-assisted engineering with Claude Code and OpenAI Codex"]
    body = [
        '<g class="fade">',
        '<text class="sum" x="36" y="62">Software Engineer with hands-on experience designing, building, deploying and maintaining production</text>',
        '<text class="sum" x="36" y="86">backend systems. I work across <tspan class="b">PHP/Laravel</tspan> and <tspan class="b">Python/FastAPI</tspan> with '
        '<tspan class="b">PostgreSQL</tspan> and <tspan class="b">MySQL</tspan>, owning</text>',
        '<text class="sum" x="36" y="110">features end to end, from API design and data modeling to deployment, monitoring and troubleshooting.</text>',
        '</g>',
        '<g class="fade d2">',
        f'<rect x="36" y="138" width="330" height="218" {panel}/>',
        '<text class="label" x="56" y="166">CURRENTLY</text>',
        '<text class="name" x="56" y="192">PAYSTAR</text>',
        '<text class="meta" x="56" y="211">Software Engineer · Full-time</text>',
        '<text class="name" x="56" y="238">AVINA IT SOLUTIONS</text>',
        '<text class="meta" x="56" y="257">Software Engineer · Part-time</text>',
        '<text class="label" x="56" y="290">EDUCATION</text>',
        '<text class="name" x="56" y="316">B.Sc. Computer Engineering</text>',
        '<text class="meta" x="56" y="335">University of Guilan · 2020–2024</text>',
        '</g>',
        '<g class="fade d3">',
        f'<rect x="378" y="138" width="486" height="218" {panel}/>',
        '<text class="label" x="398" y="166">FOCUS AREAS</text>',
    ]
    for i, item in enumerate(focus):
        y = 194 + i * 32
        body += [f'<circle cx="403" cy="{y - 5}" r="3.5" fill="{T["accent"]}"/>',
                 f'<text class="item" x="416" y="{y}">{escape(item)}</text>']
    body.append('</g>')
    return svg(900, 392, "About", css, body)


# ---------------------------------------------------------------- skills
SKILLS = [
    ("BACKEND", ["PHP", "Laravel", "Python", "FastAPI"],
     ["RESTful APIs", "API Design", "Service Integration", "Authentication & Authorization"]),
    ("LARAVEL", ["Queues & Jobs", "Middleware", "Validation", "Eloquent ORM", "Sanctum", "Passport"], []),
    ("DATA", ["PostgreSQL", "MySQL", "Redis"], ["Database Design", "Data Modeling", "Query Optimization"]),
    ("PRODUCTION", ["Linux", "Ubuntu", "AWS", "Docker", "GitHub Actions", "Terraform"],
     ["VPS", "Server Configuration", "Application Deployment", "Production Environments",
      "Release Management", "Monitoring", "Troubleshooting"]),
    ("TESTING", ["Cypress", "Postman", "Hoppscotch"],
     ["Automated, API, Functional & Regression Testing", "Bug Analysis & Reporting"]),
    ("TOOLS", ["Git", "GitHub", "GitLab", "Composer", "DirectAdmin"], []),
    ("AI-ASSISTED", ["Claude Code", "OpenAI Codex"],
     ["AI Coding Agents", "Agentic Workflows", "AI-assisted Debugging & Refactoring",
      "Code Review & Documentation", "Technical Analysis", "Development Automation"]),
    ("PRACTICES", [], ["Software Design", "OOP", "SOLID", "MVC", "Clean Code", "Refactoring",
                       "Debugging", "Code Review", "Technical Problem Solving"]),
]


def skills():
    W, PAD, VAL_X, LH, ROW_PAD, SEP = 900, 36, 250, 22, 14, " · "
    VAL_W = W - PAD - VAL_X
    css = f"""text {{ font-size: 14px; }}
    .label {{ font-size: 12px; font-weight: 700; fill: {T["accent"]}; letter-spacing: 1.4px; }}
    .tool {{ font-weight: 700; fill: {T["title"]}; }}
    .con {{ fill: {T["text"]}; }}
    .sep {{ fill: {T["sep"]}; }}"""

    def flow(tools, concepts):
        items = [(x, "tool", 8.0) for x in tools] + [(x, "con", 7.0) for x in concepts]
        lines, cur, cur_w = [], [], 0.0
        for text, cls, cw in items:
            w, sep_w = len(text) * cw, (len(SEP) * 7.0 if cur else 0)
            if cur and cur_w + sep_w + w > VAL_W:
                lines.append(cur)
                cur, cur_w, sep_w = [], 0.0, 0
            if cur:
                cur.append((SEP, "sep"))
            cur.append((text, cls))
            cur_w += sep_w + w
        return lines + ([cur] if cur else [])

    body, y = [], PAD
    for i, (label, tools, concepts) in enumerate(SKILLS):
        lines = flow(tools, concepts)
        first = y + ROW_PAD + 15
        body.append(f'<text class="label" x="{PAD}" y="{first}">{escape(label)}</text>')
        for j, ln in enumerate(lines):
            spans = "".join(f'<tspan class="{c}">{escape(s)}</tspan>' for s, c in ln)
            body.append(f'<text x="{VAL_X}" y="{first + j * LH}">{spans}</text>')
        y += ROW_PAD * 2 + 15 + (len(lines) - 1) * LH + 6
        if i < len(SKILLS) - 1:
            body.append(f'<line x1="{PAD}" y1="{y}" x2="{W - PAD}" y2="{y}" {stroke("rule")}/>')
    return svg(W, y + PAD - ROW_PAD, "Skills", css, body)


# ---------------------------------------------------------------- journey
COMPANIES = [
    ("P", "PAYSTAR", "Rasht, Iran · On-site", [
        ("Software Engineer", "Nov 2025 – Present", True, "Full-time",
         ["Building and running production backend services: RESTful APIs, service integrations,",
          "deployment, server configuration, monitoring and production troubleshooting."]),
    ]),
    ("A", "AVINA IT SOLUTIONS", "Tehran, Iran · Remote", [
        ("Software Engineer", "Oct 2025 – Present", True, "Part-time",
         ["Backend features and service integrations across PHP/Laravel and Python/FastAPI projects,",
          "plus refactoring, deployment workflows and release management."]),
        ("Back-end Developer", "Feb 2025 – Oct 2025", False, "Full-time · 9 mos",
         ["RESTful APIs, authentication and authorization, business logic and third-party integrations;",
          "query optimization, debugging and refactoring through Git-based code reviews."]),
    ]),
    ("P", "PARDIS TECHNOLOGY PARK", "Tehran, Iran · Remote", [
        ("Quality Assurance Engineer", "Apr 2024 – Jan 2025", False, "Full-time · 10 mos",
         ["Functional, API, regression and automated testing of web applications with Cypress,",
          "plus reproducible bug reports and fix validation with developers."]),
        ("Software Engineer Intern", "Feb 2024 – Apr 2024", False, "Full-time · 3 mos",
         ["Backend development with PHP, Laravel and MySQL: REST APIs, database operations,",
          "application logic, authentication and bug fixing."]),
    ]),
]


def journey():
    NODE_X, NODE_R, CARD_X, CARD_R, PAD, CARD_H = 56, 22, 96, 868, 20, 120
    css = f""".initial {{ font-size: 18px; font-weight: 700; fill: {T["node_fg"]}; }}
    .company {{ font-size: 18px; font-weight: 700; fill: {T["title"]}; letter-spacing: .6px; }}
    .cmeta {{ font-size: 13px; font-weight: 400; fill: {T["muted"]}; letter-spacing: 0; }}
    .role {{ font-size: 16px; font-weight: 700; fill: {T["title"]}; }}
    .tag {{ font-size: 10.5px; font-weight: 700; fill: #FFFFFF; letter-spacing: 1px; }}
    .meta {{ font-size: 13px; fill: {T["muted"]}; }}
    .chip {{ font-size: 12px; font-weight: 600; fill: {T["chip_fg"]}; }}
    .desc {{ font-size: 14px; fill: {T["text"]}; }}"""
    body, nodes, y = [], [], 36
    for i, (initial, name, meta, roles) in enumerate(COMPANIES):
        cy = y + NODE_R
        nodes.append(cy)
        body += [f'<g class="fade d{i + 1}">',
                 f'<circle cx="{NODE_X}" cy="{cy}" r="{NODE_R}" fill="{T["node"]}"/>',
                 f'<text class="initial" x="{NODE_X}" y="{cy + 6.5}" text-anchor="middle">{initial}</text>',
                 f'<text class="company" x="{CARD_X}" y="{cy + 6}">{escape(name)}'
                 f'<tspan class="cmeta" dx="14">{escape(meta)}</tspan></text>']
        top = cy + 34
        for j, (title, dates, current, rmeta, desc) in enumerate(roles):
            left, right = CARD_X + PAD, CARD_R - PAD
            body.append(f'<rect x="{CARD_X}" y="{top}" width="{CARD_R - CARD_X}" height="{CARD_H}" rx="10" '
                        f'{fill("panel")} {stroke("border")}/>')
            body.append(f'<text class="role" x="{left}" y="{top + 32}">{escape(title)}</text>')
            dw = text_w(dates, 12) + 24
            body.append(pill(right - dw, top + 16, dw, 22, fill("chip_bg"), dates, "chip"))
            x = left
            if current:
                body.append(pill(x, top + 43, 72, 19, f'fill="{T["tag_bg"]}"', "CURRENT", "tag"))
                x += 82
            body.append(f'<text class="meta" x="{x}" y="{top + 57}">{escape(rmeta)}</text>')
            for k, line in enumerate(desc):
                body.append(f'<text class="desc" x="{left}" y="{top + 86 + k * 20}">{escape(line)}</text>')
            top += CARD_H + (12 if j < len(roles) - 1 else 0)
        body.append('</g>')
        y = top + 28
    # timeline segments between the company circles
    rail = [f'<line x1="{NODE_X}" y1="{a + NODE_R + 6}" x2="{NODE_X}" y2="{b - NODE_R - 6}" {stroke("rail", 3)}/>'
            for a, b in zip(nodes, nodes[1:])]
    return svg(900, y - 28 + 32, "Career timeline", css, rail + body)


# ---------------------------------------------------------------- how I work
PRINCIPLES = [
    ("01", "Production first", ["I deploy, monitor and troubleshoot what I ship,",
                                "and stay responsible for it after release."]),
    ("02", "Simple over clever", ["Readable, well-structured code built on SOLID",
                                  "principles, so the next change is a safe one."]),
    ("03", "Data done right", ["Careful schemas, sensible indexes and fast",
                               "queries are the base of every reliable service."]),
    ("04", "AI as a teammate", ["Claude Code and Codex speed up building and",
                                "debugging; I still review every change myself."]),
]


def how_i_work():
    css = f""".num {{ font-size: 28px; font-weight: 700; fill: {T["accent"]}; }}
    .title {{ font-size: 18px; font-weight: 700; fill: {T["title"]}; }}
    .desc {{ font-size: 14px; fill: {T["text"]}; }}"""
    body = [f'<line x1="40" y1="145" x2="860" y2="145" {stroke("rule", 2)}/>',
            f'<line x1="450" y1="40" x2="450" y2="250" {stroke("rule", 2)}/>']
    for i, (num, title, desc) in enumerate(PRINCIPLES):
        x, y = 40 + (i % 2) * 430, 70 + (i // 2) * 130
        body += [f'<g class="fade d{i + 1}">',
                 f'<text class="num" x="{x}" y="{y}">{num}</text>',
                 f'<text class="title" x="{x + 56}" y="{y - 6}">{escape(title)}</text>',
                 f'<text class="desc" x="{x + 56}" y="{y + 20}">{escape(desc[0])}</text>',
                 f'<text class="desc" x="{x + 56}" y="{y + 42}">{escape(desc[1])}</text>',
                 '</g>']
    return svg(900, 280, "How I work", css, body)


CARDS = {"about": about, "skills": skills, "journey": journey, "how-i-work": how_i_work}

if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent.parent / "assets"
    for name, build in CARDS.items():
        path = out_dir / f"{name}-glass.svg"
        path.write_text(build(), encoding="utf-8")
        print(path.name)
