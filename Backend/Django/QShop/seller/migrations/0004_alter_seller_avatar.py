# Generated by Django 3.2.3 on 2021-05-23 15:22

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20210523_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=None),
        ),
    ]
