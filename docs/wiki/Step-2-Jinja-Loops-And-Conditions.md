**English** · [Dansk](Step-2-Jinja-Loops-And-Conditions-da) · [Bahasa Malaysia](Step-2-Jinja-Loops-And-Conditions-ms)

# Step 2: Jinja loops and conditions

Lecture "Multiline Statements with Jinja". Single-line expressions such as `{{ post.title }}` are not enough when a page must repeat a block for every post or show a block only sometimes. Jinja has multiline statements for that.

![The blog page: every post listed by a Jinja for loop](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-2-blog-for-loop.png)

## What we gained

- **Statements use `{% %}`, expressions use `{{ }}`.** An expression prints a value. A statement controls the flow and prints nothing itself.
- **A `for` loop renders a list.** The route fetches the posts from the API and passes them to the template; the template repeats one card per post:

  ```jinja
  {% for post in posts %}
  <div class="card">
      <h2>{{ post.title }}</h2>
      <p class="text">{{ post.subtitle }}</p>
  </div>
  {% endfor %}
  ```

- **An `if` statement shows content conditionally.** A block must be closed with `endif` (and a loop with `endfor`); `else` handles the other case:

  ```jinja
  {% if posts %} ... {% else %}
  <p class="text">No posts yet.</p>
  {% endif %}
  ```

- **An API as a data source.** The lecture uses the n:Point service as a JSON bin that acts as an API, so no login is needed. The `requests` library fetches it.

## In this project

The route `get_blog` renders `blog.html` with this loop. The API call lives in `ApiPostSource`, so the template never knows where the posts came from and the tests can replace the source with a fake.
