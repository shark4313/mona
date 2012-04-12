from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from guardian.admin import GuardedModelAdmin

from userena.models import UserenaSignup
from userena.utils import get_profile_model
from users.models import UserProfile

    
def full_name(obj):
        try:
            return ("%s %s %s ") %( obj.first_name , obj.get_profile().middle_name  ,  obj.last_name )
        except:
            return ("%s %s ") %( obj.first_name ,   obj.last_name )
        
class UserenaAdmin(UserAdmin, GuardedModelAdmin):
    list_display = ( 'email'   , full_name, 
                    'is_staff', 'date_joined')
    def save_model(self, request, obj, form, change):
        
        obj.save()
        object, created = UserProfile.objects.get_or_create(user = obj )
        if created == False :
            object.first_name = obj.first_name
            object.last_name = obj.last_name
            object.email = obj.email
        object.save()
        
admin.site.unregister(User)        
admin.site.register(User, UserenaAdmin)
# admin.site.register(get_profile_model() , get_profile_modelAdmin)
