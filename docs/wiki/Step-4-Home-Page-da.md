[English](Step-4-Home-Page) · **Dansk** · [Bahasa Malaysia](Step-4-Home-Page-ms)

# Trin 4: Forside

Capstone-opgave 3: brug API'et med blogindlæg til at gengive hver titel og undertitel på forsiden, og giv hvert eksempel et "Read"-anker.

![Forsiden med hvert indlægs titel, undertitel og et Read-link](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-4-home-page.png)

## Hvad vi fik ud af det

- **Forelæsningerne kombineret.** `for`-løkken fra trin 2 gengiver ét kort pr. indlæg, og `url_for` fra trin 3 bygger linket i hvert "Read"-anker:

  ```jinja
  {% for post in posts %}
  <div class="card">
      <h2>{{ post.title }}</h2>
      <p class="text">{{ post.subtitle }}</p>
      <a href="{{ url_for('show_post', blog_id=post.id) }}">Read</a>
  </div>
  {% endfor %}
  ```

- **Videregivelse af data fra en rute til en skabelon.** Ruten `home` kalder use casen `list_posts` og giver resultatet til `index.html` som `posts`.
- **Skabelonarv.** `index.html`, `blog.html` og `post.html` udvider `base.html`, så banneret, stylesheetet og sidefoden kun skrives én gang.
- **Adskillelse af ansvar.** Ruten kalder ikke `requests`. Den spørger en `PostSource`, hvilket gør siden testbar uden netværk.

## I dette projekt

Testen `tests/integration/presentation/test_app.py` kontrollerer, at hvert indlæg fra en stubbet kilde har sin titel, sin undertitel og et link til `/post/<id>` på forsiden.
