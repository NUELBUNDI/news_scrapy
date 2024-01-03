import scrapy


class KraSpiderSpider(scrapy.Spider):
    name = "kra_spider"
    allowed_domains = ["www.kra.go.ke"]
    start_urls = ["https://www.kra.go.ke/news-center"]

    def parse(self, response):
        pass
