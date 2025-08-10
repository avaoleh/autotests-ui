import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # self.logout_list_item = SidebarListItemComponent(page, 'logout')
        # self.courses_list_item = SidebarListItemComponent(page, 'courses')
        # self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

        self.dashboard_list_item = SidebarListItemComponent(page, "dashboard", "Dashboard")
        self.courses_list_item = SidebarListItemComponent(page, "courses", "Courses")
        self.logout_list_item = SidebarListItemComponent(page, "logout", "Logout")


    def check_visible(self):
        # self.logout_list_item.check_visible('Logout')
        # self.courses_list_item.check_visible('Courses')
        # self.dashboard_list_item.check_visible('Dashboard')

        self.dashboard_list_item.check_visible()
        self.courses_list_item.check_visible()
        self.logout_list_item.check_visible()

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))