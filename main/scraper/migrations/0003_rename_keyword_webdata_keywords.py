# Generated by Django 4.2.6 on 2023-10-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_webdata_keyword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webdata',
            old_name='keyword',
            new_name='keywords',
        ),
    ]
