import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")


        # Регистрируем нового пользователя
        test_data = {
            'email': 'user.name@gmail.com',
            'username': 'user',
            'password': 'password'
        }

        registration_page.register_new_user(**test_data)
        dashboard_page.dashboard_toolbar_view_component.check_visible()