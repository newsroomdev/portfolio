# CLAUDE.md — portfolio repo

SvelteKit portfolio site for Gerald Rich (geraldri.ch) plus resume build tooling.

## Architecture: where content lives

- **Site content is NOT in this repo.** `src/routes/+page.ts` fetches an ArchieML
  Google Doc at runtime and renders it. Schema in `src/lib/types.ts`:
  top-level `content` array of rows; each row = `hed` {orgTitle, jobTitle,
  link?, dates, guff, skills[]} + `projects[]` {title, role, desc, img, link?}.
  Editing site copy = editing the Google Doc (Gerald does this manually).
- **Images** live in `src/lib/img/`. After adding any, run
  `node scripts/prebuild.js` to regenerate `src/lib/img/index.txt`.
  The `img` field in the doc references these filenames.
- **Resume** is generated, not hand-edited: `etc/resume-builder/build_resume.py`
  writes `static/GeraldRichResume.pdf`. It extracts AvenirNext font subsets
  from the existing PDF (self-hosting bootstrap), downloads Space Mono Italic
  once (gitignored), and fixes BaseFont metadata. Requires `pymupdf pikepdf`.
  Glyph constraint: subsets lack characters unused in the original — notably
  capital L in body text. The script fails loudly naming missing glyphs.
  `etc/GeraldRichResume.pages` is the deprecated former source; safe to delete.

## Handoff tasks (July 2026 session, claude.ai)

1. **Run the resume builder and verify output.**
   `pip3 install pymupdf pikepdf && python3 etc/resume-builder/build_resume.py`
   Expect: `final baseline 752.5/792`. Open the PDF; confirm the Big Local News
   entry leads Experience (bullets ordered DataTalk, Police Records, AgendaWatch).
2. **Capture screenshots for the new BLN portfolio projects** into `src/lib/img/`
   (Playwright is already a dev dependency; `pnpm install` first):
   - `bln_datatalk.png` — https://www.datatalk.genie.stanford.edu/
   - `bln_police_records.png` — https://biglocalnews.org/content/news/2025/08/04/police-records.html
     (or ask Gerald for a screenshot of the database UI at clean.calmatters.org)
   - `bln_agendawatch.png` — https://agendawatch.org/
   Match the crop feel of existing images (e.g. `axios_2018_elections.png`).
   Then `node scripts/prebuild.js`.
3. **Verify the site builds** (`pnpm install && pnpm run build`), then commit
   and push everything (resume PDF + builder + images + index.txt).
4. Gerald pastes the ArchieML block below into the Google Doc himself
   (Claude Code cannot edit Google Docs).

## ArchieML block for Gerald to paste (adapt to the doc's existing idiom)

    hed.orgTitle: Big Local News at Stanford
    hed.jobTitle: Software Developer / Engineer
    hed.link: https://biglocalnews.org/
    hed.dates: 2024 to present
    hed.guff: Big Local News gathers hard-to-obtain government data and builds
    tools that help local newsrooms hold institutions accountable.
    [.hed.skills]
    * Python
    * Data Pipelines
    * GCP
    * Elasticsearch
    * NLP
    * LLM Agents
    []

    [.projects]
    title: DataTalk
    role: Engineer
    link: https://www.datatalk.genie.stanford.edu/
    img: bln_datatalk.png
    desc: An AI agent answering campaign-finance questions with verified data.
    Built with Stanford's Open Virtual Assistant Lab and Columbia Journalism
    School: fine-tuned narrow agents convert plain-English questions into
    auditable queries against FEC filings.

    title: Police Records Access Project
    role: Engineer
    link: https://biglocalnews.org/content/news/2025/08/04/police-records.html
    img: bln_police_records.png
    desc: A first-of-its-kind database of 1.5 million pages of California police
    misconduct and use-of-force records from nearly 500 agencies, processed at
    scale with generative AI. Published in 2025 by the LA Times, SF Chronicle,
    KQED, and CalMatters.

    title: AgendaWatch
    role: Engineer
    link: https://agendawatch.org/
    img: bln_agendawatch.png
    desc: Harvests local government agendas and minutes daily across four metro
    regions and alerts reporters when items on their beats surface in upcoming
    meetings. Prefect-orchestrated pipelines on GCP Cloud Run.
    []

## Open items (decisions pending from Gerald)

- ProPublica dates: resume says Feb.–Sept. 2014, LinkedIn says Feb.–Aug. Pick one.
- Marshall Project: resume Sept. 2014 vs LinkedIn Aug. 2014. Pick one.
- Awards section has no Pulitzer-finalist line. If added, exact phrasing matters:
  the finalist citation names Toness and Lurye; Gerald's honest claim is shaping
  the digital version of the finalist series. Never "Pulitzer finalist" as a
  personal title.
- Webby honors date on LinkedIn reads Jan 2024; winners were announced spring
  2024. Gerald to confirm from his announcement email.

## Style (applies to all prose in this repo)

Strunk & White economy, AP style, Oxford comma, em-dashes without surrounding
spaces, leads with problems before solutions. House styleguide priority:
Strunk & White → Chicago → AP.
