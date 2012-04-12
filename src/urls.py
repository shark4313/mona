from django.conf import settings
from django.conf.urls.defaults import handler500, handler404, patterns, include, \
    url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('userena.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
       url(r'^events/', include('events.urls'))  ,  
       url(r'^poll/', include('cmsplugin_poll.urls')),
       (r'^test/(\d+)/$', 'users.views.feed_models'),
       (r'^search/$', 'users.views.search'),
       (r'^team/(?P<team_id>\d+)/$', 'users.views.showTeam'),
    (r'^comments/', include('django.contrib.comments.urls')),

    url(r'^', include('cms.urls')),

    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    url(r'^media/cms/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.CMS_MEDIA_ROOT, 'show_indexes': True}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

)

if settings.DEBUG:
    urlpatterns = patterns(
        '',

        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

        url(r'', include('django.contrib.staticfiles.urls')),

    ) + urlpatterns

    