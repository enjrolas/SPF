from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spf_sales.views.home', name='home'),
    # url(r'^spf_sales/', include('spf_sales.foo.urls')),
     
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^factoryState/', include('factoryState.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^command/', 'command.views.command'),
     url(r'^json/', 'command.views.json'),
     url(r'^interface/', 'command.views.interface'),
     url(r'^testing/', 'command.views.testing'),
     url(r'^startup/', 'command.views.startup'),
     url(r'^order/', 'order.views.order'),
     url(r'^latestCommand/', 'command.views.latestCommand'),
     url(r'^differentCommands/', 'command.views.newCommands'),
     url(r'^tinyGParameter/', 'command.views.tinyGParameter'),
     url(r'^factoryState/', 'command.views.factoryState'),

)
