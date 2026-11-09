"""@brief Post source that reads a JSON API over HTTP."""

import requests

from blog_capstone.domain.errors import PostSourceUnavailableError
from blog_capstone.domain.post import Post


class ApiPostSource:
    """@brief Reads posts from a JSON list served by an HTTP endpoint."""

    def __init__(
        self,
        url: str,
        timeout_seconds: float,
        session: requests.Session | None = None,
    ) -> None:
        """@brief Create the source.

        @param url Endpoint that returns the JSON list of posts.
        @param timeout_seconds Timeout of the request in seconds.
        @param session HTTP session to use; a new one is made per call when None.
        @return None
        """
        self._url = url
        self._timeout_seconds = timeout_seconds
        self._session = session

    def fetch_posts(self) -> list[Post]:
        """@brief Download and parse the posts.

        @return All posts in the order the API gives them.
        @throws PostSourceUnavailableError On network, HTTP, JSON or shape errors.
        """
        try:
            if self._session is not None:
                payload = self._get_json(self._session)
            else:
                with requests.Session() as session:
                    payload = self._get_json(session)
            return [self._to_post(item) for item in payload]
        except requests.RequestException as error:
            raise PostSourceUnavailableError("Posts API request failed") from error
        except (ValueError, KeyError, TypeError) as error:
            raise PostSourceUnavailableError("Posts API returned bad data") from error

    def _get_json(self, session: requests.Session) -> list[dict[str, object]]:
        response = session.get(self._url, timeout=self._timeout_seconds)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, list):
            raise TypeError("Expected a JSON list of posts")
        return payload

    @staticmethod
    def _to_post(item: dict[str, object]) -> Post:
        post_id, title, subtitle, body = (
            item["id"],
            item["title"],
            item["subtitle"],
            item["body"],
        )
        if (
            not isinstance(post_id, int)
            or not isinstance(title, str)
            or not isinstance(subtitle, str)
            or not isinstance(body, str)
        ):
            raise TypeError("Post fields have the wrong type")
        return Post(id=post_id, title=title, subtitle=subtitle, body=body)
