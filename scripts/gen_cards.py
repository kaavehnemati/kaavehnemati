"""Generate the profile README section cards in a transparent "glass" style.

Writes assets/<card>-<VERSION>.svg for: about, skills, journey, how-i-work.
The SVGs have no background: text uses mid-tone colors that read on both
GitHub's light (#ffffff) and dark (#0d1117) pages, and panels are a faint
translucent gray ("glass"), so no theme switching is needed.

Usage: python3 scripts/gen_cards.py
After changing content, set VERSION to a never-used value and update the
file names in the README: raw.githubusercontent.com caches images.
"""
from pathlib import Path
from xml.sax.saxutils import escape

VERSION = "clear"

TITLE = "#4F74BA"     # names, titles, bold tools   (~4.5:1 on white, ~4.1:1 on dark)
TEXT = "#768191"      # body text                   (~4.1:1 / ~4.6:1)
MUTED = "#8B95A5"     # small meta text
ACCENT = "#B07152"    # labels, numbers, bullets    (~3.9:1 / ~4.9:1)
GLASS = "#8B95A5"     # panel tint and lines
NODE = "#22468A"
TAG = "#B07152"
HL_FROM, HL_TO = "#B07152", "#4A6FB5"

W = 900
FONT = "'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
FADE = """.fade { animation: fade .8s ease-out both; }
    .d2 { animation-delay: .15s; } .d3 { animation-delay: .3s; } .d4 { animation-delay: .45s; }
    @keyframes fade { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: none; } }
    @media (prefers-reduced-motion: reduce) { .fade { animation: none; } }"""


def svg(h, label, css, body):
    defs = (f'<defs><linearGradient id="hl" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{HL_FROM}"/><stop offset="1" stop-color="{HL_TO}"/>'
            f'</linearGradient></defs>')
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{label}">',
        f"  <style>\n    text {{ font-family: {FONT}; }}\n    {css}\n    {FADE}\n  </style>",
        f"  {defs}",
        *("  " + ln for ln in body),
        "</svg>",
    ]) + "\n"


def glass(x, y, w, h, rx=10):
    """Frosted panel: faint gray tint, soft border, tan-to-cobalt highlight on the top edge."""
    return [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{GLASS}" fill-opacity=".08" '
            f'stroke="{GLASS}" stroke-opacity=".35"/>',
            f'<rect x="{x + rx + 4}" y="{y}" width="{w - 2 * rx - 8}" height="2" rx="1" fill="url(#hl)" opacity=".85"/>']


def text_w(s, px):
    return len(s) * px * 0.6


def pill(x, y, w, h, paint, label, cls):
    return (f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="{h / 2}" {paint}/>'
            f'<text class="{cls}" x="{x + w / 2:.1f}" y="{y + h / 2 + 4.2:.1f}" text-anchor="middle">{escape(label)}</text>')


