from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'default_phone_number',
                  'default_street_address1',
                  'default_street_address2',
                  'default_town_or_city',
                  'default_county',
                  'default_postcode',
                  'default_country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form'
            self.fields[field].label = False


class ArtistForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = (
            'full_name',
            'bio',
            'location',
            'is_artist',
            'is_customer',
            'artist_image',
            'artist_image_url',
            'artist_link',
            'artist_insta',
            'artist_deviant',
            'artist_twitter')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'bio': 'Biography',
            'location': 'Location',
            'is_artist': 'Account to sell work?',
            'is_customer': 'Account to purchase art?',
            'artist_image': 'Headshot',
            'artist_link': 'Link to website',
            'artist_insta': 'Link to Instagram Profile',
            'artist_deviant': 'Link to DeviantArt Profile',
            'artist_twitter': 'Link to Twitter Profile'
        }
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form'
            self.fields[field].label = False
