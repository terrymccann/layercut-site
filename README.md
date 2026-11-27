# layercut.app

The LayerCut website: a home page, documentation, a roadmap, and legal pages. Live at https://layercut.app. It's a static site, built with one Python script and hosted on Cloudflare Pages.

```
src/home.html        home page body
src/docs/*.md        documentation, one Markdown file per page (order is set in build.py)
src/legal/*.md       terms, privacy, refunds, license keys
src/roadmap.md       the roadmap page
src/changelog.md     the changelog page
src/*.svg            the cut-sheet drawings used on the home page
assets/              site.css, site.js, fonts (Archivo, SIL Open Font License)
img/                 screenshots, icons, social image
build.py             writes the finished site into dist/
```

## Build

```sh
pip install markdown
python3 build.py          # → dist/
python3 -m http.server 8787 --directory dist    # preview at http://localhost:8787
```

## Deploy to Cloudflare Pages

### Option A — from the terminal (recommended)

```sh
npx wrangler login                                   # once; approve in the browser
npx wrangler pages project create layercut-site --production-branch main   # once
python3 build.py
npx wrangler pages deploy dist --project-name layercut-site --branch main
```

### Option B — in the dashboard, no tools needed

1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** → **Upload assets**.
2. Project name `layercut-site`, then drag in the `dist` folder (or `layercut-site-dist.zip`) → **Deploy site**.
3. Later updates: open the project → **Create deployment** → upload the new `dist`.

### Connect layercut.app (once)

1. In the Pages project → **Custom domains** → **Set up a custom domain** → `layercut.app` → **Activate domain**.
2. Repeat for `www.layercut.app`.
3. Redirect www to the bare domain: **layercut.app zone → Rules → Redirect Rules → Create rule → template "Redirect from WWW to root"**.

### Email

The site uses `hello@layercut.app`. Set up forwarding to your inbox in **layercut.app zone → Email → Email Routing → Routing rules → Create address**.

### Current setup

The site is live on the Pages project `layercut-site` (direct upload), with `layercut.app` and `www.layercut.app` attached. `hello@layercut.app` forwards through Cloudflare Email Routing. To publish a change: build, zip the contents of `dist/`, and upload it as a new deployment (Option B, step 3).

## Things that update themselves

- **Stylesheet and script links** carry a content hash (`?v=`), so browsers never keep a stale copy after a deploy.

- **Download buttons** read `https://downloads.layercut.app/latest/version.json`, which the release workflow publishes. Until the first release exists, the buttons show "Soon" and invite people to email for the beta.
- **sitemap.xml** is regenerated on every build.
