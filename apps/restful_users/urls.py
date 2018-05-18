from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/$', views.index),
    url(r'^new$', views.new),
    url(r'^process$', views.process),
    url(r'^process_btn$', views.process_btn),
    url(r'^show$', views.show),
    url(r'^show/(?P<returned_id>\d+)$', views.show),
]
