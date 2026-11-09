# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [9eacf46] |

---

## Artifact Under Review

- Instance reviewed: [WIKI-001]
- Checklist used: [QC-WIKI-001]
- Scope: full review of docs/wiki (7 English pages, 7 Danish, 7 Bahasa Malaysia, sidebar)
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | _Sidebar.md exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, one English page list, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All seven English pages are listed; a script checked that every internal link in every page resolves to an existing file. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so it has no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages section is last: English, Dansk, Bahasa Malaysia, each linking to its Home page. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English plus Danish and Bahasa Malaysia; the registry names English as PO language and lists da and ms as extra wiki languages. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Seven pages in each language; a script compared the page sets. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | First line of every page names the current language in bold and links to the others; checked by script. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Home-da.md and Home-ms.md style names, BCP 47 codes. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | A script confirmed the code blocks and URLs are identical to the English pages; commands and identifiers stay in English. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The published wiki does not exist until this change is merged; it is checked after the merge and this record is then updated. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional; no layout rules are changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All 22 files are directly in docs/wiki/. |

## Overall Verdict

Go-with-conditions — no Mandatory criterion fails; criterion 14 is Pending until the wiki is published. The condition is closed by a delta re-review after the merge. Autonomous mode: AI as stand-in for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the published wiki, sidebar and links after the merge and record a delta re-review for criterion 14 | S01 | 2026-11-13 |

---
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[WIKI-001]: ../../wiki/
[9eacf46]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/commit/9eacf463ce13f1309ed1c414e4092b5b757c8b1d
