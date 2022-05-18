from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from property_crawlers.page_object.locators import GovukHomePageLocators
from .base_page import BasePage


class GovukHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    def click_advanced_option(self):
        # self.click(GovukHomePageLocators.advanced_option)
        self.driver.find_element(By.ID, 'search_advanced').click()

    def click_address_option(self):
        # self.click(GovukHomePageLocators.address_option)
        self.driver.find_element(By.ID, 'primaryCriteria_ADDRESS').click()

    def fill_postcode_field(self, text: str):
        # self.enter_text(GovukHomePageLocators.postcode_field, text)
        Select(self.driver.find_element(By.ID, 'postCode')).select_by_value(text)

    def select_category_dropdown(self, text: str):
        # self.select_text(GovukHomePageLocators.category_dropdown, text)
        Select(self.driver.find_element(By.ID, 'specialCategoryCode')).select_by_visible_text(text)

    def click_search_button(self):
        # self.click(GovukHomePageLocators.search_button)
        self.driver.find_element(By.ID, 'submitsearch3').click()

    def click_next_button(self):
        # self.click(GovukHomePageLocators.next_button[])
        self.driver.find_element(By.ID, 'next_page_link').click()
