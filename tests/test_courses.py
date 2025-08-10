import pytest  # Импортируем библиотеку pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.courses  # Добавили маркировку courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка компонента
    courses_list_page.navbar.check_visible("username")

    # courses_list_page.check_visible_courses_title()
    # courses_list_page.check_visible_empty_view()

    courses_list_page.toolbar_view.check_visible()


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    # Открыть страницу создания курса
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    # 1. Проверяем заголовок и состояние кнопки создания курса
    # create_course_page.check_visible_create_course_title()
    # create_course_page.check_disabled_create_course_button()

    courses_list_page.toolbar_view.check_visible()

    # 2. Проверяем пустой блок предпросмотра изображения
    # create_course_page.check_visible_image_preview_empty_view()
    #
    # # 3. Проверяем блок загрузки изображения (до загрузки)
    # create_course_page.check_visible_image_upload_view(is_image_uploaded=False)

    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

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
    # create_course_page.upload_preview_image("./testdata/files/image.png")
    #
    # # 8. Проверяем, что блок загрузки теперь отображает состояние с загруженной картинкой
    # create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    # 9. Проверяем, что превью изображения отображается
    #create_course_page.check_visible_preview_image()

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
    #courses_list_page.check_visible_courses_title()

    # 13. Проверяем наличие кнопки создания курса
    #courses_list_page.check_visible_create_course_button()

    # 14. Проверяем корректность данных на карточке курса (первый курс — индекс 0)
    # courses_list_page.check_visible_course_card(
    #     index=0,
    #     title="Playwright",
    #     max_score="100",
    #     min_score="10",
    #     estimated_time="2 weeks"
    # )

    courses_list_page.course_view.check_visible(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )