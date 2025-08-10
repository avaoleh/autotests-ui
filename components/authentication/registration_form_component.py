from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # self.registration_form_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        # self.registration_form_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        # self.registration_form_password_input = page.get_by_test_id('registration-form-password-input').locator('input')

        self.email_input = Input(page, 'registration-form-email-input', 'Email Input')
        self.username_input = Input(page, 'registration-form-username-input', 'Username Input')
        self.password_input = Input(page, 'registration-form-password-input', 'Password Input')


    # def fill_registration_form_email(self, email: str):
    #     self.registration_form_email_input.fill(email)
    #
    # def fill_registration_form_username(self, username: str):
    #     self.registration_form_username_input.fill(username)
    #
    # def fill_registration_form_password(self, password: str):
    #     self.registration_form_password_input.fill(password)

    def fill(self, email: str, username: str, password: str):
        # self.registration_form_email_input.fill(email)
        # expect(self.registration_form_email_input).to_have_value(email)
        #
        # self.fill_registration_form_username(username)
        # expect(self.registration_form_email_input).to_have_value(email)
        #
        # self.registration_form_password_input.fill(password)
        # expect(self.registration_form_password_input).to_have_value(password)

        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

        self.email_input.check_have_value(email)
        self.username_input.check_have_value(username)
        self.password_input.check_have_value(password)

    def check_visible(self):
        # expect(self.registration_form_email_input).to_be_visible()
        # expect(self.fill_registration_form_username).to_be_visible()
        # expect(self.registration_form_password_input).to_be_visible()

        self.email_input.check_visible()
        self.username_input.check_visible()
        self.password_input.check_visible()