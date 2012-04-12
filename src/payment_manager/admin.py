from django.contrib import admin

from models import *
from src.users.models import *

class PaymentsHistoryAdmin(admin.ModelAdmin):
    model = PaymentsHistory
    list_filter = ('month', ) 
    list_display = ("user", 'paid', 'month',)
    search_fields = ['user__email' , "user__profile__mobile"]

admin.site.register(PaymentsHistory, PaymentsHistoryAdmin)
admin.site.register(MassPaymentStatus)
