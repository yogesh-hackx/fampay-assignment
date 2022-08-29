from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):
    dependencies = [
        ('youtubeLatest', '0004_auto_20220828_1727'),
    ]

    operations = [
        TrigramExtension(),
    ]
