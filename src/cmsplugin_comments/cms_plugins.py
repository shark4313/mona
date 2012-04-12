from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import DiscussionPlugin, Discussion
from django.utils.translation import ugettext as _
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType

class CMSDiscussionPlugin(CMSPluginBase):
        model = DiscussionPlugin
        name = _("Comments")
        render_template = "comments/cms-comment.html"

        def render(self, context, instance, placeholder):

            context.update({'instance':instance.discussion,
                            "enabled" : instance.discussion.enable_comments , 
                            'placeholder':placeholder,
                            })
            return context

plugin_pool.register_plugin(CMSDiscussionPlugin)
