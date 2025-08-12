from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
from elements.text import Text


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        # self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        # self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

        self.email_input = Input(page, 'login-form-email-input', 'Email Input')
        self.password_input = Input(page, 'login-form-password-input', 'Password Input')
        self.wrong_email_or_password_alert = Text(page, 'login-page-wrong-email-or-password-alert', 'Error Alert')

    def fill(self, email: str, password: str):
        # self.email_input.fill(email)
        # expect(self.email_input).to_have_value(email)
        #
        # self.password_input.fill(password)
        # expect(self.password_input).to_have_value(password)

        self.email_input.fill(email)
        self.password_input.fill(password)

    def check_visible(self):
        # expect(self.wrong_email_or_password_alert).to_be_visible()
        # expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text("Wrong email or password")

    def check_visible_login_form(self):
        # expect(self.wrong_email_or_password_alert).to_be_visible()
        # expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")
        self.email_input.check_visible()
        self.password_input.check_visible()