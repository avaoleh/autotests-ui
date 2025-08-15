import pytest
import allure

from config import settings
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

from tools.routes import AppRoute


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.courses
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.COURSES) # Добавили feature
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:

    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.CRITICAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        #courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.visit(AppRoute.COURSES)

        # Проверка компонента
        courses_list_page.navbar.check_visible(settings.test_user.username)

        # courses_list_page.check_visible_courses_title()
        # courses_list_page.check_visible_empty_view()

        courses_list_page.toolbar_view.check_visible()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        # Открыть страницу создания курса
        #create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.visit(AppRoute.CREATE_COURSES)
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
        create_course_page.create_course_form_component.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )

        # 5. Проверяем наличие заголовка "Exercises" и кнопки создания задания
        # create_course_page.check_visible_exercises_title()
        # create_course_page.check_visible_create_exercise_button()
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()

        # 6. Проверяем пустой блок заданий
        create_course_page.check_visible_exercises_empty_view()

        # 7. Загружаем изображение для превью курса
        # create_course_page.upload_preview_image("./testdata/files/image.png")
        #
        # # 8. Проверяем, что блок загрузки теперь отображает состояние с загруженной картинкой
        # create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

        #create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')

        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # 9. Проверяем, что превью изображения отображается
        #create_course_page.check_visible_preview_image()

        # 10. Заполняем форму создания курса
        create_course_page.create_course_form_component.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )

        # 11. Нажимаем на кнопку создания курса
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

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

    @allure.title("Create course 2")
    @allure.severity(Severity.CRITICAL)
    def test_create_course_2(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        #create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.visit(AppRoute.CREATE_COURSES)

        create_course_page.create_course_toolbar_view_component.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form_component.check_visible(
            title="", estimated_time="", description="", max_score="0", min_score="0"
        )

        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        #create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form_component.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )