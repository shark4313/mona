# coding: utf-8
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import request
from django.shortcuts import render_to_response, get_object_or_404 , render
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from models import *

from django.utils.translation import ugettext as _
from decimal import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from cms.models import Page


def show_event(request, event_id):
    event = Event.objects.get(id = event_id )  # featured cars
    related_events = event.related_events()
    templateVars = {'event': event, 'related_events': related_events }
    return default_render(request,templateVars , "events/index.html")    

    
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def show_events(request):
    event = Event.objects.all()

    paginator = Paginator(event, 5) # Show 25 contacts per page

    page = request.GET.get("page")

    try:
        events = paginator.page(page)
    except  (PageNotAnInteger, TypeError):
    
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)
        
    templateVars = {"contacts": events}
    return default_render(request,templateVars , "events/eventList.html")    

    
def showNews(request):
    Pages = Page.objects.all()
    
    paginator = Paginator(Pages, 5) # Show 25 contacts per page

    page = request.GET.get("page")

    try:
        events = paginator.page(page)
    except  (PageNotAnInteger, TypeError):
    
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)
        
    templateVars = {"contacts": events}
    return default_render(request,templateVars , "events/newsList.html")    

def latestEvents():
    return  Event.objects.all()
    
def latestNews():
    return feautredNews.objects.order_by('-pub_date')[:5] 
    
def latestEvent():
    from datetime import datetime
    # return Commig events
    now = datetime.now()
    try:
        return   Event.objects.filter(start_time__gt=now).order_by("start_time")[0]
    except:
        return None
        
def latestFeaturedNews():
    return feautredNews.objects.order_by('-pub_date')[:4]
def default_render(request,extra_context={}, template_name='index.html'):
    LatestEvents = latestEvents()
    LatestNews = latestNews()
    LatestFeaturedNews   =latestFeaturedNews()
    LatestEvent = latestEvent()
    templateVars = {"LatestEvent" : LatestEvent , "LatestEvents" : LatestEvents  , "LatestNews" : LatestNews , "LatestFeaturedNews" : LatestFeaturedNews}
    if extra_context != {}:
        templateVars.update(extra_context)

    return render( request , template_name , templateVars)
