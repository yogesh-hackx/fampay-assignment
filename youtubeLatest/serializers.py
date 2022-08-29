from rest_framework import serializers
from youtubeLatest.models import Thumbnail, Video


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["url", "width", "height", "type"]


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    # including respective thumbnails to the video resultset
    thumbnails = ThumbnailSerializer(read_only=True, many=True)

    class Meta:
        model = Video
        fields = [
            "videoId",
            "videoTitle",
            "description",
            "publishedAt",
            "channelId",
            "channelTitle",
            "thumbnails",
        ]
        ordering = ["-publishedAt"]
