from django.conf.urls import url
from . import views
 
 
urlpatterns = [
    url(r'^$', views.unit_list, name='unit_list'),
    url(r'^update/$', views.update_availability1, name='update_availability1'),
    # url(r'^update/(?P<pk>\d+)/(?P<userid>\d+)/$', views.update_availability, name='update_availability'),
]