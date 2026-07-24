#!/usr/bin/env python3
"""Generate static/GeraldRichResume.pdf.

Self-hosting: extracts the AvenirNext/Hack font subsets from the existing
static/GeraldRichResume.pdf (original or previously rebuilt — both carry the
same embedded subsets), downloads full Space Mono Italic once (cached beside
this script, gitignored), rebuilds the page, and fixes BaseFont metadata.

Requires: pip install pymupdf pikepdf
Run:      python3 etc/resume-builder/build_resume.py

Glyph constraint: the extracted subsets only contain characters used in the
original document. The script audits every string and fails loudly with the
missing characters if you add text the subsets can't render (notably: no
capital L in body text). Fix by rewording, or replace the subset extraction
with full licensed AvenirNext font files placed beside this script.
"""
import io, os, sys, urllib.request
from pathlib import Path

import fitz
import pikepdf

SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parent.parent
PDF_PATH = REPO / 'static' / 'GeraldRichResume.pdf'
MONO_PATH = SCRIPT_DIR / 'SpaceMono-Italic.ttf'
MONO_URL = 'https://raw.githubusercontent.com/googlefonts/spacemono/main/fonts/ttf/SpaceMono-Italic.ttf'

# ---- Bootstrap fonts ----
src = fitz.open(PDF_PATH)
FONT_BUFS = {}
for f in src[0].get_fonts():
    for key, tag in [('demibold', 'AvenirNext-DemiBold'), ('medium', 'AvenirNext-Medium'),
                     ('regular', 'AvenirNext-Regular'), ('hack', 'Hack-Regular')]:
        if tag in f[3]:
            FONT_BUFS[key] = src.extract_font(f[0])[3]
src.close()
missing_fonts = {'demibold', 'medium', 'regular', 'hack'} - set(FONT_BUFS)
if missing_fonts:
    sys.exit(f'Could not extract fonts {missing_fonts} from {PDF_PATH}')

if not MONO_PATH.exists():
    print('Downloading Space Mono Italic...')
    urllib.request.urlretrieve(MONO_URL, MONO_PATH)
FONT_BUFS['mono'] = MONO_PATH.read_bytes()

fonts = {k: fitz.Font(fontbuffer=v) for k, v in FONT_BUFS.items()}

TEAL = (0x44/255, 0x94/255, 0x8f/255)
OLIVE = (0x59/255, 0x4b/255, 0x3b/255)
GRAY = (0x5b/255, 0x58/255, 0x54/255)
BLACK = (0, 0, 0)
TAN = (0.788, 0.764, 0.731)

def audit(fkey, s):
    missing = [c for c in set(s) if fonts[fkey].has_glyph(ord(c)) == 0]
    if missing:
        sys.exit(f'MISSING GLYPHS {missing} in {fkey} for: {s!r}')

def W(fkey, s, size):
    return fonts[fkey].text_length(s, size)

doc = fitz.open()
page = doc.new_page(width=612, height=792)
inserted = set()

def put(x, y, segs, size):
    cx = x
    for text, fkey, color, url in segs:
        audit(fkey, text)
        if fkey not in inserted:
            page.insert_font(fontname=f'f_{fkey}', fontbuffer=FONT_BUFS[fkey])
            inserted.add(fkey)
        page.insert_text((cx, y), text, fontname=f'f_{fkey}', fontsize=size, color=color)
        w = W(fkey, text, size)
        if url:
            if color == TEAL:
                page.draw_line((cx, y+1.46), (cx+w, y+1.46), color=TEAL, width=0.5)
            page.insert_link({'kind': fitz.LINK_URI, 'from': fitz.Rect(cx, y-10.7, cx+w, y+3), 'uri': url})
        cx += w
    return cx

# ---- Header ----
name = 'GERALD RICH'
put((612-W('medium', name, 20))/2, 34.6, [(name, 'medium', OLIVE, None)], 20)
page.draw_line((90, 42.9), (540, 42.9), color=TAN, width=2.0)
contact = [('S', 9), ('AN ', 7.2), ('F', 9), ('RANCISCO', 7.2), (', CA  |  (713) 516-5935  |  ', 9)]
total_w = sum(W('medium', t, s) for t, s in contact) + W('hack', 'https://geraldri.ch/', 9)
cx = (612-total_w)/2
for t, size in contact:
    cx = put(cx, 58.3, [(t, 'medium', OLIVE, None)], size)
put(cx, 58.3, [('https://geraldri.ch/', 'hack', TEAL, 'https://geraldri.ch/')], 9)

y = 82.3
LOC_DY, SKL_DY, B1_DY, B_DY, GAP, EDU_DY = 12.0, 12.0, 15.2, 14.0, 19.0, 14.0

