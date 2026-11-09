**English** · [Dansk](Step-4-Home-Page-da) · [Bahasa Malaysia](Step-4-Home-Page-ms)

# Step 4: Home page

Capstone task 3: use the API of blog posts to render every title and subtitle on the home page, and give each preview a "Read" anchor.

![The home page with every post's title, subtitle and a Read link](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-4-home-page.png)

## What we gained

- **Combining the lectures.** The `for` loop of step 2 renders one card per post, and `url_for` of step 3 builds the link of each "Read" anchor:

  ```jinja
  {% for post in posts %}
  <div class="card">
      <h2>{{ post.title }}</h2>
      <p class="text">{{ post.subtitle }}</p>
      <a href="{{ url_for('show_post', blog_id=post.id) }}">Read</a>
  </div>
  {% endfor %}
  ```

- **Passing data from a route to a template.** The route `home` calls the use case `list_posts` and gives the result to `index.html` as `posts`.
- **Template inheritance.** `index.html`, `blog.html` and `post.html` extend `base.html`, so the banner, the stylesheet and the footer are written once.
- **Separating concerns.** The route does not call `requests`. It asks a `PostSource`, which makes the page testable without a network.

## In this project

The test `tests/integration/presentation/test_app.py` checks that every post of a stubbed source has its title, its subtitle and a link to `/post/<id>` on the home page.
