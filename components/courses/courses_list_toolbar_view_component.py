import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # self.title = page.get_by_test_id('courses-list-toolbar-title-text')
        # self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')
        self.title = Text(page, 'courses-list-toolbar-title-text', 'Courses List Title')
        self.create_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'Create Course Button')

    def check_visible(self):
        # expect(self.title).to_be_visible()
        # expect(self.title).to_have_text('Courses')
        # expect(self.create_course_button).to_be_visible()

        self.title.check_visible()
        self.title.check_have_text('Courses')
        self.create_course_button.check_visible()

    def click_create_course_button(self):
        self.create_course_button.click()
        # Дополнительно проверим, что произошел редирект на правильную страницу
        self.check_current_url(re.compile(".*/#/courses/create"))
