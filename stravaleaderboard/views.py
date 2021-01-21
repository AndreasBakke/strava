from django.shortcuts import render
from .models import Club, Distances
from django.http import HttpResponse
from .updates import update
import datetime
import time


# Create your views here.
def index(request):
    update()
    club_name_list = Club.objects.all().order_by('-currentpoints')
    #template = loader.get_template('stravaleaderboard/index.html')
    last_updates = club_name_list[0].last_update
    dato = datetime.datetime.today()
    t = int(time.time())
    deltaT = int((t-last_updates)/60)
    startdate = datetime.datetime(2021, 1, 11)#update to 19 when publishing
    for i in range(1,11):
        if startdate + datetime.timedelta(days=7)*(1+i)>= dato >= startdate + datetime.timedelta(days=7)*i:
            currentWeek=i
    totDist = 0
    for club in club_name_list:
        totDist += club.total_distance
    context = {
        'club_name_list' : club_name_list,
        'current_week': currentWeek,
        'deltaT': deltaT,
        'totDist': totDist
    }
    return render(request, 'stravaleaderboard/index.html', context)

def weeks(request, club_name):
    try:
        club = Club.objects.get(name=club_name)
    except:
        club = 1

    context = {
        'club': club,
        
    }
    return render(request, 'stravaleaderboard/weeks.html', context)

def about(request):
    context = {
        'a': 1,
    }
    return render(request, 'stravaleaderboard/about.html', context)
#def about(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)