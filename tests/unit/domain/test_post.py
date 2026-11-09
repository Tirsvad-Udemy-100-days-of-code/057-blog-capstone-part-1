"""@brief Tests for the Post entity."""

import dataclasses

import pytest

from blog_capstone.domain.post import Post


def test_post_holds_its_fields() -> None:
    """@brief A post keeps what it was built with.

    @return None
    """
    post = Post(id=1, title="T", subtitle="S", body="B")
    assert (post.id, post.title, post.subtitle, post.body) == (1, "T", "S", "B")


def test_post_is_immutable() -> None:
    """@brief A post cannot be changed.

    @return None
    """
    post = Post(id=1, title="T", subtitle="S", body="B")
    with pytest.raises(dataclasses.FrozenInstanceError):
        post.title = "X"  # type: ignore[misc]


def test_posts_with_same_values_are_equal() -> None:
    """@brief Posts compare by value.

    @return None
    """
    assert Post(1, "T", "S", "B") == Post(1, "T", "S", "B")
