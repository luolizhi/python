# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from pymongo import MongoClient
from scrapy.exceptions import DropItem


URL = scrapy.conf.settings['MONGODB_URL']
# DB = scrapy.conf.settings['MONGODB_DATABASE']
# COLLECTION = scrapy.conf.settings["MONGO_COLLECTION"]

class MongoDBPipeline(object):

    def __init__(self):
        client = MongoClient(URL)
        self.db = client.scrapy
        self.collection = self.db.quotes


    def process_item(self, item, spider):
        post = {
            'content':item['content'],
            'author':item['author'],
            'author_url':item['author_url'],
            'tags':item['tags'],
            'description':item['description']
        }
        self.collection.insert(post)
        return item
