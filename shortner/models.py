from uuid import uuid4
from django.db import models


class ShortUrl(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=5000)
    short_url = models.CharField(max_length=90, blank=True, null=True)

    def __str__(self):
        return self.link

    @classmethod
    def create(cls, short_url):
        link = cls(short_url=short_url)
        # do something with the book
        return link
