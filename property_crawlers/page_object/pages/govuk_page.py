from property_crawlers.page_object.locators import GovukHomePageLocators
from .base_page import BasePage


class GovukHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_advanced_option(self):
        self.click(GovukHomePageLocators.advanced_option)

    def click_address_option(self):
        self.click(GovukHomePageLocators.address_option)

    def fill_postcode_field(self, text: str):
        self.enter_text(GovukHomePageLocators.postcode_field, text)

    def select_category_dropdown(self, text: str):
        self.select_text(GovukHomePageLocators.category_dropdown, text)

    def click_search_button(self):
        self.click(GovukHomePageLocators.search_button)

    def click_next_button(self):
        self.click(GovukHomePageLocators.next_button)
