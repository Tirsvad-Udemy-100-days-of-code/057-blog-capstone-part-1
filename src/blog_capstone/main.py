"""@brief Composition root: wires the adapters into the app."""

from flask import Flask

from blog_capstone.constants import POSTS_API_URL, REQUEST_TIMEOUT_SECONDS
from blog_capstone.infrastructure.api_post_source import ApiPostSource
from blog_capstone.presentation.app import create_app


def build_app() -> Flask:
    """@brief Create the app with the real API post source.

    @return The ready Flask app.
    """
    source = ApiPostSource(POSTS_API_URL, REQUEST_TIMEOUT_SECONDS)
    return create_app(source)
