[English](Step-4-Home-Page) · [Dansk](Step-4-Home-Page-da) · **Bahasa Malaysia**

# Langkah 4: Halaman utama

Tugasan capstone 3: gunakan API siaran blog untuk memaparkan setiap tajuk dan subtajuk pada halaman utama, dan berikan setiap pratonton sauh "Read".

![Halaman utama dengan tajuk, subtajuk dan pautan Read bagi setiap siaran](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-4-home-page.png)

## Apa yang kita peroleh

- **Menggabungkan kuliah.** Gelung `for` dalam langkah 2 memaparkan satu kad bagi setiap siaran, dan `url_for` dalam langkah 3 membina pautan bagi setiap sauh "Read":

  ```jinja
  {% for post in posts %}
  <div class="card">
      <h2>{{ post.title }}</h2>
      <p class="text">{{ post.subtitle }}</p>
      <a href="{{ url_for('show_post', blog_id=post.id) }}">Read</a>
  </div>
  {% endfor %}
  ```

- **Menghantar data daripada laluan ke templat.** Laluan `home` memanggil kes guna `list_posts` dan menyerahkan hasilnya kepada `index.html` sebagai `posts`.
- **Pewarisan templat.** `index.html`, `blog.html` dan `post.html` memanjangkan `base.html`, jadi sepanduk, helaian gaya dan pengaki ditulis sekali sahaja.
- **Pengasingan tanggungjawab.** Laluan tidak memanggil `requests`. Ia bertanya kepada `PostSource`, yang menjadikan halaman boleh diuji tanpa rangkaian.

## Dalam projek ini

Ujian `tests/integration/presentation/test_app.py` menyemak bahawa setiap siaran daripada sumber olok-olok mempunyai tajuk, subtajuk dan pautan ke `/post/<id>` pada halaman utama.
