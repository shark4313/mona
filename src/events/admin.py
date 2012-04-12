
from django.utils.translation import ugettext as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from events.models import *
from cms.admin.placeholderadmin import PlaceholderAdmin

class eventAdmin(admin.ModelAdmin):

    #to presave or postsave items
    def save_model(self, request, obj, form, change):
        
        obj.Creator = request.user
        obj.save()


admin.site.register(Event , eventAdmin)
admin.site.register(EventCategory)
admin.site.register(feautredNews)
admin.site.register(FeautredPeople)
