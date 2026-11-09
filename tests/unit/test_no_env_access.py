"""@brief Guard: no test imports or reads a .env file."""

from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parents[1]
FORBIDDEN = ("dotenv", ".env")


def test_no_test_imports_or_reads_env_file() -> None:
    """@brief No test file mentions dotenv or the .env file.

    @return None
    """
    this_file = Path(__file__).resolve()
    offenders = [
        path.name
        for path in TESTS_DIR.rglob("*.py")
        if path.resolve() != this_file
        and any(word in path.read_text(encoding="utf-8") for word in FORBIDDEN)
    ]
    assert offenders == []
