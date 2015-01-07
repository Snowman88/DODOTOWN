from django.db import models
from django.utils import timezone


class Town(models.Model):
    name = models.CharField(max_length=200, verbose_name="Town")
    size = models.IntegerField()
    address = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="住所")
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
