from playwright.sync_api import sync_playwright
from app.core.config import HEADLESS


class Browser:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=HEADLESS
        )
        self.page = self.browser.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()
