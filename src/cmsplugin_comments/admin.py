from models import Discussion
from django.contrib import admin

class DiscussionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Discussion, DiscussionAdmin)
