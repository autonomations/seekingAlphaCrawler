# -*- coding: utf-8 -*-


import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from seekingAlpha.items import SeekingAlphaItem, SeekingAlphaItemLoader


class SeekingAlphaSpider(CrawlSpider):
    name = 'seekingalpha'
    allowed_domains = ['seekingalpha.com']
    start_urls = []

    def __init__(self, stocks, **kwargs):
        tickers = stocks.replace(' ','').split(',')
        for ticker in tickers:
            self.start_urls.append('http://seekingalpha.com/symbol/%s' % ticker)

        super(SeekingAlphaSpider, self).__init__(**kwargs)  # python3


    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="symbol_article"]/a',)), callback="parse_article",
             follow=True, ),
    )


    def parse_article(self, response):
        # Create item structure and loader variables
        i = SeekingAlphaItem()
#        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

        loader = SeekingAlphaItemLoader(item=i, response=response)

        #loader.context['article_title'] = response.xpath('//h1[@itemprop="headline"]/text()').extract_first()
        loader.add_xpath('ticker', '//a[@sasource="article_primary_about"]')
        loader.add_xpath('article_title', '//h1[@itemprop="headline"]/text()')
        loader.add_xpath('article_summary', '//div[@itemprop="description"]/p/text()')

        loader.add_xpath('article_body', '//div[@itemprop="articleBody"]//descendant::p/text()')
        loader.add_xpath('image_urls', '//div[@itemprop="articleBody"]//descendant::img/@src')

        # loader.add_xpath('comment_list', '//div[@class="c-list"]')

        return loader.load_item()


# class SeekingAlphaSpider(CrawlSpider):
#     name = 'seekingalpha'
#     allowed_domains = ['seekingalpha.com']
#     start_urls = []
#
#     def __init__(self, stocks, **kwargs):
#         tickers = stocks.replace(' ','').split(',')
#         for ticker in tickers:
#             self.start_urls.append('http://seekingalpha.com/symbol/%s' % ticker)
#
#         super().__init__(**kwargs)  # python3
#
#     rules = (
#         Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="symbol_article"]/a',)), callback="parse_article",
#              follow=True),
#     )
#
#
#     def parse_article(self, response):
#         # Create item structure and loader variables
#         i = SeekingAlphaItem()
#         loader = SeekingAlphaItemLoader(item=i, response=response)
#
#         #loader.context['article_title'] = response.xpath('//h1[@itemprop="headline"]/text()').extract_first()
#         loader.add_xpath('ticker', '//a[@sasource="article_primary_about"]')
#         loader.add_xpath('article_title', '//h1[@itemprop="headline"]/text()')
#         loader.add_xpath('article_summary', '//div[@itemprop="description"]/p/text()')
#
#         loader.add_xpath('article_body', '//div[@itemprop="articleBody"]//descendant::p/text()')
#         loader.add_xpath('image_urls', '//div[@itemprop="articleBody"]//descendant::img/@src')
#
#         # loader.add_xpath('comment_list', '//div[@class="c-list"]')
#
#         return loader.load_item()

