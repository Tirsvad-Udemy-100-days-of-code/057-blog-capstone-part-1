[English](Run-And-Test) · [Dansk](Run-And-Test-da) · **Bahasa Malaysia**

# Jalankan dan uji

Python 3.13 atau lebih baharu diperlukan.

## Cipta dan gunakan .venv setempat

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Prompt bermula dengan `(.venv)` semasa persekitaran aktif; `deactivate` keluar daripadanya. Folder `.venv` tidak di-commit.

## Jalankan

```bash
python -m blog_capstone
```

Buka <http://127.0.0.1:5000>. Halamannya ialah `/`, `/blog/<num>` dan `/post/<blog_id>`.

## Uji

```bash
python -m pytest
```

Ujian tidak pernah menggunakan rangkaian.

## Tangkapan skrin

Tangkapan skrin wiki ini diambil dalam kontena Docker, bukan pada desktop anda:

```bash
bash docs/screenshots/run.sh
```

## Dokumentasi sumber

```bash
doxygen Doxyfile
```
