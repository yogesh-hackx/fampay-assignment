# Generated by Django 3.2 on 2022-08-28 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('videoId', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('videoTitle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('publishedAt', models.DateTimeField()),
                ('channelId', models.CharField(max_length=25)),
                ('channelTitle', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=70)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('type', models.CharField(choices=[('default', 'DEFAULT'), ('medium', 'MEDIUM'), ('high', 'HIGH')], max_length=8)),
                ('videoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnails', to='youtubeLatest.video')),
            ],
        ),
    ]