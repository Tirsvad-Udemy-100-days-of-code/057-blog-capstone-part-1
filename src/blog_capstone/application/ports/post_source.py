"""@brief Port for reading blog posts from outside the application."""

from typing import Protocol

from blog_capstone.domain.post import Post


class PostSource(Protocol):
    """@brief Supplies the blog posts."""

    def fetch_posts(self) -> list[Post]:
        """@brief Read every post.

        @return All posts in source order.
        @throws PostSourceUnavailableError When the posts cannot be read.
        """
        ...
