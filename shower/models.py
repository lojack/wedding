from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class RegistryItem(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  picked = models.BooleanField(default=False)
  link = models.CharField(max_length=255, blank=True)
  thumbnail = models.ImageField(upload_to="registry_items", blank=True)

  def __unicode__(self):
    return self.title

admin.site.register(RegistryItem)
