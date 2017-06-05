# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotesPipeline(object):
    def process_item(self, item, spider):
        fileName = 'quotes00.jl'
        with open(fileName, 'a') as fp:
            fp.write(item['content'] + '\t')
            fp.write(item['author'] + '\t')
            fp.write(item['author_url'] + '\t')
            # fp.write(item['tags'] + '\t')
            fp.write(item['description'] + '\n')

        return item
