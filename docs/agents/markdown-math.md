# Markdown Math Delimiters

All generated Markdown research artifacts must use these delimiters:

- Inline mathematics: `$...$`
- Display mathematics: `$$...$$`

Do not use `\(...\)`, `\[...\]`, `\\begin{equation}...`, or other alternate math delimiters in generated Markdown. Keep display math on its own lines with a blank line before and after it. Use LaTeX commands inside the delimiters as needed.

Example:

```markdown
The action-conditioned transition is represented as $x_{t+1}=f(x_t,a_t)$.

$$
x_{1:T} = F(x_0, a_{1:T}, p)
$$
```

Preserve the paper's mathematical meaning while normalizing only the Markdown delimiters. Explain symbols immediately before or after a display equation. If a formula is only legible in a source screenshot, keep the screenshot as Paper Visual Evidence and transcribe the formula when possible.

