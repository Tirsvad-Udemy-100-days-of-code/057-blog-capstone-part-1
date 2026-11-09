"""@brief Tests for the Flask app through its test client."""

import pytest
from flask.testing import FlaskClient

from blog_capstone.domain.post import Post
from blog_capstone.presentation.app import create_app
from tests.conftest import FakePostSource


def make_client(source: FakePostSource) -> FlaskClient:
    """@brief Build a test client for a source.

    @param source Fake post source.
    @return A Flask test client.
    """
    return create_app(source).test_client()


def test_home_lists_every_post_with_read_link(posts: list[Post]) -> None:
    """@brief Home shows title, subtitle and a Read link per post.

    @param posts Sample posts.
    @return None
    """
    response = make_client(FakePostSource(posts)).get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    for post in posts:
        assert post.title in html
        assert post.subtitle in html
        assert f'<a href="/post/{post.id}">Read</a>' in html
    assert 'href="/blog/1"' in html
    assert "/static/css/styles.css" in html


def test_get_blog_lists_posts(posts: list[Post]) -> None:
    """@brief The blog page lists every title and subtitle.

    @param posts Sample posts.
    @return None
    """
    response = make_client(FakePostSource(posts)).get("/blog/7")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert all(post.title in html and post.subtitle in html for post in posts)
    assert "No posts yet." not in html


def test_get_blog_logs_captured_number(
    posts: list[Post], caplog: pytest.LogCaptureFixture
) -> None:
    """@brief The captured num is logged.

    @param posts Sample posts.
    @param caplog Log capture.
    @return None
    """
    with caplog.at_level("INFO"):
        make_client(FakePostSource(posts)).get("/blog/7")
    assert "num=7" in caplog.text


def test_get_blog_shows_message_for_empty_source() -> None:
    """@brief An empty source shows the empty message.

    @return None
    """
    response = make_client(FakePostSource([])).get("/blog/1")
    assert "No posts yet." in response.get_data(as_text=True)


def test_show_post_displays_title_subtitle_and_body(posts: list[Post]) -> None:
    """@brief A post page shows all three texts, including non-ASCII.

    @param posts Sample posts.
    @return None
    """
    response = make_client(FakePostSource(posts)).get("/post/2")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert posts[1].title in html
    assert posts[1].subtitle in html
    assert posts[1].body in html


def test_show_post_returns_404_for_unknown_id(posts: list[Post]) -> None:
    """@brief An unknown id gives a friendly 404 page.

    @param posts Sample posts.
    @return None
    """
    response = make_client(FakePostSource(posts)).get("/post/99")
    assert response.status_code == 404
    assert "could not find" in response.get_data(as_text=True)


@pytest.mark.parametrize("path", ["/", "/blog/1", "/post/1"])
def test_unavailable_source_returns_503(path: str) -> None:
    """@brief A failing source gives a 503 error page on every route.

    @param path Route to call.
    @return None
    """
    response = make_client(FakePostSource([], is_unavailable=True)).get(path)
    assert response.status_code == 503
    assert "unavailable" in response.get_data(as_text=True)
