**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Blog Capstone Part 1 (Templating)

Day 57 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". A small Flask blog fetches its posts from a JSON API, lists every title and subtitle on the home page and shows each post at `/post/<blog_id>`. This wiki walks through the lecture steps, shows a screenshot of each and explains what we gained from it.

| Page | Read it when you want to |
| --- | --- |
| [Step 1: Starter site](Step-1-Starter-Site) | See where the project starts: the styled site with placeholder posts |
| [Step 2: Jinja loops and conditions](Step-2-Jinja-Loops-And-Conditions) | Learn multiline Jinja statements: `for`, `if`, `else` and `endif` |
| [Step 3: URL building](Step-3-URL-Building) | Learn `url_for` and how a value travels from a link to a route |
| [Step 4: Home page](Step-4-Home-Page) | See the capstone home page with every post and its "Read" link |
| [Step 5: Post page](Step-5-Post-Page) | See one full post at `/post/<blog_id>` and how a missing post gives 404 |
| [Run and test](Run-And-Test) | Create the `.venv`, start the app and run the tests |

## The project in one picture

| Part | What it does |
| --- | --- |
| `src/blog_capstone/domain` | The `Post` data and the errors |
| `src/blog_capstone/application` | Use cases `list_posts` and `get_post`, and the `PostSource` port |
| `src/blog_capstone/infrastructure` | `ApiPostSource`, which reads the JSON API with `requests` |
| `src/blog_capstone/presentation` | The Flask routes `home`, `get_blog` and `show_post`, the Jinja templates and the CSS |
| `tests/` | pytest tests that run without network access |

The repository is at <https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1>.
