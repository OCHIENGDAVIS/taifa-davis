from django.core.management.base import BaseCommand, CommandError
from scrapy.crawler import CrawlerProcess
from engines.engines.spiders import engines


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Spinnig up the crawler......')
        process = CrawlerProcess()
        process.crawl(engines.Citizen)
        process.start()
