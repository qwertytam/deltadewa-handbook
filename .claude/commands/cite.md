---
description: Verify an external claim and wire it into the References page with an inline citation
argument-hint: "\"the claim\" [target page path]"
disable-model-invocation: true
---

Claim to source and cite: $ARGUMENTS

1. Grep `docs/footnotes/index.md` first. If the source is already there, reuse
   its `{ #slug }` — a second entry for the same source is a defect.
2. Otherwise dispatch `source-verifier` with the claim. Require its verdict
   (confirmed / contradicted / unverifiable), the precision note on which
   convention the source uses, and a paste-ready citation block.
3. If the verdict is **contradicted**, stop and report the correct value and
   the pages that would need to change — do not silently edit prose to match.
4. If **unverifiable** from a primary source, do not cite a secondary one.
   Propose softened wording that drops the implied citation instead, and say
   so in the PR body.
5. If **confirmed**, add the entry to `docs/footnotes/index.md` in the correct
   group (alphabetical within its group, matching the existing pattern), then
   add the inline cite `[[Short Label]](../footnotes/index.md#slug)` at the
   claim on the target page.
6. Run `/verify` — a citation whose anchor does not resolve fails the strict
   build, which is exactly the check you want here.
