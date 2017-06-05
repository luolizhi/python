# -*- coding: utf-8 -*-
import scrapy

from quotes.items import QuotesItem


class QuotespiderSpider(scrapy.Spider):
    name = "quoteSpider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        '''follow页面上的links，以及author信息的link'''
        # 先处理下一页的link
        next_page = response.xpath('//li[@class="next"]/a/@href')
        for url in next_page.extract():
            yield scrapy.Request(response.urljoin(url), callback=self.parse)

        # 处理作者的详细信息的link
        # 将其他信息作为参数和link一起传递到下一个request
        pages = response.xpath('//div[@class="quote"]')
        for page in pages:
            content = page.xpath('./span[@class="text"]/text()').extract_first()
            author = page.xpath('./span/small[@class="author"]/text()').extract_first()
            tags = page.xpath('./div[@class="tags"]/a/text()').extract()
            relative_author_url = page.xpath('./span/a/@href').extract_first()
            author_url = response.urljoin(relative_author_url)
            yield scrapy.Request(author_url,
                                 meta={'content': content, 'author': author, 'tags': tags, 'author_url': author_url},
                                 callback=self.parse_author)

    def parse_author(self, response):
        item = QuotesItem()
        descripition = response.xpath('//div[@class="author-description"]/text()').extract_first().strip()
        item['description'] = descripition
        item['content'] = response.meta['content']
        item['author'] = response.meta['author']
        item['tags'] = response.meta['tags']
        item['author_url'] = response.meta['author_url']
        yield item
