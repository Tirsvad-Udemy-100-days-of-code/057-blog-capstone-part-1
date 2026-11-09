[English](Step-1-Starter-Site) · **Dansk** · [Bahasa Malaysia](Step-1-Starter-Site-ms)

# Trin 1: Startside

Opgaven tager udgangspunkt i kursets startfiler: en Flask-fil `main.py`, et stylesheet og to HTML-skabeloner. Når den køres, vises en stylet "My Blog"-side med to pladsholderkort, "Just a blog post" og "Another blog post".

![Startsiden med to pladsholderindlæg](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-1-starter-site.png)

## Hvad vi fik ud af det

- **Et fast design at udfylde.** Udseendet (banner, hvide kort, røde links, sidefod) er givet. Opgaven er at erstatte den hårdkodede tekst med data.
- **`render_template`.** Ruten `home` returnerer `render_template("index.html")`. Flask leder efter filen i mappen `templates` og efter CSS'en i mappen `static`.
- **Et tydeligt udgangspunkt.** Alt på siden er fast tekst, så vi kan se præcis, hvad der skal blive dynamisk: titlen, undertitlen og "Read"-linket på hvert kort.

## I dette projekt

De to pladsholderkort er det første, skærmbilledscriptet gengiver, gennem samme `create_app` som den færdige side, så trinnet kan genskabes. Skabelonerne deler nu én `base.html`, så banner og sidefod kun findes ét sted.
