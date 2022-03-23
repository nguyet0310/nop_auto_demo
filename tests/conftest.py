import pytest
from pages.nop_pages import NopPage


@pytest.fixture
def nop_page(py):
    return NopPage(py)
