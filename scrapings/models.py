from django.db import models
# title = scrapy.Field()
    # content = scrapy.Field()
    # author = scrapy.Field()
    # image = scrapy.Field()
    # published_on = scrapy.Field()
    # summary = scrapy.Field()
    # url = scrapy.Field()
    # project = scrapy.Field()
    # spider = scrapy.Field()
    # server = scrapy.Field()
    # data = scrapy.Field()


class CitizenModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    published_on = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    url = models.CharField(blank=True, null=True, max_length=255)
    timestamp = models.CharField(blank=True, null=True, max_length=255)
    spider = models.CharField(blank=True, null=True, max_length=255)
    domain = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        verbose_name = 'Citizen Articles'
        verbose_name_plural = 'Citizen Articles'

    def __str__(self):
        return self.title







