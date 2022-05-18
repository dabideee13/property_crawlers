import json

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from spiders.govuk import GovukSpider


def spider_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(GovukSpider)
    process.start()  # the script will block here until the crawling is finished

    return results


def main():
    data = spider_results()

    with open('items.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
