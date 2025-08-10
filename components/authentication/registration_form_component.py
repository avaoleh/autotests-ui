from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.registration_form_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.registration_form_password_input = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill_registration_form_email(self, email: str):
        self.registration_form_email_input.fill(email)

    def fill_registration_form_username(self, username: str):
        self.registration_form_username_input.fill(username)

    def fill_registration_form_password(self, password: str):
        self.registration_form_password_input.fill(password)

    def fill(self, email: str, username: str, password: str):
        self.registration_form_email_input.fill(email)
        expect(self.registration_form_email_input).to_have_value(email)

        self.fill_registration_form_username(username)
        expect(self.registration_form_email_input).to_have_value(email)

        self.registration_form_password_input.fill(password)
        expect(self.registration_form_password_input).to_have_value(password)

    def check_visible(self):
        expect(self.registration_form_email_input).to_be_visible()
        expect(self.fill_registration_form_username).to_be_visible()
        expect(self.registration_form_password_input).to_be_visible()
