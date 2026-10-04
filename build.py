#!/usr/bin/env python3
"""templates/ と code/ から、公開用の HTML（index.html, day1〜3.html）を生成する。

  templates/index.html, day1.html, day2.html, day3.html   各ページの本文
  code/                                                    {{FILE:ファイル名}} の部分に埋め込むソースコード

共通のヘッダー・ナビ・前後ページ送り・フッターはこのスクリプトで付与する。
使い方:  python3 build.py
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "地球と惑星のモデリング"
COURSE = "情報工学実験"

# ナビゲーション: (表示名, リンク先)
NAV = [
    ("概要", "index.html"),
    ("第1回", "day1.html"),
    ("第2回", "day2.html"),
    ("第3回", "day3.html"),
    ("レポート課題", "index.html#report"),
    ("付録・参考値", "index.html#reference"),
    ("参考図書", "index.html#books"),
]

# ページ定義
PAGES = [
    {
        "file": "index.html",
        "title": f"{SITE} | {COURSE}",
        "description": "情報工学科4年生向け「情報工学実験」全3回：地球と惑星のモデリング。C言語での数値シミュレーションとgnuplotによる可視化。",
    },
    {
        "file": "day1.html",
        "num": "第1回",
        "heading": "地球のエネルギー収支モデル",
        "description": "第1回: 放射平衡の考え方で惑星の平衡温度を計算し、太陽定数を振ってT–S曲線を描く。",
        "prev": ("全体の概要", "index.html", "実験の進め方・gnuplotのインストール"),
        "next": ("第2回", "day2.html", "Euler法とエネルギーバランスモデルの時間発展"),
    },
    {
        "file": "day2.html",
        "num": "第2回",
        "heading": "Euler法とエネルギーバランスモデルの時間発展",
        "description": "第2回: Euler法を確認し、放射収支モデルの時間発展と氷アルベドフィードバック（ヒステリシス）を調べる。",
        "prev": ("第1回", "day1.html", "地球のエネルギー収支モデル"),
        "next": ("第3回", "day3.html", "惑星の運動（重力多体問題）"),
    },
    {
        "file": "day3.html",
        "num": "第3回",
        "heading": "惑星の運動（重力多体問題）",
        "description": "第3回: 2体問題をEuler法で解き、リープ・フロッグ法に改造してエネルギー保存を比較する。発展としてN体シミュレーション。",
        "prev": ("第2回", "day2.html", "Euler法とエネルギーバランスモデルの時間発展"),
        "next": ("レポート課題", "index.html#report", "レポートのまとめ方"),
    },
]

LAYOUT = """<!doctype html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="vendor/katex/katex.min.css">
</head>
<body>

{hero}

{nav}

<div class="wrap">

{content}
{pager}
</div>

<footer>
  {site} &middot; {course}
</footer>

<script src="vendor/katex/katex.min.js"></script>
<script src="vendor/katex/auto-render.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {{
    renderMathInElement(document.body, {{
      delimiters: [
        {{ left: "$$", right: "$$", display: true }},
        {{ left: "$", right: "$", display: false }}
      ],
      throwOnError: false
    }});
  }});
</script>

</body>
</html>
"""

HERO_INDEX = """<header class="hero">
  <div class="kicker">情報工学実験 &middot; 全3回（各回1.5時間&times;2コマ）</div>
  <h1>地球と惑星のモデリング</h1>
  <p class="lead">
    地球のエネルギー収支モデルと、惑星の運動を支配する重力多体問題を題材に、
    微分方程式を数値的に解くアルゴリズムをC言語で実装し、gnuplotで可視化します。
  </p>
  <div class="meta-badges">
    <span>対象: 情報工学科4年生</span>
  </div>
</header>"""

HERO_DAY = """<header class="hero hero-sm">
  <div class="kicker">{course} &middot; {site}</div>
  <span class="day-badge">{num}</span>
  <h1>{heading}</h1>
</header>"""


def make_nav(current_file):
    items = []
    for label, href in NAV:
        cur = ' aria-current="page"' if href == current_file else ""
        items.append(f'    <li><a href="{href}"{cur}>{label}</a></li>')
    return '<nav class="toc">\n  <ul>\n' + "\n".join(items) + "\n  </ul>\n</nav>"


def make_pager(page):
    if "prev" not in page and "next" not in page:
        return ""
    parts = ['<div class="pager">']
    if "prev" in page:
        label, href, sub = page["prev"]
        parts.append(
            f'  <a class="prev" href="{href}"><span class="pager-label">&larr; 前へ</span>{label}：{sub}</a>'
        )
    else:
        parts.append('  <span class="pager-spacer"></span>')
    if "next" in page:
        label, href, sub = page["next"]
        parts.append(
            f'  <a class="next" href="{href}"><span class="pager-label">次へ &rarr;</span>{label}：{sub}</a>'
        )
    else:
        parts.append('  <span class="pager-spacer"></span>')
    parts.append("</div>")
    return "\n".join(parts)


FILE_RE = re.compile(r"\{\{FILE:([^}]+)\}\}")


def embed_code(body):
    def repl(m):
        path = ROOT / "code" / m.group(1)
        if not path.exists():
            sys.exit(f"MISSING code file: {m.group(1)}")
        return html.escape(path.read_text(encoding="utf-8"))

    return FILE_RE.sub(repl, body)


def main():
    for page in PAGES:
        body = (ROOT / "templates" / page["file"]).read_text(encoding="utf-8")
        body = embed_code(body)
        if "num" in page:
            title = f'{page["num"]} {page["heading"]} | {SITE}'
            hero = HERO_DAY.format(course=COURSE, site=SITE, num=page["num"], heading=page["heading"])
        else:
            title = page["title"]
            hero = HERO_INDEX
        out = LAYOUT.format(
            title=title,
            description=page["description"],
            hero=hero,
            nav=make_nav(page["file"]),
            content=body.rstrip(),
            pager=make_pager(page),
            site=SITE,
            course=COURSE,
        )
        leftover = re.findall(r"\{\{[A-Z]+:[^}]*\}\}", out)
        if leftover:
            sys.exit(f'{page["file"]}: unresolved placeholders {leftover}')
        (ROOT / page["file"]).write_text(out, encoding="utf-8")
        print(f'wrote {page["file"]} ({len(out):,} chars)')


if __name__ == "__main__":
    main()
