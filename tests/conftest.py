"""@brief Shared fixtures and fakes for the tests."""

import json
from pathlib import Path

import pytest

from blog_capstone.domain.errors import PostSourceUnavailableError
from blog_capstone.domain.post import Post

FIXTURES_DIR = Path(__file__).parent / "fixtures"


class FakePostSource:
    """@brief In-memory PostSource, optionally failing."""

    def __init__(self, posts: list[Post], *, is_unavailable: bool = False) -> None:
        self._posts = posts
        self._is_unavailable = is_unavailable

    def fetch_posts(self) -> list[Post]:
        """@brief Return the stored posts or raise when unavailable.

        @return The stored posts.
        """
        if self._is_unavailable:
            raise PostSourceUnavailableError("fake source is down")
        return list(self._posts)


@pytest.fixture
def posts_payload() -> list[dict[str, object]]:
    """@brief Raw JSON data of the sample posts.

    @return The parsed fixture file.
    """
    text = (FIXTURES_DIR / "posts.json").read_text(encoding="utf-8")
    return json.loads(text)  # type: ignore[no-any-return]


@pytest.fixture
def posts(posts_payload: list[dict[str, object]]) -> list[Post]:
    """@brief The sample posts as domain objects.

    @param posts_payload Raw JSON data.
    @return Three posts.
    """
    return [Post(**item) for item in posts_payload]  # type: ignore[arg-type]
