"""@brief Smoke tests for the package and its constants."""

import importlib

from blog_capstone import constants

MAX_PORT = 65535


def test_package_is_importable() -> None:
    """@brief The package imports.

    @return None
    """
    assert importlib.import_module("blog_capstone") is not None


def test_constants_have_expected_types() -> None:
    """@brief Each constant has its documented type.

    @return None
    """
    assert isinstance(constants.APP_NAME, str)
    assert isinstance(constants.POSTS_API_URL, str)
    assert isinstance(constants.REQUEST_TIMEOUT_SECONDS, int)
    assert isinstance(constants.DEFAULT_HOST, str)
    assert isinstance(constants.DEFAULT_PORT, int)


def test_request_timeout_is_positive() -> None:
    """@brief The timeout is above zero.

    @return None
    """
    assert constants.REQUEST_TIMEOUT_SECONDS > 0


def test_default_port_is_in_valid_range() -> None:
    """@brief The port is a valid TCP port.

    @return None
    """
    assert 0 < constants.DEFAULT_PORT <= MAX_PORT
