# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# -*- coding: utf-8 -*-
""" Processing Pipeline to output JSON, CSV, MongoDB Database ready for text sentiment analysis """
import pymongo
import os
import logging
import scrapy

# Used for mongo DB
from seekingAlpha.settings import IMAGES_STORE, FILES_STORE
from seekingAlpha import settings
from seekingAlpha.settings import OUTPUT_DIRECTORY_JSON
from seekingAlpha.settings import OUTPUT_DIRECTORY_CSV
from scrapy.pipelines.images import ImagesPipeline

from textblob import TextBlob


# Used for mongo DB
from scrapy.conf import settings
from scrapy.exceptions import DropItem

# Used for CSV and JSON Creation
from scrapy.exporters import CsvItemExporter
from scrapy.exporters import JsonLinesItemExporter

import json
#from scrapy import log
from scrapy.exporters import PythonItemExporter
from scrapy.exporters import BaseItemExporter
#from logger import logger
from seekingAlpha.settings import DEBUG_ENV

class CSVWriterPipeline(CsvItemExporter):
    """ Class to Export CSV Variable
    """

    def __init__(self):
        # CSV DB Setup
        if not os.path.exists(OUTPUT_DIRECTORY_CSV):
            os.makedirs(OUTPUT_DIRECTORY_CSV)

        self.file = open(OUTPUT_DIRECTORY_CSV + '/items.csv', 'wb')
        self.csvExport = CsvItemExporter(file=self.file, include_headers_line=True, join_multivalued=', ')


    def open_spider(self, spider):
        self.csvExport.start_exporting()

    def close_spider(self, spider):
        self.csvExport.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        for data in item:
            if not data:
                item[data] = 'empty'
                raise DropItem("Missing {0}!".format(data))


        article_body_processed = ' '.join(item['article_body'])
        # text = TextBlob(article_body_processed)
        #
        # print('--------------------------------------------------------')
        #
        # print('--------------------------------------------------------')
        # for sentence in text.sentences:
        #     print(sentence)

        # item['article_sentiment'] = text.sentiment.__getattribute__('polarity')
        # print('--------------------------------------------------------')
        # print(item['article_sentiment'])
        # print('--------------------------------------------------------')


        self.csvExport.export_item(item)

        return item



class JsonWriterPipeline(JsonLinesItemExporter):
    """ Method to Export JSON Variable
    """

    def __init__(self):
        # JSON DB Setup
        if not os.path.exists(OUTPUT_DIRECTORY_JSON):
            os.makedirs(OUTPUT_DIRECTORY_JSON)

        self.file = open(OUTPUT_DIRECTORY_JSON + '/propertyList.json', 'wb')
        self.jsonExport = JsonLinesItemExporter(file=self.file)


    def open_spider(self, spider):
        self.jsonExport.start_exporting()

    def close_spider(self, spider):
        self.jsonExport.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        for data in item:
            if not data:
                item[data] = 'empty'
                raise DropItem("Missing {0}!".format(data))

        self.jsonExport.export_item(item)
        return item


class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            # return item

class MongoDBPipeline(object):

    collection_name = 'article_items'

    def __init__(self):
        self.mongo_uri = settings.get('MONGO_URI')
        self.mongo_db = settings.get('MONGO_DATABASE')


    def open_spider(self, spider):
        self.connection = pymongo.MongoClient(self.mongo_uri)
        self.db = self.connection[self.mongo_db]
        self.collection = self.db[self.collection_name]

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):

        for data in item:
            if not data:
                item[data] = 'empty'
                raise DropItem("Missing {0}!".format(data))
        self.collection.insert_one(dict(item)).inserted_id
        logging.log(level=logging.DEBUG, msg="Question added to MongoDB database!")

        return item


class ImagesPipeline(ImagesPipeline):
    """
        Image Downloader
    """
    def __init__(self):
        if not os.path.exists(IMAGES_STORE):
            os.makedirs(IMAGES_STORE)

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")

        item['image_paths'] = image_paths

        return item


class FilesPipeline(object):
    """
        Not Currently being Used
    """
    def __init__(self):
        if not os.path.exists(FILES_STORE):
            os.makedirs(FILES_STORE)

    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")
        item['file_paths'] = file_paths

        return item
