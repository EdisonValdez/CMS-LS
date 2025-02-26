# home/urls.py

from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls
from search import views as search_views
from django.http import HttpResponse
from django.urls import path, include

def health_check(request):
    """
    Simple view that returns a 200 OK response for health checks.
    """
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('', include('lscms.urls')),   
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('search/', search_views.search, name='search'),
    path('', include(wagtail_urls)),  
]
