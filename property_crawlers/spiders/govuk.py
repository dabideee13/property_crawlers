import time
import random
from pathlib import Path
from datetime import date

import scrapy
from scrapy.http import HtmlResponse
from scrapy.http.request import Request

from property_crawlers.logger import logger
from property_crawlers.driver_setup import DriverSetup
from property_crawlers.page_object.pages.govuk_page import GovukHomePage

BASE_URL = 'https://www.tax.service.gov.uk'
SPECIAL_CATEGORY = '131 - Holiday Homes (Self Catering)'
DATA_PATH = Path.joinpath(Path.cwd(), 'property_crawlers', 'data')
SCRAPE_LIST = Path.joinpath(DATA_PATH, 'scrape_list.txt')


class GovukSpider(scrapy.Spider):
    name = 'govuk'
    start_urls = ['https://www.tax.service.gov.uk/business-rates-find/list-properties/']

    def __init__(self, *args, **kwargs):
        super(GovukSpider, self).__init__(*args, **kwargs)

        self.outward_codes = self.get_outward_codes()

        self.driver = self.set_driver()
        self.driver.get(self.start_urls[0])
        self.home_page = None

    def parse(self, response):
        for outward_code in self.outward_codes:
            time.sleep(random.uniform(0.5, 2))

            self.select_filter_options(outward_code, SPECIAL_CATEGORY)

            driver_response = HtmlResponse(
                self.driver.current_url,
                body=self.driver.page_source,
                encoding='utf-8',
                request=response
            )

            table = driver_response.xpath('//table/tbody/tr')

            for idx, tr_tag in enumerate(table, start=1):
                property_link = tr_tag.xpath('./td[@class="govuk-table__cell"]/a/@href')
                property_url = BASE_URL + property_link.get()

                address = tr_tag.xpath('./td[@class="govuk-table__cell"]/a/text()').get()

                yield driver_response.follow(
                    property_url,
                    callback=self.parse_valuation,
                    cb_kwargs={
                        'source_url': property_url,
                        'address': address,
                    }
                )

            while True:
                next_page_link = driver_response.xpath('//a[@id="next_page_link"]/@href').get()

                if next_page_link is not None or len(next_page_link) > 0:
                    next_page_url = BASE_URL + next_page_link

                    yield driver_response.follow(
                        next_page_url,
                        callback=self.parse
                    )

                else:
                    break

        self.quit_driver()

    def parse_valuation(self, response, source_url: str, address: str):
        valuation_container = response.xpath('//main[@id="main-content"]')
        valuation_status = valuation_container.xpath('//h2[@class="govuk-heading-m"]/text()').get()

        if valuation_status.lower().strip() == 'current valuations':
            yield {
                'source_url': source_url,
                'name': '',
                'address_1': address,
                'address_2': '',
                'address_3': '',
                'city': '',
                'county': '',
                'postcode': '',
                'country': 'UK',
                'animal': '',
                'pet_name': '',
                'renewal_date': '',
                'date': date.today().strftime('%d/%m/%Y'),
                'outward_code': ''
            }

    def get_outward_codes(self) -> list[str]:
        with open(SCRAPE_LIST, 'r') as f:
            outward_codes = f.read().strip().split('\n')

        return [outward_code.strip() for outward_code in outward_codes]

    def set_driver(self):
        setup = DriverSetup()
        return setup.set_driver()

    def select_filter_options(self, outward_code: str, special_category: str):
        self.home_page = GovukHomePage(self.driver)
        time.sleep(random.uniform(0.5, 2))

        self.home_page.click_advanced_option()
        time.sleep(random.uniform(0.5, 2))

        self.home_page.click_address_option()
        time.sleep(random.uniform(0.5, 2))

        self.home_page.fill_postcode_field(outward_code)
        time.sleep(random.uniform(0.5, 2))

        self.home_page.select_category_dropdown(special_category)
        time.sleep(random.uniform(0.5, 2))

        self.home_page.click_search_button()
        time.sleep(random.uniform(0.5, 2))

    def quit_driver(self) -> None:
        if self.driver is not None:
            logger.info('Closing driver')

            self.driver.close()
            self.driver.quit()
