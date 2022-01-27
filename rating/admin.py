from django.contrib import admin
from .models import *


@admin.register(ImageOrVideo)
class ImageOrVideoAdmin(admin.ModelAdmin):
    fields = ['type', 'video_uri', 'image', 'show_content']
    readonly_fields = ['show_content']


admin.site.register(Comment)
admin.site.register(CommentThumb)



























