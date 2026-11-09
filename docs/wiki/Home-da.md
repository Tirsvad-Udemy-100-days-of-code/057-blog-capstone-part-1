[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Blog Capstone del 1 (skabeloner)

Dag 57 af Udemys "100 Days of Code: The Complete Python Pro Bootcamp". En lille Flask-blog henter sine indlæg fra et JSON-API, viser alle titler og undertitler på forsiden og viser hvert indlæg på `/post/<blog_id>`. Denne wiki gennemgår forelæsningens trin, viser et skærmbillede af hvert trin og forklarer, hvad vi fik ud af det.

| Side | Læs den, når du vil |
| --- | --- |
| [Trin 1: Startside](Step-1-Starter-Site-da) | Se, hvor projektet starter: den stylede side med pladsholderindlæg |
| [Trin 2: Jinja-løkker og betingelser](Step-2-Jinja-Loops-And-Conditions-da) | Lære flerlinjede Jinja-sætninger: `for`, `if`, `else` og `endif` |
| [Trin 3: URL-opbygning](Step-3-URL-Building-da) | Lære `url_for` og hvordan en værdi rejser fra et link til en rute |
| [Trin 4: Forside](Step-4-Home-Page-da) | Se capstone-forsiden med alle indlæg og deres "Read"-link |
| [Trin 5: Indlægsside](Step-5-Post-Page-da) | Se ét helt indlæg på `/post/<blog_id>`, og hvordan et manglende indlæg giver 404 |
| [Kør og test](Run-And-Test-da) | Oprette `.venv`, starte appen og køre testene |

## Projektet på ét billede

| Del | Hvad den gør |
| --- | --- |
| `src/blog_capstone/domain` | `Post`-dataene og fejlene |
| `src/blog_capstone/application` | Use cases `list_posts` og `get_post` samt porten `PostSource` |
| `src/blog_capstone/infrastructure` | `ApiPostSource`, som læser JSON-API'et med `requests` |
| `src/blog_capstone/presentation` | Flask-ruterne `home`, `get_blog` og `show_post`, Jinja-skabelonerne og CSS'en |
| `tests/` | pytest-tests, der kører uden netværksadgang |

Repositoriet findes på <https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1>.
