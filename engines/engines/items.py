# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy_djangoitem import DjangoItem
# from scrapings.models import CitizenModel


class EnginesItem(scrapy.Item):
    # django_model = CitizenModel
    title = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    image = scrapy.Field()
    published_on = scrapy.Field()
    summary = scrapy.Field()
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    data = scrapy.Field()
    timestamp = scrapy.Field()
    spider = scrapy.Field()
    domain = scrapy.Field()
