[English](Step-3-URL-Building) · [Dansk](Step-3-URL-Building-da) · **Bahasa Malaysia**

# Langkah 3: Pembinaan URL

Kuliah "URL building". Aplikasi web memerlukan pautan, contohnya daripada halaman utama ke halaman blog. Menulis laluan secara manual akan rosak apabila laluan berubah. `url_for` membina laluan daripada nama fungsi Python yang melayaninya.

![Halaman blog untuk nombor 7; label menunjukkan laluan URL /blog/7](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-3-url-parameter.png)

## Apa yang kita peroleh

- **Pautan mengikut nama fungsi.** Dalam templat, `url_for('get_blog')` memberikan laluan bagi laluan `get_blog`. Ubah laluan dalam Python dan setiap pautan dikemas kini.
- **Argumen kata kunci menjadi parameter URL.** `url_for('get_blog', num=1)` membina `/blog/1`. Tangkapan skrin menunjukkan `/blog/7`.
- **Laluan menangkap nilai.** Kurungan sudut dalam laluan mengambil sebahagian daripada laluan sebagai argumen fungsi; `<int:num>` turut menukarkannya kepada integer dan memberi 404 untuk yang lain:

  ```python
  @app.route("/blog/<int:num>")
  def get_blog(num):
      ...
  ```

- **Bukti bahawa nilai telah sampai.** Kuliah mencetak parameter dalam konsol. Projek ini merekodkannya dengan `logging`, dan satu ujian menyemak bahawa `num=7` direkodkan.

## Dalam projek ini

Halaman utama mempunyai pautan "Blog page" yang dibina dengan `url_for('get_blog', num=1)`. Halaman memaparkan "Blog number 7" untuk `/blog/7`, jadi nilai daripada URL dapat dilihat.
