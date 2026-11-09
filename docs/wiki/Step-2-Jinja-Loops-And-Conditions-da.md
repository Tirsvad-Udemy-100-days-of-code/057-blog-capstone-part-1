[English](Step-2-Jinja-Loops-And-Conditions) · **Dansk** · [Bahasa Malaysia](Step-2-Jinja-Loops-And-Conditions-ms)

# Trin 2: Jinja-løkker og betingelser

Forelæsningen "Multiline Statements with Jinja". Enlinjede udtryk som `{{ post.title }}` rækker ikke, når en side skal gentage en blok for hvert indlæg eller kun vise en blok nogle gange. Til det har Jinja flerlinjede sætninger.

![Blogsiden: alle indlæg listet med en Jinja for-løkke](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-2-blog-for-loop.png)

## Hvad vi fik ud af det

- **Sætninger bruger `{% %}`, udtryk bruger `{{ }}`.** Et udtryk udskriver en værdi. En sætning styrer forløbet og udskriver ikke selv noget.
- **En `for`-løkke gengiver en liste.** Ruten henter indlæggene fra API'et og sender dem til skabelonen; skabelonen gentager ét kort pr. indlæg:

  ```jinja
  {% for post in posts %}
  <div class="card">
      <h2>{{ post.title }}</h2>
      <p class="text">{{ post.subtitle }}</p>
  </div>
  {% endfor %}
  ```

- **En `if`-sætning viser indhold betinget.** En blok skal lukkes med `endif` (og en løkke med `endfor`); `else` håndterer det andet tilfælde:

  ```jinja
  {% if posts %} ... {% else %}
  <p class="text">No posts yet.</p>
  {% endif %}
  ```

- **Et API som datakilde.** Forelæsningen bruger n:Point-tjenesten som en JSON-bin, der fungerer som et API, så der ikke kræves login. Biblioteket `requests` henter det.

## I dette projekt

Ruten `get_blog` gengiver `blog.html` med denne løkke. API-kaldet ligger i `ApiPostSource`, så skabelonen aldrig ved, hvor indlæggene kom fra, og testene kan erstatte kilden med en falsk.
