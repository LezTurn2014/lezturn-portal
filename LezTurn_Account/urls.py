from django.conf.urls import patterns, include, url
from views import mainpage,login

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^mainpage/$', mainpage, name='mainpage'),
    (r'^login/$', login)
    # url(r'^$', 'LezTurn.views.home', name='home'),
    # url(r'^LezTurn/', include('LezTurn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
