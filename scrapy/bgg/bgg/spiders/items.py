import scrapy

class GameItem(scrapy.Item):
    
    name = scrapy.Field()
    year = scrapy.Field()
    geek = scrapy.Field()
    average = scrapy.Field()
    voters = scrapy.Field()