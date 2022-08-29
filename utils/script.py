from datetime import datetime, timedelta, timezone
import requests
from youtubeLatest.models import ApiKey, Thumbnail, Video
from django.db import transaction


reqUrl = "https://youtube.googleapis.com/youtube/v3/search"


def fetchVideos(nextPageToken=None, publishedAfter=None):

    # reset request data/payload object every time fetchVideos is called
    reqData = {
        "part": "snippet",
        "q": "cricket",
        "type": "video",
        "order": "date",
        "maxResults": 50,
    }

    keys = ApiKey.objects.all()

    if publishedAfter is None:
        # fetching videos of last 10 minutes
        publishedAfter = (
            (datetime.now(timezone.utc) - timedelta(minutes=10))
            .isoformat()
            .replace("+00:00", "Z")
        )
    for key in keys:
        reqData["key"] = key.key
        if nextPageToken is not None:
            reqData["pageToken"] = nextPageToken

        reqData["publishedAfter"] = publishedAfter

        res = requests.get(reqUrl, reqData)
        print(res.status_code)
        print(res.json())

        # if quota exceeds for a api-key, move on to the next available api-key
        if (
            res.status_code == 403
            and res.json()["error"]["errors"][0]["reason"] == "quotaExceeded"
        ):
            print("QUOTA EXCEEDED!")
            continue
        if res.status_code == 200:
            data = res.json()
            hasNextPage = True if "nextPageToken" in data else False

            # inserting data one by one, can't use bulk-upsert because django currently doesn't supports it
            for item in data["items"]:
                videoId = item["id"]["videoId"]
                videoTitle = item["snippet"]["title"]
                description = item["snippet"]["description"]
                publishedAt = item["snippet"]["publishedAt"]
                channelId = item["snippet"]["channelId"]
                channelTitle = item["snippet"]["channelTitle"]

                thumbnails = item["snippet"]["thumbnails"]
                thumbTypes = ["default", "medium", "high"]

                with transaction.atomic():
                    Video.objects.get_or_create(
                        videoId=videoId,
                        videoTitle=videoTitle,
                        description=description,
                        publishedAt=publishedAt,
                        channelId=channelId,
                        channelTitle=channelTitle,
                    )
                    for thumbType in thumbTypes:
                        url = thumbnails[thumbType]["url"]
                        width = thumbnails[thumbType]["width"]
                        height = thumbnails[thumbType]["height"]
                        video = Video.objects.get(videoId=videoId)
                        Thumbnail.objects.get_or_create(
                            videoId=video,
                            url=url,
                            width=width,
                            height=height,
                            type=thumbType,
                        )

            # recursively fetching the next-page's data, as youtube API max allows 50 records/page
            if hasNextPage:
                fetchVideos(data["nextPageToken"], publishedAfter)
