from django.db import models
from django.db.models import Sum
from django.core.cache import cache
from django.utils.text import slugify

from datetime import datetime

# Create your models here.



from django.db import models

class jsondata(models.Model):
    end_year = models.IntegerField(blank=True, null=True)
    intensity = models.IntegerField(blank=True, null=True)
    sector = models.TextField( blank=True, null=True)
    topic = models.TextField( blank=True, null=True)
    insight = models.TextField( blank=True, null=True)
    url = models.TextField( blank=True, null=True)
    region = models.TextField( blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    impact = models.TextField( blank=True, null=True)
    added =models.TextField( blank=True, null=True)
    published = models.TextField( blank=True, null=True)
    country = models.TextField( blank=True, null=True)
    relevance = models.IntegerField(blank=True, null=True)
    pestle = models.TextField( blank=True, null=True)
    source = models.TextField( blank=True, null=True)
    title = models.TextField( blank=True, null=True)
    likelihood = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Convert the "added" string to a datetime object
        if self.added:
            self.added = datetime.strptime(self.added, "%B, %d %Y %H:%M:%S")

        # Convert the "published" string to a datetime object
        if self.published:
            self.published = datetime.strptime(self.published, "%B, %d %Y %H:%M:%S")

        super().save(*args, **kwargs)

    def get_intensity_density(self):
         intensity=self.intensity
         print(intensity)
              


    


class tinky(models.Model):
        name:models.CharField(max_length=20)