# Generated by Django 4.1.7 on 2023-04-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
