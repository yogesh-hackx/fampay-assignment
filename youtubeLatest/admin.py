from django.contrib import admin

# Register your models here.
from .models import ApiKey, Video, Thumbnail

admin.site.register(Video)
admin.site.register(Thumbnail)
admin.site.register(ApiKey)
