
from django.utils.translation import ugettext as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import *
from cms.admin.placeholderadmin import PlaceholderAdmin


admin.site.register(Picture)