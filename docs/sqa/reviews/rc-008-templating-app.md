# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [227a5fb] |

---

## Artifact Under Review

- Instance reviewed: [PY-002]
- Checklist used: [QC-PY-001]
- Scope: full review of src/blog_capstone and tests at MIL-002 (30 tests)
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case modules and functions, PascalCase classes, UPPER_SNAKE constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; route names follow the assignment (home, get_blog, show_post). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | No formatter or linter is configured; PEP 8 followed by hand, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated; test functions too. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | ApiPostSource wraps requests and JSON errors in PostSourceUnavailableError with raise from. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | The requests session created per call is used as a context manager; an injected session is owned by the caller. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions carry Doxygen docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | logging only; the lecture's printed parameter is logged; no secrets. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; use cases are not modelled (see Project Plan, Open Issues). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 30 pytest tests named for behaviour, no network, no order dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | Optional; no type checker adopted. Three type: ignore comments in tests are justified by JSON-to-dataclass conversion and a frozen-instance assertion. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Flask and requests declared in pyproject.toml, both used; pytest in the dev extra. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The API address and timeout are defined once in constants.py; the layout lives in base.html. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports nothing; application imports domain; infrastructure imports application and domain; presentation imports application and domain; only main.py wires infrastructure. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | The PostSource protocol has one method; the app is open to other sources through create_app. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | domain, application, infrastructure and presentation under src/blog_capstone; tests under unit and integration. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English names with letters, digits and underscores. |

## Overall Verdict

Go — no criterion fails. Autonomous mode: AI as stand-in for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None open | S01 | — |

---
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[PY-002]: ../../../src/blog_capstone/
[227a5fb]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/commit/227a5fbb8a022e447d5509d1353edc55f0287627
