from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from users.models import UserProfile
class PaymentsHistory(models.Model):
    did_not_pay = "0"
    paid = "1"
    PAYMENT_STATUS = (
                        (paid, _('paid')),
                        (did_not_pay, _('did_not_pay')),
                      )
    
    user = models.ForeignKey(UserProfile,)
    month = models.DateField(auto_now_add=True)
    paid = models.CharField(max_length=30, choices=PAYMENT_STATUS)
    
    def __unicode__(self):
        return self.user.username + " : " + self.paid
        
    class Meta:
        verbose_name = _('history_record')
        verbose_name_plural = _('history_records')
    

class MassPaymentStatus(models.Model):
    
    month = models.DateField(auto_now_add=True)
    num_who_paid = models.IntegerField(_('paid'))
    num_who_didnt = models.IntegerField(_('did not pay'))
    
    class Meta:
        verbose_name = _('status_item')
        verbose_name_plural = _('status_items')
        
    