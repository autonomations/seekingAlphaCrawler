# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
from scrapy.loader import ItemLoader


class SeekingAlphaItem(scrapy.Item):
    ticker = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    article_title = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    article_summary = scrapy.Field(input_processor=MapCompose(str.strip))
    article_body = scrapy.Field(input_processor=MapCompose(str.strip))

    image_urls = scrapy.Field()
    file_urls = scrapy.Field()

    article_sentiment = scrapy.Field()


class SeekingAlphaItemLoader(ItemLoader):
    """ Seeking Alpha Item Loader that is an Item Wrapper Handler """

    default_item_class = SeekingAlphaItem()
    default_input_processor = TakeFirst()
    default_output_processor = MapCompose(str.strip)


    def __init__(cls, item, response):
        ItemLoader.__init__(cls, item, response)
