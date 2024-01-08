import scrapy


class TzaSpiderSpider(scrapy.Spider):
    name = "tza_spider"
    allowed_domains = ["www.tra.go.tz"]
    start_urls = ["https://www.tra.go.tz/"]

    def parse(self, response):
        pass
