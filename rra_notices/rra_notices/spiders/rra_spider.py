import scrapy
from rra_notices.items import NoticesItem


class RraSpiderSpider(scrapy.Spider):
    name = "rra_spider"
    allowed_domains = ["www.rra.gov.rw"]
    start_urls = ["https://www.rra.gov.rw/en/about-us/announcements"]
    

    def parse(self, response):
        articles = response.xpath('//div[@class="accordion-item"]')
        
        for article in articles:
            notice=NoticesItem()
            
            notice['notice_title']     = article.xpath(".//h2[@class='accordion-header']/button[@class='accordion-button']/text()").get()
            notice['notice_date']      = article.xpath(".//h2[@class='accordion-header']/button[@class='accordion-button']/text()").get()
            notice['notice_text']      = article.xpath('.//div[@class="accordion-body"]/p/a/text()').get()
            notice['notice_pdf']       = response.urljoin(article.xpath(".//div[@class='accordion-body']/p/a/@href").get())
            notice['notice_url']       = response.url
            notice['notice_country']   = 'Rwanda'
        
            yield notice
