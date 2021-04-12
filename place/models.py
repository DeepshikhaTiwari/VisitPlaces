from django.contrib.gis.db import models
from django.urls import reverse


class Place(models.Model):
    title = models.CharField(max_length=150)
    location = models.PointField(srid=4326, blank=True, null=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    address = models.CharField(max_length=225, blank=True, null=True)
    city = models.CharField(max_length=15)
    type = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('place-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
