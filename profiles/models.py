from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Create User profile model
    """
    # publicly visible profile info
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=60, blank=False)
    bio = models.TextField(max_length=5000, blank=True)
    location = models.CharField(max_length=30, blank=True)
    is_artist = models.BooleanField('artist status', default=False)
    is_customer = models.BooleanField('customer status', default=True)
    artist_image = models.ImageField(null=True, blank=True)
    artist_image_url = models.URLField(max_length=1024, null=True, blank=True)
    artist_link = models.URLField(max_length=1024, null=True, blank=True)
    artist_insta = models.URLField(max_length=1024, null=True, blank=True)
    artist_deviant = models.URLField(max_length=1024, null=True, blank=True)
    artist_twitter = models.URLField(max_length=1024, null=True, blank=True)

    # administration contact info
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


# Create a UserProfile instance on creation of a profile
post_save.connect(create_or_update_user_profile, sender=User)
