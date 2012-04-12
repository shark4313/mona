from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import eventPlugin , feautredNewsPicturesPlugin
from django.utils.translation import ugettext as _


class CMSEventPlugin(CMSPluginBase):
    model = eventPlugin
    name = _("Event")
    render_template = "events/events.html"

    def render(self, context, instance, placeholder):
    #instance is the plugin model ex CMSEventPlugin
        context.update({
            'events':instance.get_latest_events(),
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSEventPlugin)


class CMSfeautredNewsPlugin(CMSPluginBase):
    model = feautredNewsPicturesPlugin
    name = _("Featured News")
    render_template = "featured/featured.html"

    def render(self, context, instance, placeholder):
    #instance is the plugin model ex CMSEventPlugin
        context.update({
            'LatestFeaturedNews':instance.get_featured_news(),
            'object':instance,
            'placeholder':placeholder,
            
        })
        return context

plugin_pool.register_plugin(CMSfeautredNewsPlugin)

