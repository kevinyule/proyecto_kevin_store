# Generated by Django 2.2.3 on 2023-02-17 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtcs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]