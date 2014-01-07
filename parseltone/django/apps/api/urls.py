from django.conf.urls import *

urlpatterns = patterns('parseltone.django.apps.api.views',
    url(r'^login/', 'login', name='api_login'),
    url(r'^permissions/', 'permissions', name='api_permissions'),
)
