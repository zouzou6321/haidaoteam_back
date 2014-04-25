from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from haidaoteam import settings
urlpatterns = patterns('',
                       url(r'^$','haidaoteam_json.json_web.webroot'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^haidao_one_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,'show_indexes':True  }),
                       url(r'^(?P<path>.*)','haidaoteam_json.json_web.webholdon'),
    # Examples:
    # url(r'^$', 'haidaoteam.views.home', name='home'),
    # url(r'^haidaoteam/', include('haidaoteam.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
