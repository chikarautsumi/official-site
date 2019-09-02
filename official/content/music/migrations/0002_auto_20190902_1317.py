# Generated by Django 2.2.4 on 2019-09-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicpage',
            name='bandcamp_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='musicpage',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
