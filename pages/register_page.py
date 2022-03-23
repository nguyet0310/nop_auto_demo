from base_element import Elements
from pages.base_page import BasePage
from utils.route import Route
from faker import Faker


class RegisterPage(BasePage):
    url = Route.base_url + "/registerresult/1?returnUrl=/"
    true = True
    fake = Faker()

    def __init__(self, py):
        super().__init__(py)

    def goto(self):
        BasePage.goto(self, self.url)
        return self

    def select_gender(self):
        BasePage.check_element(self, Elements.check_female)
        return self

    def input_firstname(self):
        BasePage.input_text(self, Elements.txt_first_name, self.fake.first_name())
        return self

    def input_lastname(self):
        BasePage.input_text(self, Elements.txt_last_name, self.fake.last_name())
        return self

    def input_email(self):
        BasePage.input_text(self, Elements.txt_email, self.fake.email())
        return self

    def input_pw(self):
        BasePage.input_text(self, Elements.txt_password, "123456")
        return self

    def confirm_pw(self):
        BasePage.input_text(self, Elements.txt_confirm_pw, "123456")
        return self

    def click_register(self):
        BasePage.click(self, Elements.btn_register)
        return self

    def get_register_text(self):
        BasePage.get_attribute_value(self, Elements.msg_register_success, "innerHTML")
