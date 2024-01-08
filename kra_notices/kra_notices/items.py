import scrapy


class NewsItems(scrapy.Item):
    
    title    = scrapy.Field()
    date     = scrapy.Field()
    article  = scrapy.Field()
    url      = scrapy.Field()
