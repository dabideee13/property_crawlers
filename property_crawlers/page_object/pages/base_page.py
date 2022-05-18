from typing import Optional

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def click(self, by_locator: tuple[str, str], driver: Optional = None) -> None:
        if driver is None:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator)).click()

        if driver is not None:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator: tuple[str, str], text: str):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def check_presence(self, by_locator: tuple[str, str], driver: Optional = None) -> None:
        if driver is None:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by_locator))

        if driver is not None:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(by_locator))

    def select_value(self, by_locator: tuple[str, str], value: str) -> None:
        Select(self.driver.find_element(*by_locator)).select_by_value(value)

    def select_text(self, by_locator: tuple[str, str], text: str) -> None:
        Select(self.driver.find_element(*by_locator)).select_by_visible_text(text)
