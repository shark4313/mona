from django.db import models
from userena.models import UserenaBaseProfile
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class WorkFeild(models.Model):
    name = models.CharField(_("Work name") , max_length=255)
    class Meta:
        verbose_name        = _('Work Feild')
        verbose_name_plural = _('Work Feilds')
    def __unicode__(self):
        return self.name

class Country(models.Model):
    name =models.CharField(_('Country Name'),  max_length=30 , default= "Egypt")
    class Meta:
        verbose_name        = _('Country')
        verbose_name_plural = _('Countries')

    def __unicode__(self):
        return self.name

class Governorate(models.Model):
    name =models.CharField(_('Governorate Name'),  max_length=30)
    country = models.ForeignKey(Country   ,   verbose_name=_('Country') , default = 1)     
    featured    = models.BooleanField(_("Featured") , default=False)
    class Meta:
        verbose_name        = _('Governorate')
        verbose_name_plural = _('Governorates')

    def __unicode__(self):
        return self.name
    
class City(models.Model):
    name =models.CharField(_('City Name'),  max_length=30 , default = "Cairo")
    governorate = models.ForeignKey(Governorate   ,   verbose_name=_('Governorate')  , default = 1)     
    featured    = models.BooleanField(_("Featured") , default=False)
    class Meta:
        verbose_name        = _('City')
        verbose_name_plural = _('Cities')

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name =models.CharField(_('Team Name'),  max_length=30)
    featured  = models.BooleanField(_("Featured") , default=False)
    address =    models.CharField(_('Address'), help_text="1600 Amphitheatre Pky, Mountain View, CA" ,  max_length=255 , blank = True)        
   # members = models.ManyToManyField(UserProfile,   verbose_name=_('Team members' ) , blank=True)
    contact =     models.CharField(_('Contact'), help_text="0105555551" , blank = True  ,  max_length=20 ) 
    city = models.ForeignKey(City   ,   verbose_name=_('City') )     
    class Meta:
        verbose_name        = _('Team')
        verbose_name_plural = _('Teams')

    def __unicode__(self):
        return  ("%s in %s") % (self.name , self.city.name)    
    
class UserProfile(UserenaBaseProfile):
    MALE= 0
    FEMALE = 1
 
    GENDER_CHOICES = (
               
                (MALE, _('male')),
                (FEMALE, _('female')) ,

            )

    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    middle_name = models.CharField(_('middle_name'),  max_length=30 , blank = True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    email = models.EmailField(_('e-mail address'), blank=True)

    gender = models.IntegerField(_("Gender"), choices=GENDER_CHOICES, default=MALE)
    monthly_payment =  models.DecimalField(_("Monthly payment"), help_text=_("Monthly payment"), decimal_places=1, max_digits=10 , default = 50 )

    age = models.CharField(_('Age'),   max_length=3 , blank = True)
    mobile  = models.CharField(_('Mobile'),help_text=_("  Mobile number Ex: 01112345678"),max_length=11 )
    tele2  = models.CharField(_('Telephone 2'),help_text=_("anther telephone "),max_length=15 , blank = True )
    facebook = models.CharField(_('Facebook'),  help_text=("example http://www.facebook.com/sharkstein") ,  max_length=255 , blank = True)
    twitter = models.CharField(_('Twitter'), help_text="example  https://twitter.com/sharkawy4313" ,  max_length=255 , blank = True )
    interests =   models.TextField(_('Interests'),help_text=_("Describe your interests") , blank = True)
    paid  = models.BooleanField(_("paid") , default=False)
    myteam =  models.ForeignKey(Team   ,   verbose_name=_('Team')  , default = 1 )     
    workFeild = models.ForeignKey(WorkFeild ,  default=0)
    profession = models.CharField(_("Profession") , max_length  = 255)
    
    def __unicode__(self):
        return   ("%s %s %s") %( self.first_name ,  self.middle_name ,  self.last_name )
        
        
  

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
