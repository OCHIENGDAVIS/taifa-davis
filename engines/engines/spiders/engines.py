import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import EnginesItem


class Nation(CrawlSpider):
    name = 'nation'
    allowed_domains = ['nation.co.ke']
    start_urls = ['https://www.nation.co.ke/']
    rules = [
        Rule(LinkExtractor(deny='https://nation.co.ke/archives.*', allow='.*'), callback='parse_items', follow=True)
    ]

    def parse_items(self, response):
        item = EnginesItem()
        main_story = response.css('div.story-view')
        item['title'] = main_story.css('header').css('h2::text').extract()
        item['author'] = main_story.css('section.author').css('strong::text').extract()
        item['published_on'] = main_story.css('header').css('h6::text').extract()
        item['image'] = main_story.css('img.photo_article').xpath('@src').get()
        item['summary'] = main_story.css('section.summary').css('li::text').extract()
        item['content'] = main_story.css('section.body-copy').css('p::text').extract()
        yield item


class Citizen(CrawlSpider):
    name = 'citizen'
    allowed_domains = ['citizentv.co.ke']
    start_urls = ['https://citizentv.co.ke/']
    rules = [
        Rule(LinkExtractor(deny='https://citizentv.co.ke/archives.*', allow='.*'), callback='parse_items', follow=True)
    ]

    def parse_items(self, response):
        item = EnginesItem()
        main_story = response.css('div.articlestory')
        item['url'] = response.url
        item['title'] = main_story.css('h1.articleh1::text').extract()[0]
        item['author'] = main_story.css('section.main-post-author').css('a::text').extract()[0]
        item['published_on'] = main_story.css('span.date-tag::text').extract()[0]
        item['image'] = main_story.css('figure.images-section').css('img').xpath('@src').get()
        item['summary'] = main_story.css('div.summary').css('li::text').extract()
        item['content'] = main_story.css('div.parallax-container').css('p::text').extract()[0]
        yield item


# Not yet finished
class Standard(CrawlSpider):
    name = 'standard'
    allowed_domains = ['standardmedia.co.ke']
    start_urls = ['https://www.standardmedia.co.ke/']
    rules = [
        Rule(LinkExtractor(deny='https://www.standardmedia.co.ke/archives.*', allow='.*'), callback='parse_items', follow=True )
    ]

    def parse_items(self, response):
        item = EnginesItem()
        main_story = response.css('article.article')
        item['title'] = main_story.css('div.article-body').css('h1.article-title::text').extract()
        item['author'] = main_story.css('section.author').css('strong::text').extract()
        item['published_on'] = main_story.css('header').css('h6::text').extract()
        item['image'] = main_story.css('img.photo_article').xpath('@src').get()
        item['summary'] = main_story.css('section.summary').css('li::text').extract()
        item['content'] = main_story.css('section.body-copy').css('p::text').extract()
        yield item


# GENERIC one page spider
class ArticleSpider(scrapy.Spider):
    name = 'citizenarticles'

    def start_requests(self):
        urls = [
            'https://citizentv.co.ke/news/lawyers-move-to-court-to-challenge-unconstitutional-curfew-328211/',
            'https://citizentv.co.ke/news/kenyas-two-recovered-coronavirus-patients-speak-out-after-23-day-quarantine-328649/',
            'https://citizentv.co.ke/lifestyle/',
        ]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        item = EnginesItem()
        main_story = response.css('div.articlestory')
        item['url'] = response.url
        item['title'] = main_story.css('h1.articleh1::text').extract()
        item['author'] = main_story.css('section.main-post-author').css('a::text').extract()
        item['published_on'] = main_story.css('span.date-tag::text').extract()
        item['image'] = main_story.css('figure.images-section').css('img').xpath('@src').get()
        item['summary'] = main_story.css('div.summary').css('li::text').extract()
        item['content'] = main_story.css('div.parallax-container').css('p::text').extract()
        print(item)
        yield item













