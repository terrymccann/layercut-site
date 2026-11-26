#!/usr/bin/env python3
"""Build layercut.app into dist/: shared header and footer, Markdown docs and legal pages.

    python3 build.py          # writes dist/
Deploy dist/ to Cloudflare Pages (see README.md).
"""
import datetime, html, pathlib, re, shutil
import markdown

ROOT = pathlib.Path(__file__).parent
SRC, DIST = ROOT / "src", ROOT / "dist"
SITE = "https://layercut.app"
TODAY = datetime.date.today()

# docs order: (slug, sidebar title, group)
DOCS = [
    ("", "Overview", "Start here"),
    ("getting-started", "Install and first cut", "Start here"),
    ("the-window", "The LayerCut window", "Start here"),
    ("materials", "Materials", "Set up"),
    ("fit-test", "The fit test", "Set up"),
    ("model-and-scale", "Model, size and slicing", "Set up"),
    ("stacked", "Stacked", "Build modes"),
    ("interlocking", "Interlocking: grid", "Build modes"),
    ("radial", "Interlocking: radial", "Build modes"),
    ("panels", "Panels", "Build modes"),
    ("living-hinges", "Living hinges", "Build modes"),
    ("sheets-and-nesting", "Sheets and nesting", "Cut and build"),
    ("exporting", "Export and LightBurn", "Cut and build"),
    ("assembly", "Assembling your piece", "Cut and build"),
    ("warnings", "Warnings and notes", "Reference"),
    ("shortcuts", "Keyboard shortcuts", "Reference"),
    ("command-line", "Command-line tool", "Reference"),
    ("editions", "Free and Pro", "Reference"),
    ("troubleshooting", "Troubleshooting", "Reference"),
]

LEGAL = ["terms", "privacy", "refunds", "license"]


def head(title, desc, path, extra=""):
    canon = SITE + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#1a2026">
<meta property="og:type" content="website">
<meta property="og:site_name" content="LayerCut">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/archivo-latin-standard-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={CSS_V}">
<script>
  document.documentElement.classList.add("js");
  try {{ var t = localStorage.getItem("lc-site-theme"); if (t === "light" || t === "dark") document.documentElement.dataset.theme = t; }} catch (e) {{}}
</script>
<script src="/assets/site.js?v={JS_V}" defer></script>
{extra}</head>
"""


def header(active):
    def item(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/"><img src="/img/icon-96.png" alt="" width="28" height="28">LayerCut</a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      {item("/#modes", "Features", "features")}
      {item("/docs/", "Docs", "docs")}
      {item("/#pricing", "Pricing", "pricing")}
      {item("/roadmap/", "Roadmap", "roadmap")}
      <a class="btn" href="/#download">Download</a>
    </nav>
  </div>
</header>
"""


FOOTER = f"""<footer class="site-foot">
  <div class="wrap">
    <div class="about">
      <a class="brand" href="/"><img src="/img/icon-96.png" alt="" width="28" height="28">LayerCut</a>
      <p style="margin-top:12px;max-width:30em">Turns 3D models into laser-cut parts and exports LightBurn and SVG files. Works offline on macOS and Windows.</p>
    </div>
    <div>
      <h4>Product</h4>
      <ul>
        <li><a href="/#modes">Features</a></li>
        <li><a href="/#pricing">Pricing</a></li>
        <li><a href="/roadmap/">Roadmap</a></li>
        <li><a href="/#download">Download</a></li>
        <li><a href="/docs/editions/">Free and Pro</a></li>
      </ul>
    </div>
    <div>
      <h4>Help</h4>
      <ul>
        <li><a href="/docs/">Documentation</a></li>
        <li><a href="/docs/getting-started/">Install and first cut</a></li>
        <li><a href="/docs/troubleshooting/">Troubleshooting</a></li>
        <li><a href="mailto:hello@layercut.app">hello@layercut.app</a></li>
      </ul>
    </div>
    <div>
      <h4>Legal</h4>
      <ul>
        <li><a href="/terms/">Terms</a></li>
        <li><a href="/privacy/">Privacy</a></li>
        <li><a href="/refunds/">Refunds</a></li>
        <li><a href="/license/">License keys</a></li>
      </ul>
    </div>
    <div class="fine">
      <span>© {TODAY.year} LayerCut. LightBurn is a trademark of LightBurn Software, LLC; LayerCut is not affiliated with it.</span>
      <button class="theme-switch" type="button">Theme: System</button>
    </div>
  </div>
</footer>
</body>
</html>
"""


def md(text):
    return markdown.markdown(text, extensions=["tables", "attr_list", "md_in_html", "toc", "sane_lists"],
                             extension_configs={"toc": {"permalink": False}})


def front(text):
    """Split '---' front matter (key: value lines) from Markdown."""
    meta = {}
    if text.startswith("---"):
        _, fm, text = text.split("---", 2)
        for line in fm.strip().splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    return meta, text.strip()


def write(path, content):
    out = DIST / path.strip("/") / "index.html" if not path.endswith(".html") else DIST / path.strip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content)


