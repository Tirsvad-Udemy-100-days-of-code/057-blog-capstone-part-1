[English](Run-And-Test) · **Dansk** · [Bahasa Malaysia](Run-And-Test-ms)

# Kør og test

Python 3.13 eller nyere er påkrævet.

## Opret og brug en lokal .venv

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Prompten starter med `(.venv)`, mens miljøet er aktivt; `deactivate` forlader det. Mappen `.venv` bliver ikke committet.

## Kør

```bash
python -m blog_capstone
```

Åbn <http://127.0.0.1:5000>. Siderne er `/`, `/blog/<num>` og `/post/<blog_id>`.

## Test

```bash
python -m pytest
```

Testene bruger aldrig netværket.

## Skærmbilleder

Wikiens skærmbilleder tages i en Docker-container, aldrig på dit skrivebord:

```bash
bash docs/screenshots/run.sh
```

## Kildedokumentation

```bash
doxygen Doxyfile
```
