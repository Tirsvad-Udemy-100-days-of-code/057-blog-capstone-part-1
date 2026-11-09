**English** · [Dansk](Run-And-Test-da) · [Bahasa Malaysia](Run-And-Test-ms)

# Run and test

Python 3.13 or newer is needed.

## Create and use a local .venv

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The prompt starts with `(.venv)` while the environment is active; `deactivate` leaves it. The `.venv` folder is not committed.

## Run

```bash
python -m blog_capstone
```

Open <http://127.0.0.1:5000>. The pages are `/`, `/blog/<num>` and `/post/<blog_id>`.

## Test

```bash
python -m pytest
```

The tests never use the network.

## Screenshots

The screenshots of this wiki are taken in a Docker container, never on your desktop:

```bash
bash docs/screenshots/run.sh
```

## Source documentation

```bash
doxygen Doxyfile
```
