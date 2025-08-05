from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.locator('//*[@id=":r0:"]')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.locator('//*[@id=":r1:"]')
    username_input.fill("password")

    # Заполняем поле пароль
    password_input = page.locator('//*[@id=":r2:"]')
    password_input.fill("password")

    # Нажимаем на кнопку Login
    login_button = page.get_by_test_id('registration-page-registration-button')
    login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    dashboard_txt = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_txt).to_be_visible()
    expect(dashboard_txt).to_have_text("Dashboard")

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)