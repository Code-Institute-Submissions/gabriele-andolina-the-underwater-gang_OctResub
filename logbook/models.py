from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Dive(models.Model):
    """
    Creates a Dive model for database use.
    """
    title = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dive_name')
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=255)
    diving_site = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    depth = models.CharField(max_length=255)
    gas_mixture = models.CharField(max_length=255)
    air_in = models.CharField(max_length=255)
    air_out = models.CharField(max_length=255)
    visibility = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dive_log', args=[self.slug])

    def save(self, *args):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args)

