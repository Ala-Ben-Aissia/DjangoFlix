# Generated by Django 4.1.7 on 2023-03-28 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('playlists', '0010_playlist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playlists', to='categories.category'),
        ),
    ]
