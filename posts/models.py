from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    img = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.title
