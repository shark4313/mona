# Django settings for cms project.
from distutils.version import LooseVersion
import django
import os
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

CMS_CONTENT_CACHE_DURATION = 0
MANAGERS = ADMINS

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': 'egamal_monasikia1',
         'USER': 'egamal_monasikia',                      # Not used with sqlite3.
	 'PASSWORD': 'monasikiap455w0rd',                  # Not used with sqlite3.
	 'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
	 'PORT': '',    
    }
 }
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'djangocms2',
        
#        }
#        }
DATABASE_SUPPORTS_TRANSACTIONS = True

TIME_ZONE = 'Africa/Cairo'

SITE_ID = 1

USE_I18N = True


MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
STATIC_ROOT =  'static/'

CMS_MEDIA_ROOT = os.path.join(PROJECT_DIR, '../../cms/media/cms/')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

FIXTURE_DIRS = [os.path.join(PROJECT_DIR, 'fixtures')]

SECRET_KEY = '*xq7m@)*f2awoj!spa0(jibsrz9%c0d=e(g)v*!17y(vx0ue_3'
THUMBNAIL_DEBUG = True
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
#)


LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
ANONYMOUS_USER_ID  =  -1
USERENA_MUGSHOT_GRAVATAR = True
AUTH_PROFILE_MODULE = 'users.UserProfile'

# TEMPLATE_LOADERS = (
    # ('django.template.loaders.cached.Loader', (
      
        # 'django.template.loaders.app_directories.Loader',
          # 'django.template.loaders.filesystem.Loader',
        # 'django.template.loaders.eggs.Loader',
    # )),
# )
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)



TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    'django.core.context_processors.csrf',
    "cms.context_processors.media",
    "sekizai.context_processors.sekizai",
    
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = (


    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
   
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
  'userena.middleware.UserenaLocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    
)

ROOT_URLCONF = 'src.urls'


TEMPLATE_DIRS = (
                    'templates'
)

STATICFILES_DIRS = (

    '/static',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
   
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


INSTALLED_APPS = [
    'userena',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'comments',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
    'menus',
    'cms.plugins.text',
    # 'cms.plugins.picture',
    # 'cms.plugins.file',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'cms.plugins.flash',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    
    "cmsplugin_comments",
    # 'cms.plugins.teaser',
    # 'cms.plugins.video',
    'cms.plugins.twitter',
    'cms.plugins.inherit',
    'mptt',
    'src.sampleapp',
    # 'project.placeholderapp',
    # 'project.pluginapp',
    # 'project.pluginapp.plugins.manytomany_rel',
    # 'project.fakemlng',
    # 'project.fileapp',
    'south',
    # 'reversion',
    'sekizai',
    # 'cms_themes',
       # 'imagestore.imagestore_cms',
       # 'imagestore',
    'easy_thumbnails',
    "cmsplugin_poll",
    # 'inline_ordering',
    # 'cmsplugin_gallery',
    'tagging',
    # "gallery",
    "events",

    # 'cmsplugin_facebook',
    # 'cms_facebook',
    'users',
    "django_extensions",
    'guardian',
    "debug_toolbar",
    'payment_manager',
]

# COMMENTS_APP = 'cmsplugin_comments'


AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tafratest1@gmail.com'
EMAIL_HOST_PASSWORD = 'tafratest'
EMAIL_USE_TLS = True



if LooseVersion(django.get_version()) >= LooseVersion('1.3'):
    INSTALLED_APPS.append('django.contrib.staticfiles')
    TEMPLATE_CONTEXT_PROCESSORS.append("django.core.context_processors.static")
else:
    INSTALLED_APPS.append('staticfiles')
    TEMPLATE_CONTEXT_PROCESSORS.append("staticfiles.context_processors.static")


gettext = lambda s: s

LANGUAGE_CODE = "ar"

LANGUAGES = (
    ('ar', gettext('Arabic')),
)

CMS_LANGUAGES = (
    ('ar', gettext('Arabic')),
)

APPEND_SLASH = True

CMS_TEMPLATES = (
    ('col_two.html', gettext('two columns')),
    
    ('nav_playground.html', gettext('navigation examples')),

)


CMS_SOFTROOT = True
CMS_MODERATOR = True
CMS_PERMISSION = True
CMS_PUBLIC_FOR = 'all'
CMS_CACHE_DURATIONS = {
    'menus': 0,
    'content': 0,
    'permissions': 0,
}
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_FLAT_URLS = False
CMS_MENU_TITLE_OVERWRITE = True
CMS_HIDE_UNTRANSLATED = False
CMS_URL_OVERWRITE = True
CMS_SHOW_END_DATE = True
CMS_SHOW_START_DATE = True

CMS_PLUGIN_PROCESSORS = tuple()

CMS_PLUGIN_CONTEXT_PROCESSORS = tuple()

SOUTH_TESTS_MIGRATE = False
IMAGESTORE_SHOW_USER  = False


CMS_NAVIGATION_EXTENDERS = (
    ('src.sampleapp.menu_extender.get_nodes', 'SampleApp Menu'),
)

try:
    from local_settings import *
except ImportError:
    pass
    
TEST_RUNNER = 'src.testrunner.CMSTestSuiteRunner'
TEST_OUTPUT_VERBOSE = True
