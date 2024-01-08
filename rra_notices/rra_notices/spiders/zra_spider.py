import scrapy
from rra_notices.items import NoticesItem


class ZraSpiderSpider(scrapy.Spider):
    name = "zra_spider"
    allowed_domains = ["www.zra.org.zm"]
    start_urls = ["https://www.zra.org.zm/category/zra-news"]

    def parse(self, response):
        for link in response.xpath('//div[@class="post_read_more"]/a/@href'):
            yield response.follow(link=link, callable=self.notices)
            
    def notices(self, response):
        
        notice = NoticesItem()
        
        notice['notice_title']    =  response.xpath('//h2/text()')
        notice['notice_date']     =  response.xpath('//li[@class="post_date"]/i/text()').get
        notice['notice_text']     =  response.xpath('//div[@class="wpb_text_column"]/p/text()').getall()
        notice['notice_url']      =  response.url
        notice['notice_pdf']      =  None
        notice['notice_country']  = 'Zambia'

