# Rollback

Remove these two lines from any affected HTML page:

```html
<link rel="stylesheet" href="./src/ui4-unified.css">
<script type="module" src="./src/ui4-shell.js"></script>
```

The original page styling and logic will immediately resume after GitHub Pages redeploys.
