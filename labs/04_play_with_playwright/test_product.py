import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page.get_by_text("Get started")).to_be_visible()


def test_has_product(page: Page):
    page.goto("http://localhost:5173/")    