# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.loader import ItemLoader
from seekingAlpha.items import SeekingAlphaItem, SeekingAlphaItemLoader

from scrapy.loader.processors import TakeFirst, MapCompose, Join



class SeekingAlphaSpider(CrawlSpider):
    name = 'seekingalpha'
    allowed_domains = ['seekingalpha.com']
    start_urls = ['http://seekingalpha.com/symbol/AMD']


    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="symbol_article"]/a',)), callback="parse_article",
             follow=True),
    )


    def parse_article(self, response):
        # Create item structure and loader variables
        i = SeekingAlphaItem()
        loader = SeekingAlphaItemLoader(item=i, response=response)

        #loader.context['article_title'] = response.xpath('//h1[@itemprop="headline"]/text()').extract_first()
        loader.add_xpath('ticker', '//a[@sasource="article_primary_about"]')
        loader.add_xpath('article_title', '//h1[@itemprop="headline"]/text()')
        loader.add_xpath('article_summary', '//div[@itemprop="description"]/p/text()')

        loader.add_xpath('article_body', '//div[@itemprop="articleBody"]//descendant::p/text()')
        loader.add_xpath('image_urls', '//div[@itemprop="articleBody"]//descendant::img/@src')

        # loader.add_xpath('comment_list', '//div[@class="c-list"]')

        return loader.load_item()

