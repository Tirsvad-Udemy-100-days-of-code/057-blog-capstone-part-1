[English](Step-2-Jinja-Loops-And-Conditions) · [Dansk](Step-2-Jinja-Loops-And-Conditions-da) · **Bahasa Malaysia**

# Langkah 2: Gelung dan syarat Jinja

Kuliah "Multiline Statements with Jinja". Ungkapan satu baris seperti `{{ post.title }}` tidak mencukupi apabila halaman perlu mengulang satu blok bagi setiap siaran atau memaparkan blok hanya kadangkala. Jinja mempunyai pernyataan berbilang baris untuk tujuan itu.

![Halaman blog: setiap siaran disenaraikan oleh gelung for Jinja](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-2-blog-for-loop.png)

## Apa yang kita peroleh

- **Pernyataan menggunakan `{% %}`, ungkapan menggunakan `{{ }}`.** Ungkapan mencetak nilai. Pernyataan mengawal aliran dan tidak mencetak apa-apa sendiri.
- **Gelung `for` memaparkan senarai.** Laluan mengambil siaran daripada API dan menyerahkannya kepada templat; templat mengulang satu kad bagi setiap siaran:

  ```jinja
  {% for post in posts %}
  <div class="card">
      <h2>{{ post.title }}</h2>
      <p class="text">{{ post.subtitle }}</p>
  </div>
  {% endfor %}
  ```

- **Pernyataan `if` memaparkan kandungan secara bersyarat.** Blok mesti ditutup dengan `endif` (dan gelung dengan `endfor`); `else` mengendalikan kes yang lain:

  ```jinja
  {% if posts %} ... {% else %}
  <p class="text">No posts yet.</p>
  {% endif %}
  ```

- **API sebagai sumber data.** Kuliah menggunakan perkhidmatan n:Point sebagai bin JSON yang bertindak sebagai API, jadi tiada log masuk diperlukan. Pustaka `requests` mengambilnya.

## Dalam projek ini

Laluan `get_blog` memaparkan `blog.html` dengan gelung ini. Panggilan API terletak dalam `ApiPostSource`, jadi templat tidak pernah tahu dari mana siaran datang dan ujian boleh menggantikan sumber itu dengan yang palsu.
