import scrapy

class ZimraSpiderSpider(scrapy.Spider):
    
    name            = "zimra_spider"
    allowed_domains = ["www.zimra.co.zw"]
    start_urls      = ["https://www.zimra.co.zw/public-notices"]
    
        
    def parse(self, response):
        
        articles = response.xpath("//li/div[@class='pd-filebox']")
        
        for article in articles:
            title  = article.xpath(".//div[@class='pd-title']/text()").get()
            link   = response.urljoin(article.xpath(".//a[@class='wd-download-link']/@href").get()) 
               
            yield{'title'    : title,'file_urls':[link]}
