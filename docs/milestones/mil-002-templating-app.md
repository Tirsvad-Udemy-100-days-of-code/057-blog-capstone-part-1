# MIL-002 Templating app

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [5fefc13] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted after [RC-005] (autonomous, not independent) | [5fefc13] |

---

## Purpose

Decide whether the Flask application meets the Day 57 assignment: a styled home page listing all posts with a "Read" link, and a page per post at `/post/<blog_id>`.

## Deliverable

The Flask application in `src/` with Jinja templates and static assets, and a pytest suite in `tests/` that runs without network access.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /` returns 200 and shows the title and subtitle of every post of the (stubbed) API response, each with a "Read" link to `/post/<id>` | Yes | Any post missing |
| 2 | `GET /post/<id>` shows title, subtitle and body of that post | Yes | Any part missing |
| 3 | `GET /post/<unknown id>` returns 404 | Yes | Other status |
| 4 | The API address is in `src/constants.py`; tests make no network call | Yes | Hard-coded address or network call |
| 5 | Route function names follow the assignment (`home`, `get_blog`, `show_post`) | Yes | Different names |
| 6 | The source has Doxygen comments and is reviewed against `qc-programming-python.md` with a `Go` | Go | No-Go |
| 7 | `python -m pytest` passes | 0 failures | Any failure |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs the project skeleton, configuration and environment |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2, 3 and 4; success criteria 1, 2, 3 and 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — inside the one-week window of the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Obtain the starter files | Download the course's starting files archive named in the brief into a separate empty folder, inspect it as untrusted data, and copy only the static assets and templates the project needs into `src/`. If the link has expired, rebuild the templates and record the gap in the Project Plan's Open Issues. | No | |
| 2 | Fetch blog posts from the API | Add a small gateway function that reads the posts from the n:Point JSON bin with `requests`; the address is a constant in `constants.py`. Tests replace the gateway with a stub so no network is used. | No | |
| 3 | List all posts on the home page | Route `home` fetches the posts and passes them to `index.html`; a Jinja `for` loop renders each title and subtitle (lecture "Multiline Statements with Jinja"). | No | |
| 4 | Link each post with url_for | Add a "Read" anchor to each preview with `url_for('show_post', blog_id=post.id)` so it points to `/post/<blog_id>` (lecture "URL building"). | No | |
| 5 | Show one post at /post/<blog_id> | Route `show_post` takes `blog_id` from the URL, finds the post and renders title, subtitle and body in `post.html`; an unknown id returns 404. Include the lecture's `get_blog` route, which prints the captured URL parameter. | No | |
| 6 | Write pytest tests | Test the home page, the post page, the 404 and the gateway with a stubbed response and a JSON fixture in `tests/`. | No | |
| 7 | Review the code against the Python checklist | Add Doxygen comments, run the framework's Python QC checklist and record the `RC-*` review. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-setup-and-repository.md
[RC-005]: ./../sqa/reviews/rc-005-mil-002.md
[5fefc13]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/057-blog-capstone-part-1/commit/5fefc139d1df1e190ba76b4efb57489eaed0c1c4
