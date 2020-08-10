from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey('Artist', null=True, blank=True, on_delete=models.SET_NULL)
    year = models.IntegerField(null=True, blank=True)
    Title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    sold = models.BooleanField(blank=False)
    medium = models.CharField(max_length=254)
    length = models.IntegerField(null=True, blank=True)
    width = models.IntegerField( null=True, blank=True)
    depth = models.IntegerField( null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    duration = models.IntegerField( null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

