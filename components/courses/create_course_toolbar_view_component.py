from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        # self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.title = Text(page, 'create-course-toolbar-title-text', 'Create Course Title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create Course Button')

    def check_visible(self, is_create_course_disabled: bool = True) -> None:
        """
        Checks the visibility of the toolbar components and button state
        :param is_create_course_disabled: Whether the create button should be disabled (True) or enabled (False)
        """
        # Check title visibility and text
        # expect(self.create_course_title).to_be_visible()
        # expect(self.create_course_title).to_have_text('Create course')
        #
        # # Check button visibility and state
        # expect(self.create_course_button).to_be_visible()
        # if is_create_course_disabled:
        #     expect(self.create_course_button).to_be_disabled()
        # else:
        #     expect(self.create_course_button).to_be_enabled()

        self.title.check_visible()
        self.title.check_have_text('Create course')

        self.create_course_button.check_visible()
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    # def check_visible_create_course_title(self):
    #     expect(self.create_course_title).to_be_visible()
    #     expect(self.create_course_title).to_have_text('Create course')

    def click_create_course_button(self):
        self.create_course_button.click()


    # def check_disabled_create_course_button(self):
    #     expect(self.create_course_button).to_be_disabled()
    #
    # def check_visible_create_course_button(self):
    #     expect(self.check_visible_create_course_button).to_be_visible()

