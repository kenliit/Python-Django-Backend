import json
import pytz
import urllib3
from .get_user_ip_address import visitor_ip_address
from django.conf import settings
from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')
        if tzname is None:
            http = urllib3.PoolManager()
            if settings.DEBUG:
                r = http.request('GET', 'http://ip-api.com/json/68.147.172.43')
                request.session['ip'] = '68.147.172.43'
            else:
                request.session['ip'] = visitor_ip_address(request)
                r = http.request('GET', 'http://ip-api.com/json/' + request.session['ip'])
            print(request.session['ip'])
            tz = json.loads(r.data.decode('utf-8'))
            if tz['status'] == 'success':
                try:
                    tzname = tz['timezone']
                    request.session['django_timezone'] = tzname
                    timezone.activate(pytz.timezone(tzname))
                    # request.session['country'] = tz['country']
                    request.session['countryCode'] = tz['countryCode']
                    # request.session['region'] = tz['regionName']
                    request.session['regionCode'] = tz['region']
                    request.session['city'] = tz['city']
                    # request.session['latitude'] = tz['lat']
                    # request.session['longitude'] = tz['lon']
                    request.session['isp'] = tz['isp']
                except:
                    pass
            else:
                timezone.deactivate()
                request.session['django_timezone'] = 'unknown'

        return self.get_response(request)



