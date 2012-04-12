# -*- coding: utf-8 -*-
from cms.apphook_pool import apphook_pool
from cms.views import details
from django.conf import settings
from django.conf.urls.defaults import url, patterns
from views import show_event , show_events , showNews

urlpatterns = patterns('',
		    url(r'^events/(?P<event_id>\d+)/$', show_event, name='show_event'),
		    url(r'^events/$', show_events, name='show_events'),
		    url(r'^news/$', showNews, name='showNews'),
          )