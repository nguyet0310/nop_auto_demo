from pages.home_page import HomePage
from pages.register_page import RegisterPage


class NopPage:
    def __init__(self, py):
        self.py = py
        self.homepage = HomePage(py)
        self.register_page = RegisterPage(py)
