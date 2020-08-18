from django.db import models
from profiles.models import UserProfile
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    class Meta:
        # Fix display in Admin
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    # get a user friendly version of the category title
    def get_friendly_name(self):
        return self.friendly_name


class Artwork(models.Model):
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE)
    artist = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.CharField(max_length=10)
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    qty = models.IntegerField()
    sold = models.BooleanField(blank=False)
    framed = models.BooleanField(blank=False, null=True)
    medium = models.CharField(max_length=254)
    length = models.DecimalField('length (cm)', max_digits=6, decimal_places=2,
                                 blank=False, null=True)
    width = models.DecimalField('width (cm)', max_digits=6, decimal_places=2,
                                blank=False, null=True)
    depth = models.DecimalField('depth (cm)', max_digits=6, decimal_places=2,
                                blank=False, null=True)
    weight = models.DecimalField('weight (g)', max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    duration = models.IntegerField('duration (mins)',null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.title

    def get_artist(self):
        return self.artist

