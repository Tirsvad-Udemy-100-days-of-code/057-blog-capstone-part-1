# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [5fefc13] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-09, end 2026-11-13, constraint from BC-001. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Three gateways, each with its MIL document, decision date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates 11-10, 11-12 and 11-13 equal the MIL target dates and lie in the window. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope coverage table maps every In Scope item to a MIL. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-002 to MIL-003, acyclic and in schedule order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | A No-Go moves later phases; only S01 moves the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | N-A | No governance document (GOV) exists in this project; owners use SA IDs (S01). |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions carry their source; no re-baseline yet. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Three plan risks with mitigation, traced to BC risks. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open issues are current and do not contradict the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Deliverables match the MIL Deliverable sections. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column states none (technical tasks). |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars match the table; chain matches the dependency list. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Marked not yet synced. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Single plan, Version History kept. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Language en, Domain it. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | Valid codes. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | IT Executive English. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary exists; terms consistent. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | English keys and headings. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No twin. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 reads English and knows the domain; AI as stand-in. Not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Terms defined. |

## Overall Verdict

Go — all applicable criteria pass; criterion 7 is N-A because no governance document exists. Autonomous mode: AI as stand-in for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None open | S01 | — |

---
[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[5fefc13]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/commit/5fefc139d1df1e190ba76b4efb57489eaed0c1c4
