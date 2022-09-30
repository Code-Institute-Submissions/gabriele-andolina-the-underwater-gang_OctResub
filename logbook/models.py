from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Dive(models.Model):
    """
    Creates a Dive model for database use.
    """
    diver = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=255, blank=False)
    diving_site = models.CharField(max_length=255, blank=False)
    duration = models.CharField(max_length=255, blank=True)
    depth = models.CharField(max_length=255, blank=True)
    gas_mixture = models.CharField(max_length=255, blank=True)
    air_in = models.CharField(max_length=255, blank=True)
    air_out = models.CharField(max_length=255, blank=True)
    visibility = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('dive_content', args=[self.slug])

    def save(self, *args):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args)

