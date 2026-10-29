# Arbin Sigdel - Portfolio (Streamlit)

A one-page portfolio: intro, about, experience, projects, skills, contact, and a CV download button.

```
arbin-portfolio/
  app.py                   layout and styling (you rarely need to touch this)
  content.py               ALL your text: edit this file
  requirements.txt         one dependency: streamlit
  assets/                  your CV PDF (and an optional profile.jpg)
  .streamlit/config.toml   colours and settings
```

## 1. Run it on your computer

```bash
cd arbin-portfolio
pip install -r requirements.txt
streamlit run app.py
```

It opens at http://localhost:8501. Edit `content.py`, save, and the page refreshes.

## 2. Before you deploy: fill in these three things

1. **Project links.** In `content.py`, each project's `"code"` currently points to your GitHub profile. Replace it with the exact repository URL (for example `https://github.com/arbinsigdel12/clickcart`). If a project has no public repo, set `"code": ""` and the link disappears.
2. **Profile photo (optional).** Save a photo as `assets/profile.jpg`. It shows next to the intro automatically. No file, no photo.
3. **Check every sentence.** Only keep claims you can explain in an interview. The line "Working on right now: unit testing, Git, SQL" is only honest if you are doing it.

## 3. Deploy free on Streamlit Community Cloud

1. **Put the folder on GitHub.** Create a new *public* repository (for example `portfolio`) on github.com, then in the project folder run:
   ```bash
   git init
   git add .
   git commit -m "Add portfolio"
   git branch -M main
   git remote add origin https://github.com/arbinsigdel12/portfolio.git
   git push -u origin main
   ```
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app** and choose **Deploy a public app from GitHub**.
4. Select your repository and branch `main`, and set the main file path to `app.py`.
5. Open **Advanced settings**, choose Python 3.12 or newer, and pick a custom subdomain such as `arbin-sigdel` so your link becomes `https://arbin-sigdel.streamlit.app`.
6. Click **Deploy**. The first build takes a few minutes.

To update the site later, edit the files and run `git add . && git commit -m "Update" && git push`. It redeploys by itself.

## Good to know

- Free Streamlit apps go to sleep when nobody visits for a while. The next visitor sees a "wake up" button and waits a few seconds. **Open your link yourself shortly before you share it or before an interview.**
- Put the link at the top of your CV and on your LinkedIn and GitHub profiles.
- The fonts (Source Serif 4 and Source Sans 3) load from Google Fonts. If they cannot load, the page falls back to Georgia and your system font and still looks fine.
- To change colours, edit `.streamlit/config.toml` (button and background colours) and the `:root{...}` line in the CSS near the top of `app.py`.
