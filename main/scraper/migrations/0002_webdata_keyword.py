# Generated by Django 4.2.6 on 2023-10-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webdata',
            name='keyword',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]