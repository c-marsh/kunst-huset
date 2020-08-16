from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


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
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
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
            'artist_image',
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


class SelectorForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = (
            'is_artist',
            'is_customer')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'is_artist': '<br>Tick above if this account to sell work. This will make your profile publicly available.',
            'is_customer': 'Tick above if this account to purchase art'
        }
        self.fields['is_artist'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'tick-box'
            self.fields[field].label = placeholder
