from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<returned_id>\d+)$', views.show),

    url(r'^users/(?P<returned_id>\d+)/edit$', views.edit),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^users/(?P<returned_id>\d+)/update$', views.update),

    url(r'^ajax$', views.ajax_page),
    url(r'^all.json$', views.all_json),
    url(r'^all.html$', views.all_html),
    url(r'^find$', views.find),
    url(r'^create$', views.create)
]


#
# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^users$', views.index),
#     url(r'^users/new$', views.new),
#     url(r'^users/(?P<id>\d+)$', views.show),
#     url(r'^users/create$', views.create),
#     url(r'^users/(?P<id>\d+)/edit$', views.edit),
#     url(r'^users/(?P<id>\d+)/destroy$', views.destroy),
    # url(r'^users/(?P<id>\d+)/update$', views.update),
# ]
