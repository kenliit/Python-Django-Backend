from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from events.models import *


admin.site.register(AdditionalInfo)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("start_date", "end_date", "short_theme", "total_thumbs", "total_comments")
    list_filter = ("start_date", )
    search_fields = ("theme__startswith", )

    def short_theme(self, obj):
        return obj.__str__()

    def total_thumbs(self, obj):
        count = obj.eventthumb_set.count()
        url = (
            reverse("admin:events_eventthumb_changelist")
            + "?"
            + urlencode({"event_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, count)

    def total_comments(self, obj):
        count = obj.eventcomment_set.count()
        url = (
            reverse("admin:events_eventcomment_changelist")
            + "?"
            + urlencode({"event_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, count)



