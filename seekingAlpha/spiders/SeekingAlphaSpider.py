# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.loader import ItemLoader
from seekingAlpha.items import SeekingAlphaItem



# How to parse?
class SeekingAlphaItemLoader(ItemLoader):
    def __init__(self, itemObject, response):
        super(SeekingAlphaItemLoader, self).__init__(self, itemObject=itemObject, response=response)
        self.itemObject = itemObject

        for field in self.itemObject:
            self.__setattr__(self, field, 'empty')
            # super( self).ad = 'empty'


class SeekingAlphaSpider(CrawlSpider):
    name = 'seekingalpha'

    allowed_domains = ['seekingalpha.com']

    start_urls = ['http://seekingalpha.com/symbol/AMD']


    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="symbol_article"]/a',)), callback="parse_article",
             follow=True),
    )


    def parse_article(self, response):
        #print 'Is this being printed'
        i = SeekingAlphaItem()

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        i['ticker'] =  response.xpath('//a[@sasource="article_primary_about"]').extract_first()
        i['article_title'] = response.xpath('//h1[@itemprop="headline"]/text()').extract_first()
        i['article_summary'] = response.xpath('//div[@itemprop="description"]/p/text()').extract_first()
        i['article_body'] = response.xpath('//div[@itemprop="articleBody"]/div/p/text()').extract()

        # hxs = HtmlXPathSelector(response)
        # titles = hxs.xpath('//span[@class="pl"]')
        # items = []
        # for titles in titles:
        #     item = CraigslistSampleItem()
        #     item["title"] = titles.xpath("a/text()").extract()
        #     item["link"] = titles.xpath("a/@href").extract()
        #     items.append(item)
        # return (items)


        return i
