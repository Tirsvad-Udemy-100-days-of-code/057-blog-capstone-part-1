"""@brief Flask delivery layer for the blog."""

import logging

from flask import Flask, render_template

from blog_capstone.application.ports.post_source import PostSource
from blog_capstone.application.use_cases.blog import get_post, list_posts
from blog_capstone.domain.errors import PostNotFoundError, PostSourceUnavailableError

logger = logging.getLogger(__name__)

HTTP_NOT_FOUND = 404
HTTP_SERVICE_UNAVAILABLE = 503


def create_app(post_source: PostSource) -> Flask:
    """@brief Build the Flask app around a post source.

    @param post_source Where the posts come from.
    @return The configured Flask app.
    """
    app = Flask(__name__)

    @app.route("/")
    def home() -> str:
        """@brief Home page: title, subtitle and a Read link for every post.

        @return The rendered HTML page.
        """
        return render_template("index.html", posts=list_posts(post_source))

    @app.route("/blog/<int:num>")
    def get_blog(num: int) -> str:
        """@brief Blog page of the lecture: logs the captured URL parameter.

        @param num Number captured from the URL.
        @return The rendered HTML page.
        """
        logger.info("Blog page requested with num=%d", num)
        return render_template("blog.html", posts=list_posts(post_source), num=num)

    @app.route("/post/<int:blog_id>")
    def show_post(blog_id: int) -> str:
        """@brief Show one post with title, subtitle and body.

        @param blog_id Identifier of the post, taken from the URL.
        @return The rendered HTML page.
        """
        return render_template("post.html", post=get_post(post_source, blog_id))

    @app.errorhandler(PostNotFoundError)
    def handle_not_found(_error: PostNotFoundError) -> tuple[str, int]:
        message = "We could not find that post."
        return render_template("error.html", message=message), HTTP_NOT_FOUND

    @app.errorhandler(PostSourceUnavailableError)
    def handle_unavailable(_error: PostSourceUnavailableError) -> tuple[str, int]:
        message = "The posts are unavailable. Please try again later."
        return render_template("error.html", message=message), HTTP_SERVICE_UNAVAILABLE

    return app
