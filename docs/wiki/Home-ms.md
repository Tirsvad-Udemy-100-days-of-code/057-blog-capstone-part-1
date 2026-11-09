[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Blog Capstone Part 1 (Templating)

Hari ke-57 dalam "100 Days of Code: The Complete Python Pro Bootcamp" daripada Udemy. Sebuah blog Flask yang kecil mengambil siarannya daripada API JSON, menyenaraikan setiap tajuk dan subtajuk pada halaman utama dan memaparkan setiap siaran di `/post/<blog_id>`. Wiki ini menerangkan langkah-langkah kuliah, menunjukkan tangkapan skrin bagi setiap langkah dan menjelaskan apa yang kita peroleh daripadanya.

| Halaman | Baca apabila anda mahu |
| --- | --- |
| [Langkah 1: Tapak permulaan](Step-1-Starter-Site-ms) | Melihat titik permulaan projek: tapak yang telah digayakan dengan siaran tempat letak |
| [Langkah 2: Gelung dan syarat Jinja](Step-2-Jinja-Loops-And-Conditions-ms) | Mempelajari pernyataan Jinja berbilang baris: `for`, `if`, `else` dan `endif` |
| [Langkah 3: Pembinaan URL](Step-3-URL-Building-ms) | Mempelajari `url_for` dan cara nilai bergerak daripada pautan ke laluan |
| [Langkah 4: Halaman utama](Step-4-Home-Page-ms) | Melihat halaman utama capstone dengan setiap siaran dan pautan "Read"nya |
| [Langkah 5: Halaman siaran](Step-5-Post-Page-ms) | Melihat satu siaran penuh di `/post/<blog_id>` dan cara siaran yang tiada memberi 404 |
| [Jalankan dan uji](Run-And-Test-ms) | Mencipta `.venv`, memulakan aplikasi dan menjalankan ujian |

## Projek dalam satu gambaran

| Bahagian | Fungsinya |
| --- | --- |
| `src/blog_capstone/domain` | Data `Post` dan ralat |
| `src/blog_capstone/application` | Kes guna `list_posts` dan `get_post`, serta port `PostSource` |
| `src/blog_capstone/infrastructure` | `ApiPostSource`, yang membaca API JSON dengan `requests` |
| `src/blog_capstone/presentation` | Laluan Flask `home`, `get_blog` dan `show_post`, templat Jinja dan CSS |
| `tests/` | Ujian pytest yang berjalan tanpa akses rangkaian |

Repositori terdapat di <https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1>.
