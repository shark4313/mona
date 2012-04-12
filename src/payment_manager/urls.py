from django.conf.urls.defaults import url, patterns
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('payment_manager.views',
                       url(r'^report/$', 'get_month_report', ),
                       
                       )