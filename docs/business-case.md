# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [5fefc13] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after [RC-001] (autonomous, not independent) | [5fefc13] |

---

## Executive Summary

Day 57 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" asks the participant to build "Blog Capstone Project Part 1 - Templating": a small Flask website that fetches blog posts from a JSON API, lists every title and subtitle on the home page, and shows each full post at `/post/<blog_id>`. The project delivers that assignment as a clean, tested, documented Python repository with a README and a three-language wiki (English, Danish, Bahasa Malaysia), so other course participants can read, run and compare it and GitHub viewers can browse it for ideas.

## Methodological and Standards Foundation

The work follows the SQA and QC framework mounted at `framework/`: Business Case, Stakeholder Analysis, Project Plan, milestones and tasks, then code, each step reviewed before the next. Quality characteristics are tagged with ISO/IEC 25010:2023. Source code follows the `coding-conventions` Python rules and the Clean Architecture folder structure (`src/`, `tests/`, `docs/`).

## Problem Statement

The course assignment is delivered as a loose set of starter files and a lecture video. Solutions shared between participants are often untested, undocumented and hard to run, and they do not explain what each lecture step teaches. A participant who wants to compare solutions or learn Jinja templating (`for`, `if`, `url_for`, URL parameters) has no readable, reproducible reference.

## Business Opportunity

A small, well-structured reference solution with a screenshot per lecture step and a wiki that explains what was learned serves two audiences at once: course participants who compare solutions (S02) and repository viewers who look for ideas (S03). It also trains the Product Owner (S01) in the framework's plan-first workflow on a small, safe project.

## Objectives

1. Deliver the assignment: the home page lists the title and subtitle of every post fetched from the blog API, each with a "Read" link.
2. Deliver `/post/<blog_id>`, which shows the title, subtitle and body of one post.
3. Keep the assignment's function names so participants can compare solutions.
4. Provide automated pytest tests that run without network access.
5. Document how to create and use a local `.venv`, run the app and run the tests.
6. Publish a README and a wiki in English, Danish and Bahasa Malaysia, each with a screenshot for every lecture step and an explanation of what the step teaches.
7. Publish the repository with a description and topics.

## Scope

### In Scope

- Flask application in `src/`, Jinja templates and static assets from the starter files, constants in `constants.py`.
- Tests in `tests/` with pytest.
- `pyproject.toml`, Python `.gitignore`, `Doxyfile`, Doxygen comments in the source.
- README from the framework template; wiki in `docs/wiki/` in `en`, `da` and `ms`.
- Screenshots of each lecture step, taken in a Docker container.
- Repository description and topics on the git host.

### Out of Scope

- Features beyond the assignment (database, authentication, editing posts, deployment).
- Later course days (Day 58 onward).
- Hosting the application.
- Using the `.env` file in the project: the tokens are for the Product Owner's and the agent's tooling only and are never read by, imported into or committed with the project.

## Expected Benefits

### Tangible Benefits

- A runnable solution with passing tests and documented run steps.
- A README and a wiki in three languages with a screenshot per lecture step.

### Intangible Benefits

- A reference other participants can learn from.
- Practice with the plan-first framework workflow.

## Strategic Alignment

The project supports the Product Owner's learning goal in the bootcamp and the goal of keeping a public, reviewable portfolio of course work under the `Tirsvad-Udemy-100-days-of-code` organisation.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Home page shows all posts | Every post from the API has its title and subtitle and a "Read" link | Test with a stubbed API response; screenshot |
| 2 | Post page works | `/post/<id>` shows title, subtitle and body; an unknown id gives 404 | pytest |
| 3 | Tests pass offline | 0 failures, 0 network calls | `python -m pytest` |
| 4 | Run steps work from a clean clone | `.venv` created, dependencies installed and app started in 5 steps or fewer | README walk-through checked in a container |
| 5 | Documentation languages | README (en); wiki pages in en, da and ms with the same page set | `framework/scripts/check-languages.sh` and page list |
| 6 | Screenshots | One screenshot per lecture step in the README and in every wiki language | File list under `docs/images/` |
| 7 | Runtime dependencies | Only Flask and requests | `pyproject.toml` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The blog API (n:Point bin) is offline or changed | The app shows no posts; screenshots cannot be taken | Keep the API URL in `constants.py`; fetch through one function so tests stub it; keep a sample JSON fixture in `tests/` |
| The signed starter-file URLs have expired | Templates and static assets are not available | Rebuild the templates from the lecture description; record the gap as an open issue |
| Screenshots on the host desktop take the user's mouse and keyboard | Disturbs the user, breaks `gui-testing.md` | Take all screenshots in a Docker container |
| Danish and Bahasa Malaysia translations are inaccurate | Misleading wiki text | English is authoritative; translations follow it page by page and are reviewed against it |
| A token leaks into the repository | Credential exposure | `.env` is in `.gitignore`, is never read by project code, and no token is printed |

## Assumptions

- S01 is Product Owner, developer and reviewer; the AI acts as stand-in reviewer in autonomous mode, recorded as such in each `RC-*`.
- The Product Owner's language is English and the domain is IT.
- The repository `Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1` already exists on `git.tirsystem.com`.
- "Python greater than 3.13" is read as Python 3.13 or newer (`requires-python = ">=3.13"`).
- The people the project is for (S02, S03) are not contacted; their needs are taken from the Product Owner's brief.

## Constraints

- Python 3.13 or newer, `venv` for the environment, pytest for tests, constants in `constants.py`, configuration in `pyproject.toml`.
- Source uses Doxygen comments; a `Doxyfile` is provided.
- Folders `src/`, `tests/`, `docs/`.
- Runtime dependencies kept to the minimum needed.
- One branch and pull request per milestone; no code before its milestone is accepted.
- Target duration: one week, 2026-11-09 to 2026-11-13 (assumed; the brief gives none).

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one week of part-time effort by S01 and the AI; no licence or hosting cost | A reusable reference solution, a documented workflow and a public portfolio item. The benefit is qualitative, justified by the learning goal. |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a finished, reviewed assignment |
| S02 | Udemy participants; want readable, runnable code with the assignment's function names and run instructions |
| S03 | GitHub viewers; want a clear description, topics and README, and few dependencies |

## Recommendation

Proceed — the scope is small, the risks have mitigations and the result serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[RC-001]: ./sqa/reviews/rc-001-business-case.md
[5fefc13]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/commit/5fefc139d1df1e190ba76b4efb57489eaed0c1c4
