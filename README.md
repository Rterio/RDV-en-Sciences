# RDV en Sciences: static site

Plain HTML, CSS and JavaScript. No build step, ready for GitHub Pages.

## First steps

1. **Download the images** from the old Google Sites (while it's still online):
   ```
   python3 scripts/telecharger-images.py
   ```
2. **Add the partner logos** (they couldn't be extracted automatically). Save them as PNG in `images/partenaires/`:
   `aesgul.png`, `fsg.png`, `arcelormittal.png`, `crchudequebec.png`, `ulaval.png`, `cadeul.png`, `ibis.png`.
   Until a logo is present, the partner card simply shows the name.
3. **Add the Roca One font** (the 2027 identity typeface, a commercial font): if your team has the licence, save it as `assets/fonts/roca-one.woff2`. Until then, headings use Young Serif, a free look-alike.
4. **Preview locally** (links need a small server, opening the file directly won't navigate correctly):
   ```
   python3 -m http.server 8000
   ```
   then open http://localhost:8000

## Where to edit

| What | File |
|---|---|
| Menu, ticket link, email, social links (all pages) | `assets/site.js`, the `SITE` object at the top |
| Colors, fonts, spacing | `assets/style.css`, the `:root` variables (2027 identity palette) |
| Logo / emblem | `images/logo.png` (header, favicon), `images/embleme.png` (home page), `images/partage-2027.png` (link previews on social media) |
| Home page | `index.html` |
| Activities, partners, team | `activites/`, `partenaires/`, `organisation/` |
| Past editions | `editions/<year>/index.html` |

Each edition page uses that year's logo colors, defined in `assets/editions.css` (one `.ed-AAAA` block per year), with the logo in `images/editions/logo-AAAA.png`.

To add a new edition (e.g. 2027 once it's over):
1. Copy `editions/2025/` to `editions/2027/` and update the text, numbers, topics and photo names.
2. In `assets/editions.css`, copy a `.ed-AAAA` block, rename it `.ed-2027` and set the colors.
3. Change `ed-2025` to `ed-2027` on the page's `<body>`, save the logo as `images/editions/logo-2027.png`.
4. Add the year to the edition buttons, the previous/next links and the timelines on `index.html` and `editions/index.html`.

## Old URLs

The folders with accented names (`activités/`, `éditions-passées/`, `partenaires-2026/`, `accueil/`, `édition-2027/`) are redirect pages. They send old Google Sites links and bookmarks to the new pages. Keep them.

## Before going live

- `CNAME` file: add one containing `rdv-en-sciences.aesgul.com` only when you're ready to switch the domain.
- The ticket link still points to the **2026** Evelya event. Update `billets` in `assets/site.js` when the 2027 page exists.
- The AESGUL partner text says "troisième édition" (copied as-is from the old site).
