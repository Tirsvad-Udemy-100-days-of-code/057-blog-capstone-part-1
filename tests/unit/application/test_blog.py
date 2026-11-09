"""@brief Tests for the blog use cases."""

import pytest

from blog_capstone.application.use_cases.blog import get_post, list_posts
from blog_capstone.domain.errors import PostNotFoundError, PostSourceUnavailableError
from blog_capstone.domain.post import Post
from tests.conftest import FakePostSource


def test_list_posts_returns_every_post(posts: list[Post]) -> None:
    """@brief All posts of the source are listed.

    @param posts Sample posts.
    @return None
    """
    assert list_posts(FakePostSource(posts)) == posts


def test_list_posts_returns_empty_list_for_empty_source() -> None:
    """@brief An empty source gives an empty list.

    @return None
    """
    assert list_posts(FakePostSource([])) == []


def test_get_post_returns_matching_post(posts: list[Post]) -> None:
    """@brief The post with the id is returned.

    @param posts Sample posts.
    @return None
    """
    assert get_post(FakePostSource(posts), 2) == posts[1]


def test_get_post_raises_for_unknown_id(posts: list[Post]) -> None:
    """@brief An unknown id raises PostNotFoundError.

    @param posts Sample posts.
    @return None
    """
    with pytest.raises(PostNotFoundError):
        get_post(FakePostSource(posts), 99)


def test_get_post_propagates_unavailable_source() -> None:
    """@brief A failing source error is not hidden.

    @return None
    """
    with pytest.raises(PostSourceUnavailableError):
        get_post(FakePostSource([], is_unavailable=True), 1)
