# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class SeekingAlphaCrawlerXMLSpider(XMLFeedSpider):
    name = 'SeekingAlphaCrawlerXML'

    stocks = ['AMD', 'TSLA']
    allowed_domains = ['seekingalpha.com']
    start_urls = ['http://seekingalpha.com/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        i['url'] = selector.select('url').extract()
        i['name'] = selector.select('name').extract()
        i['description'] = selector.select('description').extract()
        return i
