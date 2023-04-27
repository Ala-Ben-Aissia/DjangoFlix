# Generated by Django 4.1.7 on 2023-04-14 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0012_alter_playlist_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaylistRelated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist')),
                ('related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_items', to='playlists.playlist')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='related',
            field=models.ManyToManyField(blank=True, related_name='related', through='playlists.PlaylistRelated', to='playlists.playlist'),
        ),
    ]