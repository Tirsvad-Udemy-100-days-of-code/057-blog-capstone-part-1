"""@brief Runs the development server with python -m blog_capstone."""

import logging

from blog_capstone.constants import DEFAULT_HOST, DEFAULT_PORT
from blog_capstone.main import build_app


def run() -> None:
    """@brief Start the Flask development server.

    @return None
    """
    logging.basicConfig(level=logging.INFO)
    build_app().run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=True)


if __name__ == "__main__":
    run()
