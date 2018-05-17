from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/$', views.index),
    url(r'^new$', views.new),
    url(r'^process$', views.process),
    url(r'^show$', views.show),
]
