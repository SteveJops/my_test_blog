# Generated by Django 3.1.4 on 2021-07-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210719_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/', verbose_name='Image'),
        ),
    ]
