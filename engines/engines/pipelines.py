# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapings.models import CitizenModel


class EnginesPipeline(object):

    def process_item(self, item, spider):
        url = item['url']
        author = item['author']
        title = item['title']
        content = item['content']
        qs = CitizenModel.objects.filter(url__iexact=url)
        if qs.exists():
            print('article already exits .....')
            return
        if author == '' and title == '' and content == '':
            print('Empty item ......<passing>.....')
            return
        item.save()
        return item
