from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


# overwriting the file if exist.
from django.utils import timezone


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


def make_thumbnail(picture):

    image = Image.open(picture)

    image.thumbnail(settings.BANNER_SIZE, Image.ANTIALIAS)

    thumb_name, thumb_extension = os.path.splitext(picture.name)
    thumb_extension = thumb_extension.lower()
    thumb_name = thumb_name[thumb_name.rfind('/') + 1:]

    thumb_filename = thumb_name + '_thumb' + thumb_extension

    if thumb_extension in ['.jpg', '.jpeg']:
        FTYPE = 'JPEG'
    elif thumb_extension == '.gif':
        FTYPE = 'GIF'
    elif thumb_extension == '.png':
        FTYPE = 'PNG'
    else:
        return False  # Unrecognized file type

    # Save thumbnail to in-memory file as StringIO
    temp_thumb = BytesIO()
    image.save(temp_thumb, FTYPE)
    temp_thumb.seek(0)

    # set save=False, otherwise it will run in an infinite loop
    picture.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
    temp_thumb.close()

    return True


def reduce_quality(picture, quality=30, size=None, crop_box=None):
    if not os.path.exists(picture):
        return False

    image = Image.open(picture)













