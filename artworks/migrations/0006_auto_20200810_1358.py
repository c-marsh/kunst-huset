# Generated by Django 3.1 on 2020-08-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0005_auto_20200810_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='image_id',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
