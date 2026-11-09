"""@brief Use cases for reading the blog."""

from blog_capstone.application.ports.post_source import PostSource
from blog_capstone.domain.errors import PostNotFoundError
from blog_capstone.domain.post import Post


def list_posts(source: PostSource) -> list[Post]:
    """@brief List every post.

    @param source Where the posts come from.
    @return All posts.
    """
    return source.fetch_posts()


def get_post(source: PostSource, blog_id: int) -> Post:
    """@brief Find one post by its id.

    @param source Where the posts come from.
    @param blog_id Id of the wanted post.
    @return The matching post.
    @throws PostNotFoundError When no post has that id.
    """
    for post in source.fetch_posts():
        if post.id == blog_id:
            return post
    raise PostNotFoundError(f"No post with id {blog_id}")
