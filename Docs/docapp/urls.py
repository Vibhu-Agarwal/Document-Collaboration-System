from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^doc/(?P<c_name>[^/]+)/(?P<room_name>[^/]+)/$', views.main, name='main'),
    re_path(r'^compare/(?P<c_name>[^/]+)/(?P<room_name>[^/]+)/$', views.compare, name='compare'),
    re_path(r'^history/(?P<c_name>[^/]+)/(?P<room_name>[^/]+)/$', views.history, name='history'),
    path('save', views.saveit, name='saveit'),
]