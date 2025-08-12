
import allure
import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.title("User login with wrong email or password")
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.title("User login with correct email and password")
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        # Регистрация
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_form_submit_button()

        # Проверка входа
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

        # Выход
        dashboard_page.sidebar.click_logout()

        # Ожидание возврата на страницу входа
        #login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.check_visible_login_form()

        # Вход
        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        # Проверка повторного входа
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

    @allure.title("Navigation from login page to registration page")
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        print("Current URL after click:", login_page.page.url)

        registration_page.page.wait_for_url("**/auth/registration")
        registration_page.registration_form.check_visible()