"""Frames and browser windows."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import INTERNET_URL


def body_text(driver):
    return driver.find_element(By.TAG_NAME, "body").text


def h3_text(driver):
    return driver.find_element(By.TAG_NAME, "h3").text


def test_nested_frames(driver):
    """Step 5: read LEFT, MIDDLE and BOTTOM."""
    pytest.skip("TODO")


def test_new_window(driver):
    """Step 6: Click Here -> 'New Window' -> close -> back."""
    pytest.skip("TODO")
