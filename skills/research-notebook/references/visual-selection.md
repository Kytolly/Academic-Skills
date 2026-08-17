# Visual Selection

## Selection test

Keep a source figure or table only when at least one answer is yes:

- Does it explain the core method more accurately than prose alone?
- Does it directly support a main empirical claim?
- Does it expose an assumption, failure mode, or tradeoff?
- Will a later reader need it to compare this paper with another method?

Do not keep title-page decoration, redundant qualitative samples, generic dataset examples, or tables whose relevant fact fits in one sentence.

Do not impose a numeric quota or maximum. The right count is determined by explanatory value: include all necessary visuals and stop when additional visuals no longer improve understanding or verification.

## Capture checklist

- Render at 160-220 DPI unless small labels require more.
- Crop outside margins while retaining the caption and essential legend or footnote.
- Check that text remains readable at normal Markdown width.
- Use the paper's original Figure/Table identifier in the filename when available.
- Save every figure and table directly under `assets/` beside the notebook. Do not create asset subdirectories.
- Write concise alt text that describes the visual, not its filename.

## Notebook captions

Use a normal Markdown image with content-focused alt text:

```markdown
![Two-stage architecture](assets/fig-03-two-stage-architecture.png)
```

Do not add screenshot source, PDF page, extraction method, or crop-process wording below the image. If an inference is needed, put it in a separate paragraph beginning with `Interpretation:`. Optional provenance belongs in `source.md`, not the notebook caption.

## Tables

- Prefer a screenshot when exact layout, grouped columns, highlighting, or footnotes matter.
- Prefer a Markdown transcription when searchability matters and the table is small.
- When transcribing, retain the screenshot and disclose omitted rows, reordered columns, rounding, or normalization.
