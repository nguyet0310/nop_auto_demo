from pages.header_nav import HeaderNav
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, py):
        self.py = py
        self.header = HeaderNav(py)

    def goto(self, url):

        self.py.maximize_window().visit(url)

    def click_x(self, xpath):
        return self.py.findx(xpath).first().click()

    def click(self, css):
        return self.py.find(css).first().click()

    def get_text(self, path):
        return self.py.find(path).first().text()

    def input_text(self, locator, test_str):
        return self.py.find(locator).first().type(test_str)

    def switch_to_iframe(self, frame_locator):
        self.py.wait().until(ec.frame_to_be_available_and_switch_to_it(frame_locator))

    def get_attribute_value(self, locator, attribute):
        return self.py.find(locator).first().get_attribute(attribute)

    def check_element(self, locator):
        return self.py.find(locator).check()
