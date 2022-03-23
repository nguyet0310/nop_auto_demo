from base_element import Elements
from utils.resources import Resources


def test_register_user(nop_page, py):
    nop_page.homepage.goto().click_register_btn()
    nop_page.register_page.select_gender().input_firstname().input_lastname().input_email().input_pw().confirm_pw().click_register()
    assert py.get(Elements.msg_register_success).text() == Resources.success_msg
