[English](Step-1-Starter-Site) · [Dansk](Step-1-Starter-Site-da) · **Bahasa Malaysia**

# Langkah 1: Tapak permulaan

Tugasan bermula daripada fail permulaan kursus: sebuah `main.py` Flask, helaian gaya dan dua templat HTML. Apabila dijalankan, ia memaparkan tapak "My Blog" yang telah digayakan dengan dua kad tempat letak, "Just a blog post" dan "Another blog post".

![Tapak permulaan dengan dua siaran tempat letak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/raw/branch/main/docs/images/step-1-starter-site.png)

## Apa yang kita peroleh

- **Reka bentuk tetap untuk diisi.** Rupanya (sepanduk, kad putih, pautan merah, pengaki) telah disediakan. Tugasnya ialah menggantikan teks yang ditetapkan secara kekal dengan data.
- **`render_template`.** Laluan `home` memulangkan `render_template("index.html")`. Flask mencari fail itu dalam folder `templates` dan CSS dalam folder `static`.
- **Titik permulaan yang jelas.** Segala-galanya pada halaman ialah teks tetap, jadi kita dapat melihat dengan tepat apa yang perlu menjadi dinamik: tajuk, subtajuk dan pautan "Read" bagi setiap kad.

## Dalam projek ini

Dua kad tempat letak ialah perkara pertama yang dijana oleh skrip tangkapan skrin, melalui `create_app` yang sama seperti tapak yang siap, jadi langkah ini boleh dihasilkan semula. Templat kini berkongsi satu `base.html`, jadi sepanduk dan pengaki wujud di satu tempat sahaja.
