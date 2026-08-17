# Paper Visual Evidence

Paper-reading workflows may embed original-paper figures and tables when they materially improve explanation or verification. Use source-linked crops or page screenshots, not agent-created replacements.

## When to capture

- Capture a figure or table only when prose alone would make the mechanism, evidence, or comparison harder to understand.
- Prefer the smallest useful crop. Keep captions, legends, axis labels, headers, and essential footnotes when they matter.
- Preserve the original visual content. Do not redraw, recolor, or silently edit it.
- If the PDF cannot be rendered reliably, omit the visual instead of inventing one.

## Portable asset layout

Store every figure and table file directly in the output workspace's `assets/` directory:

```text
{output-root}/
|-- note-or-artifact.md
`-- assets/
    |-- fig-03-model-architecture.png
    `-- table-02-main-results.png
```

Do not create `assets/figures/`, `assets/tables/`, `assets/papers/`, or other asset subdirectories. In multi-paper workspaces, prefix filenames with the paper slug to avoid collisions, for example `reactivegwm-fig-03-action-module.png`.

Use lowercase hyphenated filenames. Prefer PNG for diagrams, plots, and tables; use JPEG only for photographic content.

## Capture and verification

1. Render the relevant PDF page at a resolution that keeps labels readable.
2. Crop the figure or table while retaining essential content.
3. Inspect the crop for clipping, unreadable text, missing borders, or broken glyphs.
4. Save it directly under `assets/` and calculate the relative path from the Markdown artifact.
5. Verify that the Markdown link resolves after moving the whole output directory.

## Markdown convention

Use a normal relative Markdown image reference:

```markdown
![Figure 3. Two-stage architecture](assets/fig-03-two-stage-architecture.png)
```

For Markdown files inside a child directory, calculate the appropriate relative path, such as `../assets/reactivegwm-fig-03-action-module.png`.

Keep captions focused on what the visual shows. Do not add `Source visual`, `screenshot from PDF`, PDF page, extraction method, crop process, or similar provenance wording beneath the image. If internal provenance is useful, keep it in a separate source record or asset index rather than the notebook caption.

## Portability checks

- Every referenced image must exist directly under the output workspace's `assets/` directory.
- Use only relative links; never use `file://`, absolute machine paths, data URIs, or temporary paths.
- Do not use a screenshot as evidence for a claim it does not directly show.
- Preserve existing user-curated assets when updating a note.
