# Generated by Django 4.1.5 on 2023-01-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brikoblog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Briko Homes', max_length=255),
        ),
    ]