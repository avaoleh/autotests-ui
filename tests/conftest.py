import pytest
from playwright.sync_api import Playwright, Page


# conftest.py
pytest_plugins = (
    "fixtures.browsers"
)
