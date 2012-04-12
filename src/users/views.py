# Create your views here.

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from users.forms import *
from django.template import RequestContext
from events.views import  default_render
#ajax request 
def feed_models(request, city_id):    
    city = City.objects.get(pk=city_id)  
    teams = Team.objects.filter(city=city)     
    return render_to_response('teamSelection.html', {"city_id":city_id,'teams':teams}, )


def search(request):
    template_name = "searchResults.html"
    value = ""
    if request.method == 'GET':
        try:
            value = request.GET['q']
        except:
            pass
            
        # if value == "" or " ": 
            # cities = City.objects.filter(name__icontains=value)
            # governorates = Governorate.objects.filter(name__icontains=value)
            # teams = Team.objects.filter(name__icontains=value)     
            # extra_context = {"cities": cities  ,
                                    # "governorates" : governorates ,
                                    # "teams" : teams }
            # return default_render(request,
                                # extra_context,
                                # template_name =template_name)    

        # else:
        
        # cities = City.objects.filter(name__contains=value)
        # cities1 = City.objects.filter(governorate__name__icontains =value)
        # governorates = Governorate.objects.filter(name__icontains=value)
        teams = Team.objects.filter(name__icontains=value)     
        teams1 = Team.objects.filter(city__name__icontains =value)
        teams2 = Team.objects.filter(city__governorate__name__icontains = value)
        extra_context = {
                                    # "cities": cities , "cities1" : cities1 ,
                                    # "governorates" : governorates ,
                                    "teams2":teams2 ,"teams1" : teams1 ,    "teams" : teams }
    
  
        return default_render(request,
                                extra_context,
                                template_name =template_name)    

                               
def showTeam(request , team_id):
        team = Team.objects.get(pk  = team_id )
        users =UserProfile.objects.filter(myteam = team)
        extra_context = {"team" :team , "users" : users}
        return default_render(request,
                              extra_context,
                               template_name ="team_profile.html")    

def add_classified(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
    if request.POST.has_key('city'):
        model_id = request.POST['city']
    else:
        model_id = 0
    return render_to_response('test.html', {'form':form,'model_id':model_id}, context_instance=RequestContext(request))
