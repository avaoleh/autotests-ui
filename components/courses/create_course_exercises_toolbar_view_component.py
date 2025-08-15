from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
import allure
class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        # self.create_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        self.exercises_title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Exercises Title')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button',
                                             'Create Exercise Button')

    @allure.step('Check visible create course exercise toolbar view ')
    def check_visible(self): # check_visible_exercises_title ->
        # expect(self.exercises_title).to_be_visible()
        # expect(self.exercises_title).to_have_text('Exercises')
        # expect(self.create_exercise_button).to_be_visible()

        self.exercises_title.check_visible()
        self.exercises_title.check_have_text('Exercises')
        self.create_exercise_button.check_visible()

    # def check_visible_create_exercise_button(self):
    #     expect(self.create_exercise_button).to_be_visible()

    @allure.step('Click create exercise button')
    def click_create_exercise_button(self):
        self.create_exercise_button.click()