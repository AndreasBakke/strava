from django.shortcuts import render
from .models import Club, Distances
from django.http import HttpResponse
from .updates import update
import datetime
import time


# Create your views here.
def index(request):
    update()
    club_name_list = Club.objects.all()
    #template = loader.get_template('stravaleaderboard/index.html')
    last_updates = club_name_list[0].last_update
    dato = datetime.datetime.today()
    t = int(time.time())
    deltaT = t-last_updates
    startdate = datetime.datetime(2021, 1, 4)#update to 11 when publishing
    for i in range(1,11):
        if startdate + datetime.timedelta(days=7)*(1+i)>= dato >= startdate + datetime.timedelta(days=7)*i:
            currentWeek=i
    context = {
        'club_name_list' : club_name_list,
        'current_week': currentWeek,
        'deltaT': deltaT
    }
    return render(request, 'stravaleaderboard/index.html', context)

def weeks(request, club_name):
    club = Club.objects.get(name=club_name)
    context = {
        'club': club,
        
    }
    return render(request, 'stravaleaderboard/weeks.html', context)
