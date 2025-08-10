from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # self.app_title = page.get_by_test_id('navigation-navbar-app-title-text')
        # self.welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')
        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'App Title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome Title')

    def check_visible(self, username: str):
        # expect(self.app_title).to_be_visible()
        # expect(self.app_title).to_have_text('UI Course')
        #
        # expect(self.welcome_title).to_be_visible()
        # expect(self.welcome_title).to_have_text(f'Welcome, {username}!')

        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')
