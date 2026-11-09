# MIL-003 Documentation and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [5fefc13] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after [RC-006] (autonomous, not independent) | [5fefc13] |

---

## Purpose

Decide whether the project can be shared: a README and a three-language wiki that show each lecture step with a screenshot and explain what the step teaches.

## Deliverable

`README.md` with screenshots and run instructions, and `docs/wiki/` with the same page set in English, Danish (`-da`) and Bahasa Malaysia (`-ms`), a sidebar, and the screenshots in `docs/images/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/images/` holds one screenshot per lecture step (five steps), all taken inside a Docker container | 5 files | Fewer, or taken on the host desktop |
| 2 | The README shows every screenshot and explains `.venv`, run and test | Yes | Missing |
| 3 | The wiki has the same page set in `en`, `da` and `ms`, each page starting with the language line | Yes | A page missing |
| 4 | Each wiki step page explains what was gained in the step and shows its screenshot | Yes | Missing |
| 5 | The wiki is reviewed against `QC-WIKI-001` and the README check script passes | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Screenshots need the working application |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 5 and 6; success criteria 4, 5 and 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-13 — inside the one-week window of the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Take screenshots of each lecture step in a Docker container | Run the application and a headless browser in a Docker container (never on the host desktop, per `gui-testing.md`) and capture five screenshots into `docs/images/`: 1 starter site, 2 blog list with a Jinja loop, 3 url_for links with a parameter, 4 capstone home page, 5 capstone post page. | No | |
| 2 | Complete the README | Finish `README.md` from the framework template: purpose, requirements, `.venv` steps, run, test, Doxygen, a screenshot per lecture step, and a link to the wiki. Check it with the framework's README check script. | No | |
| 3 | Write the English wiki | Create `docs/wiki/` pages (Home, one page per lecture step, Run and test) that show the step's screenshot and explain what was gained: Jinja `for` and `if`, `url_for`, URL parameters, route variables. | No | |
| 4 | Write the Danish wiki | Translate every English page to Danish as `<Page>-da.md`, keeping code, commands and file names in English. | No | |
| 5 | Write the Bahasa Malaysia wiki | Translate every English page to Bahasa Malaysia as `<Page>-ms.md`, keeping code, commands and file names in English. | No | |
| 6 | Add the wiki sidebar and review the wiki | Add `_Sidebar.md` in the shape `wiki.md` requires (one English page list, Languages section) and review the wiki against `QC-WIKI-001`. | No | |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-templating-app.md
[RC-006]: ./../sqa/reviews/rc-006-mil-003.md
[5fefc13]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/commit/5fefc139d1df1e190ba76b4efb57489eaed0c1c4
