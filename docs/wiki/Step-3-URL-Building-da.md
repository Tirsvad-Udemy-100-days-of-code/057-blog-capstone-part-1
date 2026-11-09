[English](Step-3-URL-Building) · **Dansk** · [Bahasa Malaysia](Step-3-URL-Building-ms)

# Trin 3: URL-opbygning

Forelæsningen "URL building". En webapp har brug for links, for eksempel fra forsiden til blogsiden. Hvis stierne skrives i hånden, går det galt, når en rute ændres. `url_for` bygger stien ud fra navnet på den Python-funktion, der betjener den.

![Blogsiden for tallet 7; teksten viser URL-stien /blog/7](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-3-url-parameter.png)

## Hvad vi fik ud af det

- **Links følger funktionsnavnet.** I en skabelon giver `url_for('get_blog')` stien til ruten `get_blog`. Omdøb stien i Python, og alle links opdateres.
- **Nøgleordsargumenter bliver til URL-parametre.** `url_for('get_blog', num=1)` bygger `/blog/1`. Skærmbilledet viser `/blog/7`.
- **Ruten fanger værdien.** Vinkelparenteser i ruten tager en del af stien som funktionsargument; `<int:num>` konverterer den desuden til et heltal og giver 404 for alt andet:

  ```python
  @app.route("/blog/<int:num>")
  def get_blog(num):
      ...
  ```

- **Bevis for, at værdien nåede frem.** Forelæsningen udskriver parameteren i konsollen. Dette projekt logger den med `logging`, og en test kontrollerer, at `num=7` bliver logget.

## I dette projekt

Forsiden har et "Blog page"-link bygget med `url_for('get_blog', num=1)`. Siden viser "Blog number 7" for `/blog/7`, så værdien fra URL'en er synlig.
