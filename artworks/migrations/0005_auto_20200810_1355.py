# Generated by Django 3.1 on 2020-08-10 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0004_auto_20200810_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artwork',
            old_name='image_url',
            new_name='image_id',
        ),
    ]
