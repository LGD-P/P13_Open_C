from django.contrib import admin
from django.urls import path, include
import logging

from . import views

logger = logging.getLogger(__name__)


def trigger_error(request):
    logger.info('info')
    logger.error('error')
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error, name='sentry'),
]
