"""Elements changed asynchronously: /dynamic_controls."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import INTERNET_URL

CHECKBOX = (By.ID, "checkbox")
CHECKBOX_BUTTON = (By.CSS_SELECTOR, "#checkbox-example button")
MESSAGE = (By.ID, "message")


def test_remove_and_add_checkbox(driver):
    """Step 3: Remove -> staleness_of -> 'It's gone!'; Add -> 'It's back!'."""
    pytest.skip("TODO")