# ---------------------------------------------------------------- about
def about():
    css = f""".sum {{ font-size: 15px; fill: {TEXT}; }}
    .b {{ font-weight: 700; fill: {TITLE}; }}
    .label {{ font-size: 11px; font-weight: 700; fill: {ACCENT}; letter-spacing: 1.5px; }}
    .name {{ font-size: 15px; font-weight: 700; fill: {TITLE}; letter-spacing: .4px; }}
    .meta {{ font-size: 13.5px; fill: {MUTED}; }}
    .item {{ font-size: 15px; fill: {TEXT}; }}"""
    focus = ["Reliable, maintainable backend services and clean API design",
             "Service integrations, authentication and authorization",
             "Database design, data modeling and query performance",
             "Stable releases, production environments and troubleshooting",
             "AI-assisted engineering with Claude Code and OpenAI Codex"]
    body = [
        '<g class="fade">',
        '<text class="sum" x="4" y="22">Software Engineer with hands-on experience designing, building, deploying and maintaining production</text>',
        '<text class="sum" x="4" y="46">backend systems. I work across <tspan class="b">PHP/Laravel</tspan> and <tspan class="b">Python/FastAPI</tspan> with '
        '<tspan class="b">PostgreSQL</tspan> and <tspan class="b">MySQL</tspan>, owning</text>',
        '<text class="sum" x="4" y="70">features end to end, from API design and data modeling to deployment, monitoring and troubleshooting.</text>',
        '</g>',
        '<g class="fade d2">', *glass(4, 96, 340, 218),
        '<text class="label" x="24" y="126">CURRENTLY</text>',
        '<text class="name" x="24" y="152">PAYSTAR</text>',
        '<text class="meta" x="24" y="171">Software Engineer · Full-time</text>',
        '<text class="name" x="24" y="198">AVINA IT SOLUTIONS</text>',
        '<text class="meta" x="24" y="217">Software Engineer · Part-time</text>',
        '<text class="label" x="24" y="250">EDUCATION</text>',
        '<text class="name" x="24" y="276">B.Sc. Computer Engineering</text>',
        '<text class="meta" x="24" y="295">University of Guilan · 2020–2024</text>',
        '</g>',
        '<g class="fade d3">', *glass(356, 96, 540, 218),
        '<text class="label" x="376" y="126">FOCUS AREAS</text>',
    ]
    for i, item in enumerate(focus):
        y = 156 + i * 32
        body += [f'<circle cx="381" cy="{y - 5}" r="3.5" fill="{ACCENT}"/>',
                 f'<text class="item" x="394" y="{y}">{escape(item)}</text>']
    body.append('</g>')
    return svg(318, "About", css, body)


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
    PX, LABEL_X, VAL_X, RIGHT, LH, ROW_PAD, SEP = 4, 28, 210, 872, 23, 14, " · "
    VAL_W = RIGHT - VAL_X
    css = f"""text {{ font-size: 15px; }}
    .label {{ font-size: 12px; font-weight: 700; fill: {ACCENT}; letter-spacing: 1.4px; }}
    .tool {{ font-weight: 700; fill: {TITLE}; }}
    .con {{ fill: {TEXT}; }}
    .sep {{ fill: {MUTED}; }}"""

    def flow(tools, concepts):
        items = [(x, "tool", 8.6) for x in tools] + [(x, "con", 7.5) for x in concepts]
        lines, cur, cur_w = [], [], 0.0
        for text, cls, cw in items:
            w, sep_w = len(text) * cw, (len(SEP) * 7.5 if cur else 0)
            if cur and cur_w + sep_w + w > VAL_W:
                lines.append(cur)
                cur, cur_w, sep_w = [], 0.0, 0
            if cur:
                cur.append((SEP, "sep"))
            cur.append((text, cls))
            cur_w += sep_w + w
        return lines + ([cur] if cur else [])

    rows, y = [], 20
    for i, (label, tools, concepts) in enumerate(SKILLS):
        lines = flow(tools, concepts)
        first = y + ROW_PAD + 15
        rows.append(f'<text class="label" x="{LABEL_X}" y="{first}">{escape(label)}</text>')
        for j, ln in enumerate(lines):
            spans = "".join(f'<tspan class="{c}">{escape(s)}</tspan>' for s, c in ln)
            rows.append(f'<text x="{VAL_X}" y="{first + j * LH}">{spans}</text>')
        y += ROW_PAD * 2 + 15 + (len(lines) - 1) * LH + 6
        if i < len(SKILLS) - 1:
            rows.append(f'<line x1="{LABEL_X}" y1="{y}" x2="{RIGHT}" y2="{y}" stroke="{GLASS}" stroke-opacity=".4"/>')
    panel_h = y + 6
    body = ['<g class="fade">', *glass(PX, 4, W - 2 * PX, panel_h), *rows, '</g>']
    return svg(panel_h + 8, "Skills", css, body)


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
    NODE_X, NODE_R, CARD_X, CARD_R, PAD, CARD_H = 24, 20, 62, 896, 20, 124
    css = f""".initial {{ font-size: 17px; font-weight: 700; fill: #FFFFFF; }}
    .company {{ font-size: 18px; font-weight: 700; fill: {TITLE}; letter-spacing: .6px; }}
    .cmeta {{ font-size: 13.5px; font-weight: 400; fill: {MUTED}; letter-spacing: 0; }}
    .role {{ font-size: 16px; font-weight: 700; fill: {TITLE}; }}
    .tag {{ font-size: 10.5px; font-weight: 700; fill: #FFFFFF; letter-spacing: 1px; }}
    .meta {{ font-size: 13.5px; fill: {MUTED}; }}
    .chip {{ font-size: 12px; font-weight: 600; fill: {TITLE}; }}
    .desc {{ font-size: 15px; fill: {TEXT}; }}"""
    body, nodes, y = [], [], 4
    for i, (initial, name, meta, roles) in enumerate(COMPANIES):
        cy = y + NODE_R
        nodes.append(cy)
        body += [f'<g class="fade d{i + 1}">',
                 f'<circle cx="{NODE_X}" cy="{cy}" r="{NODE_R}" fill="{NODE}"/>',
                 f'<text class="initial" x="{NODE_X}" y="{cy + 6}" text-anchor="middle">{initial}</text>',
                 f'<text class="company" x="{CARD_X}" y="{cy + 6}">{escape(name)}'
                 f'<tspan class="cmeta" dx="14">{escape(meta)}</tspan></text>']
        top = cy + 34
        for j, (title, dates, current, rmeta, desc) in enumerate(roles):
            left, right = CARD_X + PAD, CARD_R - PAD
            body += glass(CARD_X, top, CARD_R - CARD_X, CARD_H)
            body.append(f'<text class="role" x="{left}" y="{top + 34}">{escape(title)}</text>')
            dw = text_w(dates, 12) + 24
            body.append(pill(right - dw, top + 18, dw, 22, 'fill="#4A6FB5" fill-opacity=".15"', dates, "chip"))
            x = left
            if current:
                body.append(pill(x, top + 45, 72, 19, f'fill="{TAG}"', "CURRENT", "tag"))
                x += 82
            body.append(f'<text class="meta" x="{x}" y="{top + 59}">{escape(rmeta)}</text>')
            for k, line in enumerate(desc):
                body.append(f'<text class="desc" x="{left}" y="{top + 88 + k * 21}">{escape(line)}</text>')
            top += CARD_H + (12 if j < len(roles) - 1 else 0)
        body.append('</g>')
        y = top + 26
    rail = [f'<line x1="{NODE_X}" y1="{a + NODE_R + 6}" x2="{NODE_X}" y2="{b - NODE_R - 6}" '
            f'stroke="{GLASS}" stroke-opacity=".5" stroke-width="3"/>'
            for a, b in zip(nodes, nodes[1:])]
    return svg(y - 26 + 6, "Career timeline", css, rail + body)


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
    TW, TH, GAP = 438, 118, 16
    css = f""".num {{ font-size: 28px; font-weight: 700; fill: {ACCENT}; }}
    .title {{ font-size: 18px; font-weight: 700; fill: {TITLE}; }}
    .desc {{ font-size: 14.5px; fill: {TEXT}; }}"""
    body = []
    for i, (num, title, desc) in enumerate(PRINCIPLES):
        x, y = 4 + (i % 2) * (TW + GAP), 4 + (i // 2) * (TH + GAP)
        body += [f'<g class="fade d{i + 1}">', *glass(x, y, TW, TH),
                 f'<text class="num" x="{x + 20}" y="{y + 48}">{num}</text>',
                 f'<text class="title" x="{x + 72}" y="{y + 40}">{escape(title)}</text>',
                 f'<text class="desc" x="{x + 72}" y="{y + 66}">{escape(desc[0])}</text>',
                 f'<text class="desc" x="{x + 72}" y="{y + 88}">{escape(desc[1])}</text>',
                 '</g>']
    return svg(4 + 2 * TH + GAP + 4, "How I work", css, body)


CARDS = {"about": about, "skills": skills, "journey": journey, "how-i-work": how_i_work}

if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent.parent / "assets"
    for name, build in CARDS.items():
        path = out_dir / f"{name}-{VERSION}.svg"
        path.write_text(build(), encoding="utf-8")
        print(path.name)
