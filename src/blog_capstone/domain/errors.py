"""@brief Errors raised by the blog rules and ports."""


class PostNotFoundError(Exception):
    """@brief Raised when no post has the requested id."""


class PostSourceUnavailableError(Exception):
    """@brief Raised when the posts cannot be read from their source."""
