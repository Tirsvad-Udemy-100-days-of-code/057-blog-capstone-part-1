[English](Step-5-Post-Page) · **Dansk** · [Bahasa Malaysia](Step-5-Post-Page-ms)

# Trin 5: Indlægsside

Capstone-opgave 4: "Read"-linket åbner en side med hele indlægget (titel, undertitel og brødtekst). Hvert indlæg ligger på stien `/post/<blog_id>`.

![Ét helt indlæg på /post/1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-5-post-page.png)

## Hvad vi fik ud af det

- **En rute med en variabel.** `/post/<int:blog_id>` sender id'et fra URL'en videre til funktionen `show_post(blog_id)`:

  ```python
  @app.route("/post/<int:blog_id>")
  def show_post(blog_id):
      ...
  ```

- **At finde ét element i dataene.** Use casen `get_post` slår id'et op blandt indlæggene og rejser `PostNotFoundError`, når intet passer.
- **Meningsfulde HTTP-statuskoder.** Et ukendt id giver en venlig side med status 404, og et API, der ikke kan nås, giver status 503. Begge håndteres ét sted hver, ikke inde i hver rute.
- **Det samme link i begge retninger.** "Read"-linket fra trin 4 og denne rute er kun forbundet via funktionsnavnet `show_post`, gennem `url_for`.

## I dette projekt

`tests/integration/presentation/test_app.py` har tests for et fundet indlæg, et ukendt id (404) og en utilgængelig kilde (503).
