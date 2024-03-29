import scrapy
from kra_notices.items import NewsItems


class KraSpiderSpider(scrapy.Spider):
    name              = "kra_spider"
    allowed_domains   = ["www.kra.go.ke"]
    start_urls        = ["https://www.kra.go.ke/news-center"]
    
    
    # Custom Settings 
    custom_settings = {'AUTOTHOROTTLE_ENABLED' : True, 'DOWNLOAD_DELAY':2, 'CONCURRENT_REQUESTS':16}
    

    def parse(self, response):
        for link in response.xpath("//div[@class='col-md-3']/a/@href"):
            yield response.follow(link, callback= self.news_parse)
            
    def news_parse(self, response):
        
        news_items = NewsItems()
        news_items['title']    = response.xpath("//h2[@class='blog-title']/text()").get() or response.xpath("//h2/text()").get()
        news_items['date']     = response.xpath("//div[@class ='col-wrap leftcont']/p/text()").get()
        news_items['article']  = response.xpath("//div[@class='blog-content']").get()
        news_items['url']      = response.url

              
        yield news_items
        
