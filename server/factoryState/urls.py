from django.conf.urls import patterns, url

from factoryState import views

urlpatterns = patterns('',
    url(r'^load', views.load),
)

