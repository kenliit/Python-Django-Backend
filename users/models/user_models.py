from random import randint
from django.core.mail import EmailMessage
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils import timezone
from backend.config import register_email_title, verification_code_length
from custom_functions.models_functions import OverwriteStorage, upload_to
from django.conf import settings
from rest_framework.authtoken.models import Token

from locations.models import Location
from users.managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


def make_token_string(user):
    token = Token.objects.get_or_create(user=user)[0].key
    result = token[:16] + token[20:30] + token[16:20] + token[30:]

    return result


class AgeType(models.TextChoices):
    All = 'F', 'All'
    Kid = 'K', 'KID'
    Adult = 'A', 'ADULT'
    Senior = 'S', 'Senior'


class CustomUser(AbstractUser):

    class LevelType(models.IntegerChoices):
        New = 1, 'NEW'
        Reg = 2, 'REGULAR'
        Adv = 3, 'ADVANCE'
        Buz = 4, 'BUSINESS'

    avatar = models.ImageField(
        upload_to=upload_to,
        null=False,
        default='user_avatar.jpg'
        )
    username = None
    email = models.EmailField(_('email'), unique=True)
    phone = PhoneNumberField(null=True)
    nickname = models.CharField(max_length=100, null=False, default='User')
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=1, blank=True, null=True, choices=AgeType.choices)
    level = models.IntegerField(null=False, choices=LevelType.choices, default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"

    def send_register_email(self):
        msg_html = render_to_string(
            'company/user_registration.html',
            {
                'user': self,
            }
        )
        msg = EmailMessage(subject=register_email_title, body=msg_html,
                           from_email=settings.DEFAULT_FROM_EMAIL, to=[self.email])
        msg.content_subtype = "html"
        return msg.send()

    def send_reset_password_email(self):
        msg_html = render_to_string(
            'company/user_resetpassword.html',
            {
                'user': self,
            }
        )
        msg = EmailMessage(subject=register_email_title, body=msg_html,
                           from_email=settings.DEFAULT_FROM_EMAIL, to=[self.email])
        msg.content_subtype = "html"
        return msg.send()

    def get_token_string(self):
        return make_token_string(self)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_registration_email(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        VerificationCode.generate_code(instance)
        CustomUser.send_register_email(instance)


def add_half_hour():
    return timezone.now() + timezone.timedelta(minutes=30)


def gen_code(n=6):
    return ''.join(['{}'.format(randint(0, 9)) for _ in range(0, n)])


class VerificationCode(models.Model):
    user = models.OneToOneField(CustomUser, blank=False, null=False, unique=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=verification_code_length, null=False, blank=False, default=gen_code)
    expire_time = models.DateTimeField(null=False, blank=False, default=add_half_hour)

    def __str__(self):
        return self.code

    @staticmethod
    def generate_code(user):
        verification = VerificationCode.objects.get_or_create(user=user)
        return verification

    @staticmethod
    def verify_code(user, code):
        try:
            record = VerificationCode.objects.get(user=user)
            if record.code == code and timezone.now() < record.expire_time:
                return True
            else:
                return False
        except VerificationCode.DoesNotExist:
            return False
        except VerificationCode.MultipleObjectsReturned as e:
            return False





