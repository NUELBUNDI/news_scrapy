import scrapy


class ZimSpiderSpider(scrapy.Spider):
    name = "zim_spider"
    allowed_domains = ["www.zimra.co.zw"]
    start_urls = ["https://www.zimra.co.zw/public-notices"]

    def parse(self, response):
        pass
