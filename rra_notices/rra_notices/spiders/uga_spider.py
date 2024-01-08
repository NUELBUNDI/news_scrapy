import scrapy
from rra_notices.items import NoticesItem

class UgaSpiderSpider(scrapy.Spider):
    name = "uga_spider"
    allowed_domains = ["ura.go.ug"]
    start_urls = ["https://ura.go.ug/en/category/publications/public-notices/"]

    # Custom Settings 
    custom_settings = {'AUTOTHOROTTLE_ENABLED' : True, 'DOWNLOAD_DELAY':2, 'CONCURRENT_REQUESTS':16}
    

    def parse(self, response):
        for link in response.xpath("//div[@class='d-flex justify-content-between align-items-center cta-elapsed w-100']/a/@href"):
            yield response.follow(link, callback= self.news_parse)
            
    def news_parse(self, response):
        
        notice = NoticesItem()
        
        notice['notice_title']    =  response.xpath("//h1[@class='flex-grow-1 entry-title text-x-gray flex-grow-1 d-flex align-items-center my-3']/text()").get()
        notice['notice_date']     =  response.xpath("//div[@class='entry-meta bg-transparent w-100 text-end d-flex align-items-center justify-content-end']/button/@title").get()
        notice['notice_text']     =  response.xpath("//div[@class='entry-content clean-stuff']/p/text()").get()
        notice['notice_url']      =  response.url
        notice['notice_pdf']      =  None
        notice['notice_country']  = 'Uganda'

              
        yield notice