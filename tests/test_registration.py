import pytest  # Импортируем библиотеку pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page_with_state):
    page = chromium_page_with_state
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    page.wait_for_timeout(5000)