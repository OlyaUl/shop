from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all_cars/$', views.CarListView.as_view(), name='all_cars'),
    url(r'^detail_car/(?P<pk>\d)/$', views.CarDetailView.as_view(), name='detail_car'),
    url(r'^car_update/(?P<pk>\d)/$', views.CarUpdate.as_view(), name='car_update'),
    url(r'^car_delete/(?P<pk>\d)/$', views.CarDelete.as_view(), name='car_delete'),
    url(r'^car_create/$', views.CarFormView.as_view(), name='car_create'),


]