"""ActionChains, keyboard, drag and drop, scrolling, Select."""
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from config import INTERNET_URL

FIGURES = (By.CLASS_NAME, "figure")
PARAGRAPHS = (By.CLASS_NAME, "jscroll-added")
LOADING = (By.CLASS_NAME, "jscroll-loading")

# HTML5 drag and drop simulated with JavaScript events (step 10)
JS_DRAG_AND_DROP = """
const [source, target] = arguments;
const dt = new DataTransfer();
const fire = (el, type) => el.dispatchEvent(new DragEvent(type,
    {bubbles: true, cancelable: true, dataTransfer: dt}));
fire(source, 'dragstart'); fire(target, 'dragenter');
fire(target, 'dragover'); fire(target, 'drop');
fire(source, 'dragend');
"""


def column_headers(driver):
    return [c.text for c in driver.find_elements(By.CLASS_NAME, "column")]


def loaded_paragraphs(driver):
    """Number of paragraphs; -1 while the last one is still loading."""
    if driver.find_elements(*LOADING):
        return -1
    return len(driver.find_elements(*PARAGRAPHS))


# --- step 8: hover -------------------------------------------------------
@pytest.mark.parametrize("number", [1, 2, 3])
def test_hover_shows_caption(driver, number):
    """Step 8: move_to_element(figure) -> caption visible."""
    pytest.skip("TODO")


# --- step 9: keyboard and context menu ------------------------------------
@pytest.mark.parametrize("key, name", [
    (Keys.TAB, "TAB"),
    (Keys.ESCAPE, "ESCAPE"),
    (Keys.SPACE, "SPACE"),
    ("a", "A"),
], ids=["tab", "esc", "space", "letter"])
def test_keys(driver, key, name):
    """Step 9: send_keys(key) to #target, check #result."""
    pytest.skip("TODO")


def test_context_menu(driver):
    """Step 9: context_click(#hot-spot) -> alert."""
    pytest.skip("TODO")


# --- step 10: drag and drop -----------------------------------------------
@pytest.mark.xfail(strict=False,
                   reason="HTML5 DnD: ActionChains works only "
                          "in some ChromeDriver versions")
def test_drag_and_drop_actionchains(driver):
    driver.get(f"{INTERNET_URL}/drag_and_drop")
    a = driver.find_element(By.ID, "column-a")
    b = driver.find_element(By.ID, "column-b")
    ActionChains(driver).drag_and_drop(a, b).perform()
    assert column_headers(driver) == ["B", "A"]


def test_drag_and_drop_javascript(driver):
    """Step 10: execute_script(JS_DRAG_AND_DROP, a, b)."""
    pytest.skip("TODO")


# --- step 11: scrolling and Select ----------------------------------------
def test_scroll_to_footer(driver):
    """Step 11: scroll_to_element(#page-footer) until 2 paragraphs."""
    pytest.skip("TODO")


def test_dropdown(driver):
    """Step 11: Select – by visible text and by value."""
    pytest.skip("TODO")


# --- step 12: element screenshot ------------------------------------------
def test_element_screenshot(driver, tmp_path):
    """Step 12: screenshot of #column-a to tmp_path."""
    pytest.skip("TODO")
