import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from custom_functions.models_functions import upload_to

User = get_user_model()


class Thumb(models.Model):
    like = models.BooleanField(null=False, default=True)
    by_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    vote_time = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return self.by_user.name + " - " + str(self.like)


class Rating(models.Model):
    rate = models.IntegerField(null=False, default=5)
    by_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    rate_time = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return self.by_user.name + " - " + str(self.rate)


class ImageOrVideo(models.Model):
    class ItemType(models.TextChoices):
        Type1 = 'YouTube', 'YOUTUBE'
        Type2 = 'Facebook', 'FACEBOOK'
        Type3 = 'Picture', 'PICTURE'

    type = models.CharField(max_length=20, null=False, choices=ItemType.choices)
    video_uri = models.CharField(max_length=200, null=True, blank=True,
                                 help_text="YouTube: only YouTube Id. Facebook: whole link")
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        print(self.type)
        if self.type == self.ItemType.Type3:
            return self.image.url
        else:
            return self.video_uri

    def save_item(self, item_type, uri):
        new_item = ImageOrVideo()
        if item_type == self.ItemType.Type3:
            new_item.type = self.ItemType.Type3
            new_item.image = uri

    def set_primary(self):
        self.is_primary = True

    def delete(self, *args, **kwargs):
        if self.type == self.ItemType.Type3:
            if os.path.exists(self.image.name):
                os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        return super(ImageOrVideo, self).delete(*args, **kwargs)

    def show_content(self):
        if self.type == self.ItemType.Type3:
            return mark_safe(f'<img src="{self.image.url}" width="300px" height="auto" />')
        elif self.type == self.ItemType.Type1:
            return mark_safe(
                f'<iframe \
                    width="400" height="300" \
                    src="https://www.youtube.com/embed/{self.video_uri}" \
                    title="YouTube video player" \
                    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; \
                    picture-in-picture" allowfullscreen>\
                    </iframe>'
            )
        elif self.type == self.ItemType.Type2:
            return mark_safe(
                f'<iframe \
                    src="https://www.facebook.com/plugins/video.php?\
                    href={self.video_uri}&show_text=false&t=0" \
                    width="400" height="300" \
                    style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" \
                    allow="autoplay;\
                    allowFullScreen="true">\
                    </iframe>'
            )

    show_content.short_description = 'content'


class Comment(models.Model):
    content = models.CharField(max_length=500, null=False)
    by_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    wrote_time = models.DateTimeField(null=False, default=timezone.now)
    is_primary = models.BooleanField(null=False, default=True)
    reply_to = models.IntegerField(null=True, blank=True)
    iov = models.OneToOneField(ImageOrVideo, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.by_user.name + " - " + self.content


class CommentThumb(Thumb):
    comment = models.ForeignKey(Comment, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment.by_user.name + " - " + self.comment.content[:50]








