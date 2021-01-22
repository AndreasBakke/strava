from .models import Club, Distances, Secret
import datetime
import time
import requests
import json
from decimal import Decimal

def exchange_credentials():
    a= Secret.objects.get(name = "strava")
    #header = {'Authorization': 'Bearer ' + '4f1202ea953c2401028d74661b892cd8b4dcbad7'}
#https://www.strava.com/oauth/token?client_id=59804&client_secret=6a9a2cd80fa5be0bffd26b90e92fb3b5463f6e0a&refresh_token=da1cf3fe14cd8d3abb8f058002f207397f730a35&grant_type=refresh_token
    req = requests.post("https://www.strava.com/oauth/token?client_id={}&client_secret={}&refresh_token={}&grant_type=refresh_token".format(a.client_id, a.client_secret, a.refresh_token)).json()
    #auth_url = "https://www.strava.com/api/v3/oauth/token"
    #req= requests.post(auth_url, data=payload).json()
    #req = requests.post("https://www.strava.com/oauth/token?client_id={}&client_secret={}&grant_type=refresh_token&refresh_token={}".format(a.client_id, a.client_secret, a.refresh_token)).json()
    #update:
    a.access_token = req['access_token']
    a.refresh_token = req['refresh_token']
    a.save()

def update_distances():
    currentWeek = 0
    club_name_list = Club.objects.all()
    t = int(time.time())
    a= Secret.objects.get(name = "strava")
    dato = datetime.datetime.today()
    startdate = datetime.datetime(2021, 1, 18)#update to 18 when publishing
    for i in range(1,10):
        if startdate + datetime.timedelta(days=7)*(1+i)>= dato >= startdate + datetime.timedelta(days=7)*i:
            currentWeek =i

    for club in club_name_list:
        data = requests.get("https://www.strava.com/api/v3/clubs/{}/activities?access_token={}&per_page=200&after={}".format(club.club_id, a.access_token, club.last_update)).json()
        newDistance = 0
        for i in data:
            if i["type"] == "Ride":
                newDistance += Decimal(i["distance"]/3000)
            else:
                newDistance += Decimal(i["distance"]/1000)
        if currentWeek== 0:
            club.last_update = t
            club.save()
        else:     
            d = club.distances_set.get(week = currentWeek)
            d.distance += newDistance
            d.points = d.distance / club.members
            club.currentpoints = d.points
            d.save()
            club.last_update = t
            club.save()
    

def Create_check_Clubs():
    a= Secret.objects.get(name = "strava")
    parameters = {
    "access_token": a.access_token, "per_page": 200}
    club_name_list = Club.objects.all()
    base_url = "https://www.strava.com/api/v3/"
    endpoint = "athlete/clubs"
    url = base_url + endpoint
    data = requests.get(url, params=parameters).json()
    for i in data:
        clubid = i['id']
        if Club.objects.filter(club_id= clubid).exists():
            g =2
        else:
            c = Club(name = i['name'], club_id = clubid)
            c.save()
            for i in range(1,10):
                a = c.distances_set.create(week=i)
                a.save() 
            


def update():
    
    
    #check if all clubs exist:

    t = int(time.time())
    club_name_list = Club.objects.all()
    try:
        updatetime = club_name_list[0].last_update
    except:
        exchange_credentials()
        Create_check_Clubs() 
        update_distances()
        updatetime = club_name_list[0].last_update


    if (t-updatetime)>18:
        exchange_credentials()
        Create_check_Clubs() 
        update_distances()

    
    club_name_list = Club.objects.all()
    for club in club_name_list:
        totalDistance = 0
        for dist in club.distances_set.all():
            totalDistance +=  dist.distance 
        club.total_distance = totalDistance
        club.save()
  
    #Pseudo: Hvis dato er mellom ukestart og ukeslutt 1, update week1....