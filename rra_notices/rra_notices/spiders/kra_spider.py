import scrapy
from rra_notices.items import NoticesItem


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
        
        notice = NoticesItem()
        
        notice['notice_title']    =  response.xpath("//h2[@class='blog-title']/text()").get() or response.xpath("//h2/text()").get()
        notice['notice_date']     =  response.xpath("//div[@class ='col-wrap leftcont']/p/text()").get()
        notice['notice_text']     =  response.xpath("//div[@class='blog-content']").get()
        notice['notice_url']      =  response.url
        notice['notice_pdf']      =  None
        notice['notice_country']  = 'Kenya'

              
        yield notice