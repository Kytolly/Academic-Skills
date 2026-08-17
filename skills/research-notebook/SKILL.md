---
name: research-notebook
description: Create or update a portable Markdown research notebook for one paper from a PDF, arXiv paper, local paper file, or supplied full text. Use when the user asks to read, summarize, annotate, take notes on, explain, or archive a single academic paper, especially when the note should include selected original figures or tables captured from the PDF and remain usable after moving to another environment.
---

# Research Notebook

Create one evidence-linked notebook for exactly one paper. Preserve the distinction between the paper's claims, the agent's interpretation, and the user's notes.

## Output Root

- If the user gives an exact output path, use it exactly.
- Otherwise create `{workspace-root}/paper-notebooks/{paper-slug}/`.
- Treat the notebook directory as the portable unit. Never make the Markdown depend on files outside that directory.

Create:

```text
{notebook-root}/
|-- notebook.md
|-- source.md
`-- assets/
```

Read `references/source-template.md` before writing `source.md`. Read `references/notebook-template.md` before writing `notebook.md`. Read `references/visual-selection.md` before selecting or capturing PDF visuals.

Use `docs/agents/markdown-math.md` for every formula. Inline formulas must use `$...$`; display formulas must use `$$...$$` on separate lines. Never emit `\(...\)`, `\[...\]`, or raw display environments.

## Workflow

1. Identify exactly one source paper and one notebook output path.
2. Inspect the PDF before summarizing:
   - verify the title, authors, year, venue or preprint status, page count, and stable resource identifier;
   - extract text for search and section navigation;
   - render visually important pages because extracted text does not preserve layout.
3. Write `source.md` with bibliographic metadata, source URL or identifier, supplied local path, access status, and extraction limitations.
4. Read in this order: abstract and introduction, related work, method, experiments, limitations or discussion, conclusion, then targeted appendices.
5. Draft the notebook around the paper's research problem, field position, assumptions, method, evidence, results, limitations, and reusable ideas. Do not produce a section-by-section paraphrase.
6. Select only figures and tables that materially improve explanation or verification.
7. Render the relevant page, crop the visual, inspect it, save it directly under `assets/`, and embed it with a relative Markdown link. Do not add screenshot-source wording to the notebook caption.
8. Distinguish explicitly among:
   - `Paper claim`: what the paper states or demonstrates;
   - `Interpretation`: the agent's synthesis or inference;
   - `User note`: a user-authored judgment that must be preserved verbatim or clearly attributed.
9. Run `scripts/validate_notebook.py` against `notebook.md` and resolve every missing or non-portable image reference.
10. Reopen the final Markdown and representative images. Confirm that the note is readable without the source PDF and that no essential visual is clipped or illegible.

## PDF and Visual Rules

- Use the PDF skill's visual workflow. Prefer `scripts/render_pdf_pages.py` for deterministic page rendering and `scripts/crop_image.py` for crops.
- Use no fixed minimum or maximum number of figures and tables. Include every visual that materially improves explanation or verification, and omit visuals that are decorative, redundant, or already captured clearly in prose.
- Prefer, in order: method overview, data or task construction, main quantitative results, diagnostic or ablation result, and one qualitative example that reveals a claimed capability or failure.
- Retain captions, legends, axis labels, row and column headers, and essential footnotes. Never silently alter the source visual.
- Use PNG for diagrams, plots, and tables. Use lowercase descriptive filenames such as `fig-03-model-architecture.png`.
- Store every figure and table file directly in `assets/`; do not create `figures/`, `tables/`, `papers/`, or other asset subdirectories.
- Do not embed absolute paths, `file://` links, base64 data URIs, temporary paths, or images hosted only on the web.
- Do not reproduce the full paper as page screenshots. Capture the minimum source material needed for research explanation.
- Keep notebook captions content-focused. Do not write `Source visual`, `screenshot from`, PDF page, crop method, or similar provenance text below images. If provenance tracking is useful, record it only in the `source.md` Visual Asset Index.
- Follow `docs/agents/paper-visual-evidence.md` for asset naming and migration checks.

The bundled rendering and cropping scripts require Python 3, PyMuPDF (`fitz`), and Pillow. If those libraries are unavailable, use a detected PDF renderer such as Poppler and an image-cropping tool, while preserving the same filenames and validation rules. Do not install dependencies without the user's approval when installation changes the environment.

## Notebook Quality Rules

- After the single `# {Paper Title}` heading, make `## One-Sentence Takeaway` the first second-level heading and `## Paper Information Card` the second. For a localized notebook, use direct translations of those labels in the same order. Put no bibliographic card before the first second-level heading.
- Keep the takeaway to one sentence that states the paper's central move and why it matters.
- Make the notebook useful for later research decisions, not merely shorter than the paper.
- Cite page, section, figure, table, or equation numbers for important technical claims when available.
- Record uncertainty when text extraction, OCR, formulas, or image labels are ambiguous.
- Preserve negative results, assumptions, evaluation constraints, and threats to validity.
- Do not claim that a reported metric proves a broader capability than the experiment tests.
- Keep equations in Markdown/LaTeX when they are central; explain symbols and the equation's role.
- Apply the repository-wide `$...$` / `$$...$$` delimiter rule; do not copy the PDF's `\(...\)` or `\[...\]` delimiters into Markdown.
- For a transcribed table, keep the screenshot as source evidence and label all normalization, omitted columns, or recalculated values.
- Preserve existing user edits and curated assets when updating a notebook.

## Completion Gate

Do not call the notebook complete until:

- `notebook.md`, `source.md`, and every referenced local asset exist;
- all image links are relative and pass the validator;
- every image and table is stored directly under `assets/` and referenced as `assets/{filename}`;
- notebook image captions contain no screenshot-source or crop-process explanation;
- the first two second-level headings are the takeaway and paper-information card, in that order, using the English or Chinese labels defined above;
- paper claims and agent interpretations are distinguishable;
- the method, evidence, main findings, limitations, and open questions are represented;
- the entire notebook directory can be copied without breaking its Markdown images.
