from comments.moderation import CommentModerator, moderator
from django.db import models
from django.utils.translation import ugettext as _
from cms.models import CMSPlugin

class Discussion (models.Model):
    title = models.CharField(_('Title'), max_length=128)
    enable_comments = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class DiscussionPlugin(CMSPlugin):
    discussion = models.ForeignKey(Discussion)

class EntryModerator(CommentModerator):
    """
    email admins when comment is inserted
    """
    email_notification = True
    enable_field = 'enable_comments'

moderator.register(Discussion, EntryModerator)
