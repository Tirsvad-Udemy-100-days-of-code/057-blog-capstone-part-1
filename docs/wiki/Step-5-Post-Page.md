**English** · [Dansk](Step-5-Post-Page-da) · [Bahasa Malaysia](Step-5-Post-Page-ms)

# Step 5: Post page

Capstone task 4: the "Read" link opens a page with the whole post (title, subtitle and body). Each post lives at the path `/post/<blog_id>`.

![One full post at /post/1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-5-post-page.png)

## What we gained

- **A route with a variable.** `/post/<int:blog_id>` hands the id from the URL to the function `show_post(blog_id)`:

  ```python
  @app.route("/post/<int:blog_id>")
  def show_post(blog_id):
      ...
  ```

- **Finding one item in the data.** The use case `get_post` looks the id up among the posts and raises `PostNotFoundError` when none matches.
- **Meaningful HTTP status codes.** An unknown id gives a friendly page with status 404, and an API that cannot be reached gives status 503. Both are handled in one place each, not inside every route.
- **The same link in both directions.** The "Read" link of step 4 and this route are connected only by the function name `show_post`, through `url_for`.

## In this project

`tests/integration/presentation/test_app.py` has tests for a found post, an unknown id (404) and an unavailable source (503).
