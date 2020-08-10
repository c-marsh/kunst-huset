from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    # get a user friendly version of the category title
    def get_friendly_name(self):
        return self.friendly_name


class Artists(models.Model):
    artist = models.CharField(max_length=254)

    def __str__(self):
        return self.artist


class Artwork(models.Model):
    category = models.ForeignKey('Category',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    artist = models.ForeignKey('Artists',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    date = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    qty = models.IntegerField()
    sold = models.BooleanField(blank=False)
    framed = models.BooleanField(blank=False, null=True)
    medium = models.CharField(max_length=254)
    length = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    width = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    depth = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_id = models.CharField(max_length=1024, null=True, blank=True)
    image_url = models.URLField (max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title