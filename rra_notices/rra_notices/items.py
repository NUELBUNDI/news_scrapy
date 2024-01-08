import scrapy


class NoticesItem(scrapy.Item):
    
    notice_title   = scrapy.Field()
    notice_date    = scrapy.Field()
    notice_text    = scrapy.Field()
    notice_url     = scrapy.Field()
    notice_pdf     = scrapy.Field()
    notice_country = scrapy.Field()

