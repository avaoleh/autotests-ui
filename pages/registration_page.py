from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration = RegistrationFormComponent(page)

        # self.registration_form_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        # self.registration_form_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        # self.registration_form_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_form_submit_button = page.get_by_test_id('registration-page-registration-button')

    # def fill_registration_form_email(self, email: str) -> None:
    #     self.registration_form_email_input.fill(email)
    #
    # def fill_registration_form_username(self, username: str) -> None:
    #     self.registration_form_username_input.fill(username)
    #
    # def fill_registration_form_password(self, password: str) -> None:
    #     self.registration_form_password_input.fill(password)

    def click_registration_form_submit_button(self) -> None:
        self.registration_form_submit_button.click()

    # def check_registration_form_error_message_visible(self) -> None:
    #     expect(self.registration_form_error_message).to_be_visible()

    def register_new_user(self, email: str, username: str, password: str) -> None:
        # self.fill_registration_form_email(email)
        # self.fill_registration_form_username(username)
        # self.fill_registration_form_password(password)
        self.registration.fill(email, username, password)
        self.click_registration_form_submit_button()