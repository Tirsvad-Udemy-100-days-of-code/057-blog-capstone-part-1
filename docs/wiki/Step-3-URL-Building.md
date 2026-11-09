**English** · [Dansk](Step-3-URL-Building-da) · [Bahasa Malaysia](Step-3-URL-Building-ms)

# Step 3: URL building

Lecture "URL building". A web app needs links, for example from the home page to the blog page. Writing the paths by hand breaks when a route changes. `url_for` builds the path from the name of the Python function that serves it.

![The blog page for the number 7; the label shows the URL path /blog/7](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-3-url-parameter.png)

## What we gained

- **Links follow the function name.** In a template, `url_for('get_blog')` gives the path of the route `get_blog`. Rename the path in Python and every link is updated.
- **Keyword arguments become URL parameters.** `url_for('get_blog', num=1)` builds `/blog/1`. The screenshot shows `/blog/7`.
- **The route captures the value.** Angle brackets in the route take part of the path as a function argument; `<int:num>` also converts it to an integer and gives 404 for anything else:

  ```python
  @app.route("/blog/<int:num>")
  def get_blog(num):
      ...
  ```

- **Proof that the value arrived.** The lecture prints the parameter in the console. This project logs it with `logging`, and a test checks that `num=7` is logged.

## In this project

The home page has a "Blog page" link built with `url_for('get_blog', num=1)`. The page shows "Blog number 7" for `/blog/7`, so the value from the URL is visible.
