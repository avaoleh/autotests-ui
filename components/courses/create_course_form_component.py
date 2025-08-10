from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        # self.create_course_estimated_time_input = (
        #     page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        # )
        # self.create_course_description_textarea = (
        #     page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        # )
        # self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        # self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        self.title_input = Input(page, 'create-course-form-title-input', 'Course Title Input')
        self.estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'Estimated Time Input')
        self.description_textarea = Textarea(page, 'create-course-form-description-input', 'Description Textarea')
        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'Max Score Input')
        self.min_score_input = Input(page, 'create-course-form-min-score-input', 'Min Score Input')

    def fill(  # fill_create_course_form -> fill
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        # self.create_course_title_input.fill(title)
        # expect(self.create_course_title_input).to_have_value(title)
        #
        # self.create_course_estimated_time_input.fill(estimated_time)
        # expect(self.create_course_estimated_time_input).to_have_value(estimated_time)
        #
        # self.create_course_description_textarea.fill(description)
        # expect(self.create_course_description_textarea).to_have_value(description)
        #
        # self.create_course_max_score_input.fill(max_score)
        # expect(self.create_course_max_score_input).to_have_value(max_score)
        #
        # self.create_course_min_score_input.fill(min_score)
        # expect(self.create_course_min_score_input).to_have_value(min_score)

        """Заполняет форму создания курса."""
        self.title_input.fill(title)
        self.estimated_time_input.fill(estimated_time)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

        # Проверяем значения (опционально, если нужно строго)
        self.title_input.check_have_value(title)
        self.estimated_time_input.check_have_value(estimated_time)
        self.description_textarea.check_value(description)
        self.max_score_input.check_have_value(max_score)
        self.min_score_input.check_have_value(min_score)

    def check_visible(  # check_visible_create_course_form -> check_visible
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        # expect(self.create_course_title_input).to_be_visible()
        # expect(self.create_course_title_input).to_have_value(title)
        #
        # expect(self.create_course_estimated_time_input).to_be_visible()
        # expect(self.create_course_estimated_time_input).to_have_value(estimated_time)
        #
        # expect(self.create_course_description_textarea).to_be_visible()
        # expect(self.create_course_description_textarea).to_have_value(description)
        #
        # expect(self.create_course_max_score_input).to_be_visible()
        # expect(self.create_course_max_score_input).to_have_value(max_score)
        #
        # expect(self.create_course_min_score_input).to_be_visible()
        # expect(self.create_course_min_score_input).to_have_value(min_score)

        """Проверяет, что поля формы видимы и содержат ожидаемые значения."""
        self.title_input.check_visible()
        self.title_input.check_have_value(title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.check_value(description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_value(min_score)
