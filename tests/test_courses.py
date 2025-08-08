import pytest  # Импортируем библиотеку pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.courses  # Добавили маркировку courses
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


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(create_course_page, courses_list_page):
    # Открыть страницу создания курса
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    # 1. Проверяем заголовок и состояние кнопки создания курса
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()

    # 2. Проверяем пустой блок предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()

    # 3. Проверяем блок загрузки изображения (до загрузки)
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)

    # 4. Проверяем форму создания курса — значения по умолчанию
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )

    # 5. Проверяем наличие заголовка "Exercises" и кнопки создания задания
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()

    # 6. Проверяем пустой блок заданий
    create_course_page.check_visible_exercises_empty_view()

    # 7. Загружаем изображение для превью курса
    create_course_page.upload_preview_image("./testdata/files/image.png")

    # 8. Проверяем, что блок загрузки теперь отображает состояние с загруженной картинкой
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    # 9. Проверяем, что превью изображения отображается
    create_course_page.check_visible_preview_image()

    # 10. Заполняем форму создания курса
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    # 11. Нажимаем на кнопку создания курса
    create_course_page.click_create_course_button()

    # 12. После редиректа проверяем заголовок на странице со списком курсов
    courses_list_page.check_visible_courses_title()

    # 13. Проверяем наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()

    # 14. Проверяем корректность данных на карточке курса (первый курс — индекс 0)
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )