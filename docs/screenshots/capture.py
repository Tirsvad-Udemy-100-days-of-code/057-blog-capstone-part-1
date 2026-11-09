"""@brief Take one screenshot per lecture step with a headless browser.

Runs inside the Docker container started by run.sh, never on the host desktop.
Output folder: the first argument (default /out).
"""

import sys
import threading
from pathlib import Path

from flask import Flask
from playwright.sync_api import Page, sync_playwright
from werkzeug.serving import BaseWSGIServer, make_server

from blog_capstone.domain.post import Post
from blog_capstone.main import build_app
from blog_capstone.presentation.app import create_app

HOST = "127.0.0.1"
STARTER_PORT = 5001
REAL_PORT = 5000
VIEWPORT = {"width": 1100, "height": 1250}


class StarterPosts:
    """@brief The two placeholder cards of the course's starter files."""

    def fetch_posts(self) -> list[Post]:
        """@brief Return the starter site's placeholder posts.

        @return Two posts with the starter's lorem ipsum text.
        """
        return [
            Post(1, "Just a blog post", "Lorem ipsum dolor sit ", "Lorem ipsum"),
            Post(2, "Another blog post", "Lorem ipsum dolor sit ", "Lorem ipsum"),
        ]


def serve(app: Flask, port: int) -> BaseWSGIServer:
    """@brief Start a Flask app in a background thread.

    @param app The Flask app.
    @param port Port to listen on.
    @return The server, so the caller can shut it down.
    """
    server = make_server(HOST, port, app)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def shot(page: Page, url: str, target: Path) -> None:
    """@brief Open a page, label it with its path and save a screenshot.

    @param page Playwright page.
    @param url Address to open.
    @param target PNG file to write.
    @return None
    """
    page.goto(url)
    page.evaluate(
        """() => { const b = document.createElement('div');
        b.textContent = 'URL path: ' + location.pathname;
        b.style.cssText = 'position:fixed;top:8px;right:8px;background:#212121;color:#fff;'
          + 'padding:6px 12px;border-radius:4px;font:14px monospace;z-index:9';
        document.body.appendChild(b); }"""
    )
    page.screenshot(path=str(target), full_page=False)


def main() -> None:
    """@brief Take the five screenshots.

    @return None
    """
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "/out")
    out.mkdir(parents=True, exist_ok=True)
    starter = serve(create_app(StarterPosts()), STARTER_PORT)
    real = serve(build_app(), REAL_PORT)
    base = f"http://{HOST}:{REAL_PORT}"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        shot(page, f"http://{HOST}:{STARTER_PORT}/", out / "step-1-starter-site.png")
        shot(page, f"{base}/blog/1", out / "step-2-blog-for-loop.png")
        shot(page, f"{base}/blog/7", out / "step-3-url-parameter.png")
        shot(page, f"{base}/", out / "step-4-home-page.png")
        shot(page, f"{base}/post/1", out / "step-5-post-page.png")
        browser.close()
    starter.shutdown()
    real.shutdown()


if __name__ == "__main__":
    main()
