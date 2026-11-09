**English** · [Dansk](Step-1-Starter-Site-da) · [Bahasa Malaysia](Step-1-Starter-Site-ms)

# Step 1: Starter site

The assignment starts from the course's starting files: a Flask `main.py`, a stylesheet and two HTML templates. Running it shows a styled "My Blog" site with two placeholder cards, "Just a blog post" and "Another blog post".

![The starter site with two placeholder posts](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-1-starter-site.png)

## What we gained

- **A fixed design to fill in.** The look (banner, white cards, red links, footer) is given. The task is to replace the hard-coded text with data.
- **`render_template`.** The route `home` returns `render_template("index.html")`. Flask looks for the file in the `templates` folder and for the CSS in the `static` folder.
- **A clear starting point.** Everything on the page is fixed text, so we can see exactly what must become dynamic: the title, the subtitle and the "Read" link of each card.

## In this project

The two placeholder cards are the first thing the screenshot script renders, through the same `create_app` as the finished site, so the step is reproducible. The templates now share one `base.html`, so the banner and footer exist in one place only.
