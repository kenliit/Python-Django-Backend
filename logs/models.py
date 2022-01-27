from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


User = get_user_model()


class UserLog(models.Model):
    sessionId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_ip = models.GenericIPAddressField(null=True, blank=True)
    login_time = models.DateTimeField(null=False, default=timezone.now)
    country = models.CharField(max_length=2, blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    isp = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return f"{self.user.nickname} -- {self.login_time}"

    @staticmethod
    def write_log(request, content):
        if 'ip' in request.session:
            ip = request.session['ip']
        else:
            ip = None

        if 'countryCode' in request.session:
            countryCode = request.session['countryCode']
        else:
            countryCode = None

        if 'regionCode' in request.session:
            regionCode = request.session['regionCode']
        else:
            regionCode = None

        if 'city' in request.session:
            city = request.session['city']
        else:
            city = None

        if 'isp' in request.session:
            isp = request.session['isp']
        else:
            isp = None

        log = UserLog.objects.create(
            user=request.user,
            login_ip=ip,
            country=countryCode,
            region=regionCode,
            city=city,
            isp=isp,
            content=content
        )

        return log.pk


















