# 🚀 Blog Capstone Part 1 (Templating)

Day 57 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": a small Flask blog that lists the posts of a JSON API on the home page and shows each post at `/post/<blog_id>`. It is for course participants who compare solutions and for visitors who browse the repository for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The assignment combines two lectures, "Multiline Statements with Jinja" and "URL building", into one project: fetch the blog posts from an n:Point JSON bin, render every title and subtitle on the home page with a Jinja `for` loop, and link each preview with a "Read" anchor (`url_for`) to a page with the whole post.

| Folder | What it holds |
| --- | --- |
| `src/` | The application, in the layers `domain`, `application`, `infrastructure` and `presentation`; constants are in `src/blog_capstone/constants.py` |
| `tests/` | The pytest tests; they run without network access |
| `docs/` | Project documents, screenshots and the wiki (English, Danish and Bahasa Malaysia) |

Source comments use the Doxygen style inside PEP 257 docstrings; `Doxyfile` is in the repository root.

```python
def show_post(blog_id: int) -> str:
    """@brief Render one blog post.

    @param blog_id Identifier taken from the URL.
    @return The rendered HTML page.
    """
```

A module docstring is one line, `"""@brief ..."""`. A constant has a string literal with `@brief` directly after it.

## 📋 Requirements

- Python 3.13 or newer, with the `venv` module.
- Flask and requests are the only runtime dependencies (the web framework and the HTTP client for the API).
- pytest for the tests (development only).
- Doxygen, only if you want to build the API documentation.

## 🛠️ Setup

Create a local virtual environment named `.venv` in the repository root, upgrade pip inside it and install the project with its test tools.

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

While the environment is active, the prompt starts with `(.venv)`. Leave it with `deactivate`. The `.venv` folder is ignored by git.

Build the API documentation (optional):

```bash
doxygen Doxyfile
```

## ▶️ Run

The application is added in milestone MIL-002; this section is completed there.

## 🧪 Tests

```bash
python -m pytest
```

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
