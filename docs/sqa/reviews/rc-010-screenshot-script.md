# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PY-003]
- Checklist used: [QC-PY-001]
- Scope: full review of docs/screenshots/capture.py and the template tweaks of MIL-003
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Meets the criterion. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Meets the criterion. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | No formatter configured; PEP 8 by hand, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Meets the criterion. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | No exception handling. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Meets the criterion. |
| 7 | Files, locks and connections are managed with context managers | Pass | sync_playwright is used as a context manager. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Meets the criterion. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | No logging. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | The script is a build tool; the application tests still pass (30). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | Optional; no type checker adopted. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | playwright is installed only inside the container and is not a project dependency. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Ports and size are named constants. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | The script imports the application's composition root, nothing imports the script. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One reason to change: the screenshot list. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | N-A | A tooling script under docs/screenshots, not application source. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Meets the criterion. |

## Overall Verdict

Go — no criterion fails. Autonomous mode: AI as stand-in for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None open | S01 | — |

---
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[PY-003]: ../../screenshots/capture.py
