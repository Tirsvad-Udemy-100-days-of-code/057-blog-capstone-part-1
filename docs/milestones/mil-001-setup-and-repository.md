# MIL-001 Setup and repository

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after [RC-004] (autonomous, not independent) | pending |

---

## Purpose

Decide whether the project skeleton is ready for application code: configuration, environment instructions, documentation tooling and a described repository.

## Deliverable

A repository with `pyproject.toml`, Python `.gitignore`, `src/constants.py`, empty `src/` and `tests/` packages with one passing smoke test, a `Doxyfile`, a first README with `.venv` instructions, and the repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m venv .venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` succeed on Python 3.13 | Succeeds | Any step fails |
| 2 | `python -m pytest` passes the smoke test | 0 failures | Any failure |
| 3 | `pyproject.toml` declares `requires-python = ">=3.13"` and only Flask and requests as runtime dependencies | Yes | Other runtime dependency |
| 4 | `.gitignore` excludes `.venv`, `.env` and Python caches; `.env` is not tracked or referenced by code | Yes | Tracked or referenced |
| 5 | `doxygen Doxyfile` runs without errors | No errors | Errors |
| 6 | The repository has a description and topics on the git host | Present | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [BC-001], SA-001, PP-001 accepted | The plan-first gate |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4 (offline pytest), Objective 5 (venv documentation), Objective 7 (description and topics) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — inside the one-week window of the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml, .gitignore and constants.py | Create `pyproject.toml` (Python 3.13 or newer, runtime dependencies Flask and requests, `dev` extra with pytest, pytest settings), a Python `.gitignore` that also ignores `.venv` and `.env`, and `src/constants.py` for constants. The folders `src/` and `tests/` get a package layout following the clean-architecture skill, with one smoke test. | No | |
| 2 | Add Doxyfile and Doxygen comment style | Add a `Doxyfile` for `src/` with Python support, and document the Doxygen comment style used in the source (`##` and `@param` blocks). Check that `doxygen Doxyfile` runs. | No | |
| 3 | Document the local .venv in the README | Create `README.md` from the framework template with the steps to create and activate `.venv`, run `python -m pip install --upgrade pip`, install the project and run the tests, for Windows and Linux. Screenshots are added in MIL-003. | No | |
| 4 | Set repository description and topics | Set a short description and topics (python, flask, jinja2, udemy, 100-days-of-code, templating, blog) on the git host through its API, using the token from the local `.env` only in the shell; the project never reads `.env`. | No | |

---

[BC-001]: ../business-case.md
[RC-004]: ./../sqa/reviews/rc-004-mil-001.md
