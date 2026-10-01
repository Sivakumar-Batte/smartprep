# Installation

1. Upload `src/ui4-unified.css` and `src/ui4-shell.js` to the repository `src` folder.
2. For each page below, edit the file in GitHub and add the stylesheet tag before `</head>` and script tag before `</body>`:
   - `app.html`
   - `focus.html`
   - `practice.html`
   - `revision.html`
   - `queue.html`
   - `analytics.html`
   - `cloud.html`
   - `index.html`
3. Copy the exact tags from `snippets/add-to-each-page.html`.
4. Commit each page or all pages with: `Apply SmartPrep UI Sprint 4 unified shell`.
5. Wait 2–5 minutes and hard-refresh the browser (`Ctrl+Shift+R`).
6. Validate one page at a time. If a page has a visual conflict, remove only the two UI4 tags from that page; its engine remains untouched.

## Homepage migration
Do not redirect `index.html` until every page passes validation. After acceptance, either keep Evidence at `/index.html` and bookmark `/app.html`, or copy the old Evidence page to `evidence.html` before making `index.html` redirect to `app.html`.