def docs_nav(current):
    out, group = [], None
    for slug, title, g in DOCS:
        if g != group:
            if group is not None:
                out.append("</ul>")
            out.append(f"<h2>{g}</h2><ul>")
            group = g
        cur = ' aria-current="page"' if slug == current else ""
        href = f"/docs/{slug + '/' if slug else ''}"
        out.append(f'<li><a href="{href}"{cur}>{title}</a></li>')
    out.append("</ul>")
    return "\n".join(out)


def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for d in ["assets", "img"]:
        shutil.copytree(ROOT / d, DIST / d)
    for f in ["_headers", "_redirects", "robots.txt"]:
        if (SRC / f).exists():
            shutil.copy(SRC / f, DIST / f)

    pages = ["/"]
    # home
    home = (SRC / "home.html").read_text()
    hero_svg = (SRC / "hero-sheet.svg").read_text()
    home = home.replace("<!--HERO_SHEET-->", hero_svg).replace("<!--HINGE_SHEET-->", (SRC / "hinge-sheet.svg").read_text())
    write("/", head("LayerCut — turn 3D models into laser-cut parts",
                    "LayerCut slices STL and OBJ models into stacked layers, interlocking slices or flat-panel boxes with living hinges, nests them on your sheet and exports LightBurn and SVG files.",
                    "/") + header("home") + home + FOOTER)

    # docs
    for i, (slug, title, group) in enumerate(DOCS):
        meta, body = front((SRC / "docs" / f"{slug or 'index'}.md").read_text())
        prev_ = DOCS[i - 1] if i > 0 else None
        next_ = DOCS[i + 1] if i + 1 < len(DOCS) else None
        pager = '<nav class="pager" aria-label="Pages">'
        if prev_:
            pager += f'<a class="prev" href="/docs/{prev_[0] + "/" if prev_[0] else ""}"><span>Previous</span>{prev_[1]}</a>'
        if next_:
            pager += f'<a class="next" href="/docs/{next_[0]}/"><span>Next</span>{next_[1]}</a>'
        pager += "</nav>"
        h1 = meta.get("title", title)
        intro = f'<p class="intro">{meta["intro"]}</p>' if meta.get("intro") else ""
        path = f"/docs/{slug + '/' if slug else ''}"
        page = (head(f"{h1} — LayerCut docs", meta.get("description", meta.get("intro", h1)), path)
                + header("docs")
                + f"""<main id="main" class="wrap docs-layout">
  <div>
    <button class="docs-nav-toggle" aria-expanded="false" aria-controls="docs-nav">Docs menu<span aria-hidden="true">▾</span></button>
    <nav class="docs-nav" id="docs-nav" aria-label="Documentation">{docs_nav(slug)}</nav>
  </div>
  <article class="prose">
    <h1>{h1}</h1>
    {intro}
    {md(body)}
    {pager}
  </article>
</main>
""" + FOOTER)
        write(path, page)
        pages.append(path)

    # legal
    for slug in LEGAL:
        meta, body = front((SRC / "legal" / f"{slug}.md").read_text())
        path = f"/{slug}/"
        page = (head(f"{meta['title']} — LayerCut", meta.get("description", meta["title"]), path)
                + header("") + f"""<main id="main" class="wrap page-legal"><article class="prose">
<h1>{meta['title']}</h1>
{md(body)}
<p class="updated">Last updated {meta.get('updated', TODAY.isoformat())}.</p>
</article></main>
""" + FOOTER)
        write(path, page)
        pages.append(path)

    # roadmap
    meta, body = front((SRC / "roadmap.md").read_text())
    page = (head("Roadmap — LayerCut", meta["description"], "/roadmap/")
            + header("roadmap") + f"""<main id="main" class="wrap page-legal page-roadmap"><article class="prose">
<h1>{meta['title']}</h1>
<p class="intro">{meta['intro']}</p>
{md(body)}
<p class="updated">Last updated {meta.get('updated', TODAY.isoformat())}.</p>
</article></main>
""" + FOOTER)
    write("/roadmap/", page)
    pages.append("/roadmap/")

    # 404
    (DIST / "404.html").write_text(head("Page not found — LayerCut", "Page not found", "/404") + header("") +
        """<main id="main" class="wrap page-legal"><article class="prose">
<h1>That page isn't here</h1>
<p class="intro">The link may be old, or the page may have moved.</p>
<p><a href="/">Go to the home page</a> or <a href="/docs/">browse the documentation</a>.</p>
</article></main>
""" + FOOTER)

    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"<url><loc>{SITE}{p}</loc><lastmod>{TODAY.isoformat()}</lastmod></url>" for p in pages]
    sm.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(sm))
    print(f"built {len(pages)} pages into {DIST}")


import hashlib
VERSION = TODAY.strftime("%Y%m%d")
# content hashes, so a browser never keeps a stale stylesheet or script after a deploy
CSS_V = hashlib.sha1((ROOT / "assets/site.css").read_bytes()).hexdigest()[:10]
JS_V = hashlib.sha1((ROOT / "assets/site.js").read_bytes()).hexdigest()[:10]
if __name__ == "__main__":
    build()
