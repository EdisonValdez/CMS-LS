# lscms/health/views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def health_check(request):
    return HttpResponse("OK", status=200)
