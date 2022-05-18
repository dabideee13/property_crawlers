import scrapy
from scrapy.http import HtmlResponse

from property_crawlers.logger import logger
from property_crawlers.driver_setup import DriverSetup
from property_crawlers.page_object.pages.govuk_page import GovukHomePage

BASE_URL = 'https://www.tax.service.gov.uk'


class GovukSpider(scrapy.Spider):
    name = 'govuk'
    start_urls = ['https://www.tax.service.gov.uk/business-rates-find/list-properties/']

    def __init__(self, *args, **kwargs):
        super(GovukSpider, self).__init__(*args, **kwargs)

        self.driver = self.set_driver()
        self.driver.get(self.start_urls[0])

    def parse(self, response):
        driver_response = HtmlResponse(
            self.driver.current_url,
            body=self.driver.page_source,
            encoding='utf-8',
            request=response
        )

    def set_driver(self):
        setup = DriverSetup()
        return setup.set_driver()

    def select_filter_options(self):
        home_page = GovukHomePage(self.driver)
        home_page.click_advanced_option()
        home_page.click_address_option()

        # TODO
        home_page.fill_postcode_field()
        home_page.select_category_dropdown()

        home_page.click_search_button()

    def quit_driver(self) -> None:
        if self.driver is not None:
            logger.info('Closing driver')

            self.driver.close()
            self.driver.quit()
