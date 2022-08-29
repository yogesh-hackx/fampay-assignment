from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from youtubeLatest.models import Video
from youtubeLatest.serializers import VideoSerializer


class VideoView(viewsets.ModelViewSet):
    # getting videos in descending order of their published date
    queryset = Video.objects.all().order_by("-publishedAt")
    serializer_class = VideoSerializer
    # adding various filters
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["videoTitle"]
