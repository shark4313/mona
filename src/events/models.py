from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext as _
from tagging.fields import TagField

from cms.models import CMSPlugin, Page
from cms.models.fields import PageField
from filer.fields.image import FilerImageField

class FeautredPeople(models.Model):
    full_name  = models.CharField(_('Full name '), max_length=255)
    image = FilerImageField(null=True, blank=True, default=None)
    description = models.TextField(_('Description') )
    short_description =  models.CharField(_('Short description '), max_length=255)
    
    def __unicode__(self):
        return " %s" %self.full_name
    class Meta:
        verbose_name        = _('Feautred People')
        verbose_name_plural = _('Feautred People')

class EventCategory(models.Model):
        name  = models.CharField(_('Category '), max_length=255)
        class Meta:
            verbose_name        = _('Category')
            verbose_name_plural = _('Categories')
        def __unicode__(self):
            return self.name

class Event(models.Model):
# Create your models here.
    title =  models.CharField(_('title'),help_text=_("news title"),max_length=255)
    where =   models.CharField(_('Where ?'), max_length=255)
    description = models.TextField(_('Description') )
    short_description =  models.CharField(_('Short description '), max_length=255)
    is_published = models.BooleanField(default=False)
    is_public = models.BooleanField(_('Is public'), default=True)
    # address = models.TextField(_('title'),help_text=_("news title"),max_length=255)
    image = FilerImageField(null=True, blank=True, default=None)
    featured_people  = models.ManyToManyField(FeautredPeople)
    start_time = models.DateTimeField(_("start_time"),help_text=_("start_time") , default = datetime.now() )
    end_time = models.DateTimeField(_("end_time"),help_text=_("end_time") , blank=True , null=True )
    tags = TagField(_('Tags'), blank=True)
    category = models.ForeignKey(EventCategory) 
    Creator = models.ForeignKey(User , editable= False , related_name='event_creator')
    Created_in = models.DateTimeField(_("Created in"),help_text=_("Created in") , default = datetime.now() , editable = False)

    class Meta:
        verbose_name        = _('Event')
        verbose_name_plural = _('Events')
    def get_absolute_url(self):
        return "/events/events/%i/" % self.id

    def __unicode__(self):
        return  ("%s") % (self.title )
    
    def related_events(self):
        return Event.objects.filter(category = self.category)
        
class eventPlugin(CMSPlugin):
    def get_latest_events(self):
        return Event.objects.all()

class feautredNews(models.Model):
    image = FilerImageField(null=True, blank=True, default=None)
    free_link = models.URLField(_("External link"), max_length=255, blank=True, null=True,  help_text=_("External link if present it will be used either than internal page"))
    page_link = PageField(null=True, blank=True,   help_text=_("if present image will be clickable"))
    header = models.CharField(_("Header") , max_length=255 , blank=True , null= True)
    shortDescription = models.TextField(_("short description"), max_length=255, blank=True, null=True, help_text=_("short description of the image"))
    pub_date    = models.DateTimeField(_("Created in"),help_text=_("Created in") , default = datetime.now() , editable = False)
    
    class meta:
        get_latest_by = "order_date"
        verbose_name        = _('feautred News')
        verbose_name_plural = _('feautred News')

    def __unicode__(self):
        return  "%s   %s"  % (self.header  , self.link() )

    def link(self):
        if self.free_link:
            return self.free_link
        elif self.page_link and self.page_link:
            return self.page_link.get_absolute_url()
        else:
            return ''
class feautredNewsPicturesPlugin(CMSPlugin):
    def get_featured_news(self):
    #don't forget return :D
        return feautredNews.objects.order_by('-pub_date')[:4] # the last is not with us