def section(title, first_dy=22.0):
    global y
    put(90, y, [(title+' ', 'demibold', BLACK, None)], 10)
    page.draw_line((90, y+1.46), (90+W('demibold', title, 10), y+1.46), color=BLACK, width=0.5)
    y += first_dy

def entry(title_segs, loc, skills=None, bullets=None):
    global y
    put(90, y, title_segs, 10)
    y += LOC_DY
    put(90, y, [(loc, 'medium', OLIVE, None)], 9)
    if skills:
        y += SKL_DY
        put(90, y, [(skills, 'mono', GRAY, None)], 8)
    if bullets:
        y += B1_DY
        for i, b in enumerate(bullets):
            if i: y += B_DY
            put(104.4, y, [('-', 'regular', OLIVE, None)], 10)
            put(122.4, y, b, 10)
    y += GAP

def edu(main_segs, year):
    global y
    endx = put(90, y, main_segs, 10)
    put(endx, y, [(year, 'regular', GRAY, None)], 8)
    y += EDU_DY

section('EXPERIENCE')
entry([('SOFTWARE DEVELOPER / ENGINEER, ', 'medium', BLACK, None),
       ('BIG LOCAL NEWS', 'medium', TEAL, 'https://biglocalnews.org/'),
       (' AT STANFORD ', 'medium', BLACK, None)],
      'SAN FRANCISCO, CA \u2014 JUN. 2024 TO PRESENT ',
      'SKILLS: PYTHON, DATA PIPELINES, GCP, ELASTICSEARCH, NLP, LLM AGENTS ',
      [[('Develop ', 'regular', BLACK, None), ('DataTalk', 'regular', TEAL, 'https://www.datatalk.genie.stanford.edu/'), (', an AI agent answering campaign-finance questions with verified data ', 'regular', BLACK, None)],
       [('Helped build the ', 'regular', BLACK, None), ('Police Records Access Project', 'regular', TEAL, 'https://biglocalnews.org/content/news/2025/08/04/police-records.html'), (': 1.5 million pages of police records ', 'regular', BLACK, None)],
       [('Engineer ', 'regular', BLACK, None), ('AgendaWatch', 'regular', TEAL, 'https://agendawatch.org/'), (', harvesting local government agendas daily to alert reporters ', 'regular', BLACK, None)]])
entry([("MENTOR, COLUMBIA JOURNALISM SCHOOL'S ", 'medium', BLACK, None),
       ('LEDE PROGRAM', 'medium', TEAL, 'https://ledeprogram.com/'), (' ', 'medium', BLACK, None)],
      'NEW YORK, NY \u2014 JUN. 2024 TO AUG. 2024 ',
      'SKILLS: EDUCATION, EDITING, TECHNICAL CONSULTING ',
      [[('Met with graduate students weekly to review projects and give feedback ', 'regular', BLACK, None)],
       [('Advised on quick, two-week projects\u2019 scope while encouraging growth beyond lessons ', 'regular', BLACK, None)]])
entry([('INTERACTIVE NEWS EDITOR, ', 'medium', BLACK, None),
       ('THE ASSOCIATED PRESS', 'medium', TEAL, 'https://projects.apnews.com/'), (' ', 'medium', BLACK, None)],
      'SAN FRANCISCO, CA | NEW YORK, NY \u2014 SEPT. 2022 TO FEB. 2024 ',
      'SKILLS: CODE & STORY EDITING, TECHNICAL STRATEGY, SCRUM, CORE WEB VITALS, DESIGN SYSTEMS ',
      [[('Coordinated with customers globally to deliver timely, accurate election visualizations ', 'regular', BLACK, None)],
       [('Managed a team of nearly a dozen: devs, designers, project managers, QA, contractors ', 'regular', BLACK, None)],
       [('Implemented Agile & doubled the monthly output of custom feature pages ', 'regular', BLACK, None)]])
entry([('SENIOR SOFTWARE ENGINEER (READER EXPERIENCE), THE ATLANTIC ', 'medium', BLACK, None)],
      'NEW YORK, NY \u2014 NOV. 2019 TO SEPT. 2022 ',
      'SKILLS: TYPESCRIPT, CANVAS, NEXT.JS, SVELTE, GRAPHQL, DJANGO, SEO, NEXT-GEN IMAGES & VIDEO ',
      [[('Migrated sections and article pages to React with an emphasis on embeds and media ', 'regular', BLACK, None)],
       [('Contributed to continuous integration GitHub Actions pipelines and tests for code quality ', 'regular', BLACK, None)],
       [('Specialized in web presentations for ', 'regular', BLACK, None),
        ('award-winning', 'regular', TEAL, 'https://www.theatlantic.com/magazine/archive/2022/09/trump-administration-family-separation-policy-immigration/670604/'),
        (' ', 'regular', BLACK, None),
        ('features', 'regular', TEAL, 'https://www.theatlantic.com/podcasts/floodlines/'),
        (' and ', 'regular', BLACK, None),
        ('series', 'regular', TEAL, 'https://www.theatlantic.com/shadowland/'), (' ', 'regular', BLACK, None)]])
