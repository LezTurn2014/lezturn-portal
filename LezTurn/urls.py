from django.conf.urls import patterns, include, url
import LezTurn_Account.urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'',include(LezTurn_Account.urls))
    # url(r'^$', 'LezTurn.views.home', name='home'),
    # url(r'^LezTurn/', include('LezTurn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
