"""@brief Flask delivery layer for the blog."""

import logging

from flask import Flask, render_template

from blog_capstone.application.ports.post_source import PostSource
from blog_capstone.application.use_cases.blog import get_post, list_posts
from blog_capstone.domain.errors import PostNotFoundError, PostSourceUnavailableError

logger = logging.getLogger(__name__)

HTTP_NOT_FOUND = 404
HTTP_SERVICE_UNAVAILABLE = 503


class BlogViews:
    """@brief The pages of the blog; one method per route of the assignment."""

    def __init__(self, post_source: PostSource) -> None:
        """@brief Create the views.

        @param post_source Where the posts come from.
        @return None
        """
        self._post_source = post_source

    def home(self) -> str:
        """@brief Home page: title, subtitle and a Read link for every post.

        @return The rendered HTML page.
        """
        return render_template("index.html", posts=list_posts(self._post_source))

    def get_blog(self, num: int) -> str:
        """@brief Blog page of the lecture: logs the captured URL parameter.

        @param num Number captured from the URL.
        @return The rendered HTML page.
        """
        logger.info("Blog page requested with num=%d", num)
        return render_template(
            "blog.html", posts=list_posts(self._post_source), num=num
        )

    def show_post(self, blog_id: int) -> str:
        """@brief Show one post with title, subtitle and body.

        @param blog_id Identifier of the post, taken from the URL.
        @return The rendered HTML page.
        """
        return render_template("post.html", post=get_post(self._post_source, blog_id))


def handle_not_found(_error: PostNotFoundError) -> tuple[str, int]:
    """@brief Friendly page for an unknown post.

    @param _error The raised error.
    @return The error page and the status code 404.
    """
    message = "We could not find that post."
    return render_template("error.html", message=message), HTTP_NOT_FOUND


def handle_unavailable(error: PostSourceUnavailableError) -> tuple[str, int]:
    """@brief Friendly page when the posts cannot be fetched.

    @param error The raised error; its cause is logged here, where it is handled.
    @return The error page and the status code 503.
    """
    logger.warning("Posts are unavailable: %s (cause: %r)", error, error.__cause__)
    message = "The posts are unavailable. Please try again later."
    return render_template("error.html", message=message), HTTP_SERVICE_UNAVAILABLE


def create_app(post_source: PostSource) -> Flask:
    """@brief Build the Flask app around a post source.

    @param post_source Where the posts come from.
    @return The configured Flask app.
    """
    app = Flask(__name__)
    views = BlogViews(post_source)
    app.add_url_rule("/", "home", views.home)
    app.add_url_rule("/blog/<int:num>", "get_blog", views.get_blog)
    app.add_url_rule("/post/<int:blog_id>", "show_post", views.show_post)
    app.register_error_handler(PostNotFoundError, handle_not_found)
    app.register_error_handler(PostSourceUnavailableError, handle_unavailable)
    return app
