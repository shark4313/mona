from django.utils.translation import ugettext as _
from users.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Country)
admin.site.register(Governorate)
admin.site.register(City)
    
def full_name(obj):
        return   ("%s %s %s") %( obj.first_name ,  obj.middle_name ,  obj.last_name )
        
class UserProfileAdmin(admin.ModelAdmin):
        list_filter = ('gender',"workFeild__name" , "myteam__name" , "myteam__city__governorate__name")
        search_fields = ['user__email', 'mobile']
        exclude = [ "user" , "mugshot"]
        list_display= [full_name , "mobile" , "email" ] 
        
        
admin.site.register(Team)
# admin.site.unregister(UserProfile)
admin.site.register(UserProfile , UserProfileAdmin)
admin.site.register(WorkFeild)
