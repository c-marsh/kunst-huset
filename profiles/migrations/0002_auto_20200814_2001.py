# Generated by Django 3.1 on 2020-08-14 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=60)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('is_artist', models.BooleanField(default=False, verbose_name='artist status')),
                ('is_customer', models.BooleanField(default=False, verbose_name='customer status')),
                ('artist_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('artist_image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('artist_link', models.URLField(blank=True, max_length=1024, null=True)),
                ('artist_insta', models.URLField(blank=True, max_length=1024, null=True)),
                ('artist_deviant', models.URLField(blank=True, max_length=1024, null=True)),
                ('artist_twitter', models.URLField(blank=True, max_length=1024, null=True)),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('default_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('default_county', models.CharField(blank=True, max_length=80, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
