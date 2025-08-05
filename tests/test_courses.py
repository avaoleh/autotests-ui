from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        # Первая часть: регистрация и сохранение состояния
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Открываем страницу регистрации
        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
            wait_until='networkidle'
        )

        # 2. Заполняем форму регистрации
        email_input = page.locator('//*[@id=":r0:"]')
        email_input.fill('user.name@gmail.com')

        username_input = page.locator('//*[@id=":r1:"]')
        username_input.fill('username')

        password_input = page.locator('//*[@id=":r2:"]')
        password_input.fill('password')

        # 3. Нажимаем кнопку Registration
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # 4. Сохраняем состояние браузера
        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        # Вторая часть: новая сессия с сохраненным состоянием
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        # 5. Открываем страницу Courses
        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses",
            wait_until='networkidle'
        )

        # 6. Проверяем заголовок "Courses"
        courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_header).to_be_visible()
        expect(courses_header).to_have_text("Courses")

        # 7. Проверяем icon
        no_results = page.get_by_test_id('courses-list-empty-view-icon')
        expect(no_results).to_be_visible()

        # 8. Проверяем блок "There is no results"
        no_results = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results).to_be_visible()
        expect(no_results).to_have_text("There is no results")

        # 9. Проверяем блок "Results from the load test pipeline will be displayed here"
        results = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(results).to_be_visible()
        expect(results).to_have_text("Results from the load test pipeline will be displayed here")