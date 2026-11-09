"""@brief Tests for ApiPostSource with a fake requests session (no network)."""

from typing import Any

import pytest
import requests

from blog_capstone.domain.errors import PostSourceUnavailableError
from blog_capstone.domain.post import Post
from blog_capstone.infrastructure.api_post_source import ApiPostSource

URL = "https://example.invalid/posts"
TIMEOUT = 3


class FakeResponse:
    """@brief Minimal stand-in for requests.Response."""

    def __init__(self, payload: Any = None, *, status: int = 200, bad_json: bool = False) -> None:
        self._payload = payload
        self._status = status
        self._bad_json = bad_json

    def raise_for_status(self) -> None:
        """@brief Raise HTTPError for 4xx and 5xx."""
        if self._status >= 400:
            raise requests.HTTPError(f"status {self._status}")

    def json(self) -> Any:
        """@brief Return the payload or fail like invalid JSON."""
        if self._bad_json:
            raise requests.JSONDecodeError("bad", "doc", 0)
        return self._payload


class FakeSession(requests.Session):
    """@brief Session returning a canned response or raising an error."""

    def __init__(self, response: FakeResponse | None = None, error: Exception | None = None) -> None:
        super().__init__()
        self._response = response
        self._error = error
        self.calls: list[tuple[str, Any]] = []

    def get(self, url: str, **kwargs: Any) -> Any:  # noqa: ANN401
        """@brief Record the call and answer."""
        self.calls.append((url, kwargs.get("timeout")))
        if self._error is not None:
            raise self._error
        return self._response


def test_fetch_posts_parses_payload(
    posts_payload: list[dict[str, object]], posts: list[Post]
) -> None:
    """@brief A valid payload becomes posts, with URL and timeout used.

    @param posts_payload Raw JSON data.
    @param posts Expected posts.
    @return None
    """
    session = FakeSession(FakeResponse(posts_payload))
    assert ApiPostSource(URL, TIMEOUT, session).fetch_posts() == posts
    assert session.calls == [(URL, TIMEOUT)]


def test_fetch_posts_raises_on_http_error() -> None:
    """@brief An HTTP error status becomes PostSourceUnavailableError.

    @return None
    """
    session = FakeSession(FakeResponse([], status=500))
    with pytest.raises(PostSourceUnavailableError) as info:
        ApiPostSource(URL, TIMEOUT, session).fetch_posts()
    assert isinstance(info.value.__cause__, requests.HTTPError)


def test_fetch_posts_raises_on_invalid_json() -> None:
    """@brief A body that is not JSON becomes PostSourceUnavailableError.

    @return None
    """
    session = FakeSession(FakeResponse(bad_json=True))
    with pytest.raises(PostSourceUnavailableError):
        ApiPostSource(URL, TIMEOUT, session).fetch_posts()


@pytest.mark.parametrize(
    "payload",
    [
        {"id": 1},
        [{"id": 1, "title": "T"}],
        [{"id": "1", "title": "T", "subtitle": "S", "body": "B"}],
        ["not an object"],
    ],
)
def test_fetch_posts_raises_on_wrong_shape(payload: object) -> None:
    """@brief JSON of the wrong shape becomes PostSourceUnavailableError.

    @param payload Bad JSON data.
    @return None
    """
    session = FakeSession(FakeResponse(payload))
    with pytest.raises(PostSourceUnavailableError):
        ApiPostSource(URL, TIMEOUT, session).fetch_posts()


def test_fetch_posts_raises_on_timeout() -> None:
    """@brief A timeout becomes PostSourceUnavailableError.

    @return None
    """
    session = FakeSession(error=requests.Timeout("slow"))
    with pytest.raises(PostSourceUnavailableError) as info:
        ApiPostSource(URL, TIMEOUT, session).fetch_posts()
    assert isinstance(info.value.__cause__, requests.Timeout)
