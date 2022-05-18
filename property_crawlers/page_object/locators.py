from selenium.webdriver.common.by import By


class GovukHomePageLocators:
    advanced_option = (By.ID, 'search_advanced')
    address_option = (By.ID, 'primaryCriteria_ADDRESS')
    postcode_field = (By.ID, 'postCode')
    category_dropdown = (By.ID, 'specialCategoryCode')
    search_button = (By.ID, 'submitsearch3')
    next_button = (By.ID, 'next_page_link')
