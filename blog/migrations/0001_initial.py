# Generated by Django 3.1.4 on 2021-07-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50, verbose_name='Blog Title')),
                ('blog_date', models.DateTimeField(auto_now_add=True, verbose_name='Blog Date')),
                ('blog_text', models.TextField(verbose_name='Main Text')),
                ('blog_image', models.ImageField(upload_to='blog/', verbose_name='Blog Image')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]