from django.contrib import admin

# Register your models here.
from shortner import models
admin.site.register(models.ShortUrl)