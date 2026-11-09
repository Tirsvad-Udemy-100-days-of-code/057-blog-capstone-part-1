# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [5fefc13] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after [RC-002] (autonomous, not independent) | [5fefc13] |

---

## Purpose

Identify who the project serves, what each stakeholder needs and how they are informed, using the Power/Interest grid (Manage Closely, Keep Satisfied, Keep Informed, Monitor). It feeds the Business Case [BC-001] and the Project Plan.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A finished, correct and well-documented assignment |
| S02 | Udemy course participants | Fellow learners who share code and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear description, topics and README, and no unnecessary runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact.
- **Keep Informed (S02):** cannot change the project but reads and reuses its output; the README and wiki are the channel.
- **Monitor (S03):** casual interest; the repository description, topics and README are enough.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The home page and the post page behave as the assignment describes | Functionality |
| CN-002 | S01 | Changes are reviewed and tracked step by step through branches and pull requests | Supportability |
| CN-003 | S02 | Code is readable and keeps the assignment's function names | Usability |
| CN-004 | S02 | The README explains how to create `.venv`, install, run and test | Usability |
| CN-005 | S02 | The wiki explains what each lecture step teaches, in English, Danish and Bahasa Malaysia | Usability |
| CN-006 | S03 | A clear repository description, topics and README | Usability |
| CN-007 | S03 | No runtime dependencies beyond the necessary ones | Implementation |
| CN-008 | S01 | Tests run offline and quickly | Reliability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Chat with S01 | Per run | Plan acceptance and the end-of-run summary | All milestones |
| CM-002 | Pull request | Per milestone | Reviewable change with `Closes #N` lines | All milestones |
| CM-003 | README and wiki | At the documentation milestone | Run instructions, screenshots, lecture explanations | Documentation |
| CM-004 | Repository description and topics | Once | Short description and topics on the git host | Setup |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no dependencies; the assignment needs Flask and requests | S03, S01 | Only Flask and requests at runtime; pytest is a development dependency only |
| S02 wants the assignment's function names; clean layering would rename things | S02, S01 | Keep the assignment's route function names in the presentation layer |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objectives 1 and 2 [BC-001] |
| S01 | CN-002, CN-008 | Objective 4 [BC-001] |
| S02 | CN-003 | Objective 3 [BC-001] |
| S02 | CN-004 | Objective 5 [BC-001] |
| S02 | CN-005 | Objective 6 [BC-001] |
| S03 | CN-006 | Objective 7 [BC-001] |
| S03 | CN-007 | Objective 5 and the dependency constraint [BC-001] |

## Sign-Off

| Stakeholder | Role | Decision |
| --- | --- | --- |
| S01 | Product Owner and reviewer | Accepted by AI as stand-in for S01 |

---

[BC-001]: ./business-case.md
[RC-002]: ./sqa/reviews/rc-002-stakeholder-analysis.md
[5fefc13]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/commit/5fefc139d1df1e190ba76b4efb57489eaed0c1c4
