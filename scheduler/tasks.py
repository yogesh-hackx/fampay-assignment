from __future__ import absolute_import, unicode_literals

from celery import shared_task


@shared_task
def fetchVideosTask():
    # adding import inside the function because adding it globally would otherwise
    # initialize the module at the time when django modules will not be ready
    from utils.script import fetchVideos

    fetchVideos()