entry([('SENIOR DEVELOPER (NEWS PRODUCTS), ', 'medium', BLACK, None),
       ('AXIOS', 'medium', TEAL, 'https://www.axios.com/results?q=%22gerald%20rich%22&sort=1'), (' ', 'medium', BLACK, None)],
      'NEW YORK, NY \u2014 JAN. 2017 TO OCT. 2019 ',
      'SKILLS: REACT, NEXT.JS, JEST, GRAPHQL, DJANGO REST, AWS LAMBDA, JENKINS, AI2HTML ',
      [[('Engineered templates, APIs, and tests for interactives in the custom CMS, site & newsletters ', 'regular', BLACK, None)],
       [('Built an election graphics framework and tools for live graphics on the web & Apple News ', 'regular', BLACK, None)],
       [('Engineered a stock chart maker for breaking news graphics ', 'regular', BLACK, None)]])
entry([('CO-FOUNDER / TECHNICAL LEAD, ', 'medium', BLACK, None),
       ('DATAPROOFER', 'medium', TEAL, 'https://github.com/dataproofer/Dataproofer'), (' ', 'medium', BLACK, None)],
      'NEW YORK, NY | SAN FRANCISCO, CA \u2014 OCT. 2015 TO PRESENT ',
      'SKILLS: WEBPACK, ELECTRON, OPEN-SOURCE MANAGEMENT ',
      [[('Authored a command line interface and desktop app for detecting errors in spreadsheets ', 'regular', BLACK, None)],
       [('Published an open library of statistical and geographic tests for outliers ', 'regular', BLACK, None)]])
entry([('INTERACTIVE PRODUCER, VOCATIV  ', 'medium', BLACK, None)],
      'NEW YORK, NY | SAN FRANCISCO, CA \u2014 JUN. 2015 TO NOV. 2016 ')
entry([('INTERACTIVE REPORTER, ', 'medium', BLACK, None),
       ('THE MARSHALL PROJECT', 'medium', BLACK, 'https://www.themarshallproject.org/search?q=%22gerald+rich%22'),
       ('  ', 'medium', BLACK, None)],
      'NEW YORK, NY \u2014 SEPT. 2014 TO MAY 2015 ')
entry([('WEB PRODUCER, PROPUBLICA  ', 'medium', BLACK, None)],
      'NEW YORK, NY \u2014 FEB. 2014 TO SEPT. 2014 ')

y += 3.0
section('EDUCATION & AWARDS', first_dy=21.0)
edu([('Webby Award, Best Individual Editorial Feature, ', 'regular', BLACK, None),
     ('\u201cAdrift\u201d', 'regular', TEAL, 'https://projects.apnews.com/features/2023/adrift/index.html'),
     (' ', 'regular', BLACK, None)], '2024')
edu([('General Assembly, Product Management ', 'regular', BLACK, None)], '2018')
edu([('Knight Foundation Prototype fund, Dataproofer ', 'regular', BLACK, None)], '2015')
edu([('The University of Texas at Austin, B.A. in Economics ', 'regular', BLACK, None)], '2008 TO 2012')

final = y - EDU_DY
assert final < 780, f'Page overflow: final baseline {final}'
tmp = io.BytesIO()
doc.save(tmp, garbage=3, deflate=True)

# ---- Fix BaseFont metadata ----
pdf = pikepdf.open(io.BytesIO(tmp.getvalue()))
name_map = {'f_demibold': 'AvenirNext-DemiBold', 'f_medium': 'AvenirNext-Medium',
            'f_regular': 'AvenirNext-Regular', 'f_hack': 'Hack-Regular', 'f_mono': 'SpaceMonoItalic'}
fdict = pdf.pages[0].Resources.Font
for key in fdict.keys():
    fd = fdict[key]
    alias = str(key).lstrip('/')
    if alias in name_map and '(null)' in str(fd.get('/BaseFont', '')):
        fd.BaseFont = pikepdf.Name('/' + name_map[alias])
        if '/DescendantFonts' in fd:
            for df in fd.DescendantFonts:
                df.BaseFont = pikepdf.Name('/' + name_map[alias])
                if '/FontDescriptor' in df:
                    df.FontDescriptor.FontName = pikepdf.Name('/' + name_map[alias])
pdf.save(PDF_PATH)
print(f'Wrote {PDF_PATH} (final baseline {final:.1f}/792)')
