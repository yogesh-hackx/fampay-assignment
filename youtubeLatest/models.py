from django.db import models


class Video(models.Model):
    videoId = models.CharField(max_length=12, primary_key=True)
    videoTitle = models.CharField(max_length=150)
    description = models.CharField(max_length=5000)
    publishedAt = models.DateTimeField()
    channelId = models.CharField(max_length=25)
    channelTitle = models.CharField(max_length=500)

    def __str__(self):
        return str(self.videoTitle)


THUMB_SIZES = (
    ("default", "DEFAULT"),
    ("medium", "MEDIUM"),
    ("high", "HIGH"),
)


class Thumbnail(models.Model):
    videoId = models.ForeignKey(
        Video,
        to_field="videoId",
        db_column="videoId",
        related_name="thumbnails",
        on_delete=models.CASCADE,
    )
    url = models.CharField(max_length=70)
    width = models.IntegerField()
    height = models.IntegerField()
    type = models.CharField(max_length=8, choices=THUMB_SIZES)

    class Meta:
        unique_together = ("videoId", "type")


class ApiKey(models.Model):
    key = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
