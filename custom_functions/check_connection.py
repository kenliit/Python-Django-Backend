from django.http import HttpResponse


def check_connection(request):
    return HttpResponse('ok')




