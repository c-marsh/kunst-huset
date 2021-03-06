# Generated by Django 3.1 on 2020-08-10 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0002_artwork_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='year',
        ),
        migrations.AddField(
            model_name='artwork',
            name='date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='framed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artworks.artists'),
        ),
    ]
