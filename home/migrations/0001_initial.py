# Generated by Django 4.0.1 on 2022-01-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=225, verbose_name='genre')),
                ('artist_name', models.CharField(max_length=225, verbose_name='artist_name')),
                ('track_name', models.CharField(max_length=225, verbose_name='track_name')),
                ('track_id', models.IntegerField(verbose_name='track_id')),
                ('popularity', models.IntegerField(verbose_name='popularity')),
                ('acousticness', models.FloatField(verbose_name='acousticness')),
                ('danceability', models.FloatField(verbose_name='danceability')),
                ('duration_ms', models.BigIntegerField(verbose_name='duration_ms')),
                ('energy', models.FloatField(verbose_name='energy')),
                ('instrumentalness', models.FloatField(verbose_name='instrumentalness')),
                ('key', models.CharField(max_length=150, verbose_name='key')),
                ('liveness', models.FloatField(verbose_name='liveness')),
                ('loudness', models.FloatField(verbose_name='loudness')),
                ('mode', models.CharField(max_length=225, verbose_name='mode')),
                ('speechiness', models.FloatField(verbose_name='speechiness')),
                ('tempo', models.FloatField(verbose_name='tempo')),
                ('time_signature', models.DateField(auto_now=True, verbose_name='time signature')),
                ('valence', models.FloatField(verbose_name='valence')),
            ],
        ),
    ]