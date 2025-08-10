from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, name: str):
        super().__init__(page)

        # self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        # self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')
        # self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button')

        self.name = name

        # Используем Page Factory элементы
        self.icon = Icon(page, f"{identifier}-drawer-list-item-icon", f"{name} Icon")
        self.title = Text(page, f"{identifier}-drawer-list-item-title-text", f"{name} Title")
        self.button = Button(page, f"{identifier}-drawer-list-item-button", f"{name} Button")

    def check_visible(self):
        """Проверяет, что иконка, текст и кнопка видимы, и текст совпадает с name."""
        # expect(self.icon).to_be_visible()
        # expect(self.title).to_be_visible()
        # expect(self.title).to_have_text(title)
        # expect(self.button).to_be_visible()

        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(self.name)
        self.button.check_visible()

    def click(self):
        """Кликает по кнопке пункта меню."""
        self.button.click()

    def navigate(self, expected_url: Pattern[str]):
        """Кликает и ожидает перехода на указанный URL (регулярное выражение)."""
        # self.button.click()
        # self.check_current_url(expected_url)

        self.button.click()
        self.check_current_url(expected_url)