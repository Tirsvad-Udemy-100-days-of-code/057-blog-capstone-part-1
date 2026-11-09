[English](Step-5-Post-Page) · [Dansk](Step-5-Post-Page-da) · **Bahasa Malaysia**

# Langkah 5: Halaman siaran

Tugasan capstone 4: pautan "Read" membuka halaman dengan keseluruhan siaran (tajuk, subtajuk dan kandungan). Setiap siaran terletak pada laluan `/post/<blog_id>`.

![Satu siaran penuh di /post/1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-5-post-page.png)

## Apa yang kita peroleh

- **Laluan dengan pemboleh ubah.** `/post/<int:blog_id>` menyerahkan id daripada URL kepada fungsi `show_post(blog_id)`:

  ```python
  @app.route("/post/<int:blog_id>")
  def show_post(blog_id):
      ...
  ```

- **Mencari satu item dalam data.** Kes guna `get_post` mencari id dalam kalangan siaran dan menimbulkan `PostNotFoundError` apabila tiada yang sepadan.
- **Kod status HTTP yang bermakna.** Id yang tidak dikenali memberi halaman mesra dengan status 404, dan API yang tidak dapat dicapai memberi status 503. Kedua-duanya dikendalikan di satu tempat masing-masing, bukan di dalam setiap laluan.
- **Pautan yang sama dalam kedua-dua arah.** Pautan "Read" dalam langkah 4 dan laluan ini disambungkan hanya melalui nama fungsi `show_post`, menerusi `url_for`.

## Dalam projek ini

`tests/integration/presentation/test_app.py` mempunyai ujian untuk siaran yang ditemui, id yang tidak dikenali (404) dan sumber yang tidak tersedia (503).
