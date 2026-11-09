"""@brief The Post entity of the blog."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Post:
    """@brief One blog post.

    @param id Unique number of the post.
    @param title Headline of the post.
    @param subtitle Short teaser text of the post.
    @param body Full text of the post.
    """

    id: int
    title: str
    subtitle: str
    body: str
