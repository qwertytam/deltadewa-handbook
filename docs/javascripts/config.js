// MathJax configuration for pymdownx.arithmatex in `generic: true` mode.
//
// Arithmatex emits math wrapped in \(...\) and \[...\] inside elements
// carrying class="arithmatex", so MathJax is scoped to those elements only
// and left to ignore the rest of the page.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

// Material's instant navigation swaps page content without a full reload, so
// MathJax must be told to re-typeset. Without this, math renders on first
// load and then appears as raw TeX on every subsequent in-site navigation.
document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
