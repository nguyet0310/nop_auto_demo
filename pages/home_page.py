from base_element import Elements
from pages.base_page import BasePage
from utils.route import Route


class HomePage(BasePage):
    url = Route.base_url

    def __init__(self, py):
        super().__init__(py)

    def goto(self):
        BasePage.goto(self, self.url)
        return self

    def click_register_btn(self):
        BasePage.click_x(self, Elements.link_register)
        return self
