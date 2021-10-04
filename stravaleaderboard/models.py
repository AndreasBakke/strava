from django.db import models
from jsonfield import JSONField

# Create your models here.
""" class Activity(models.Model):
    activity = models.JSONField()
    #resource_state = models.IntegerField()
    #athlete_name = models.TextField(max_length=200)
    #run_name = models.TextField(max_length=200)
    #distance = models.DecimalField(max_digits=200, decimal_places=1)
    #moving_time = models.IntegerField()
    #elapsed_time: models.IntegerField()
    #total_elevation_gain = models.DecimalField(max_digits=200, decimal_places=1)
    #activity_type = models.TextField(max_length=200)
    def __str__(self):
        return str(self.id) """

class Club(models.Model): 
    name = models.TextField(max_length=200)
    club_id = models.TextField(max_length=15)
    last_update = models.IntegerField(default=1615158000)
    total_distance = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    members = models.IntegerField(default = 1)
    currentpoints = models.DecimalField(max_digits=200, default=0, decimal_places=1)
    percentage = models.DecimalField(max_digits=200, default=0, decimal_places=1)
    def __str__(self):
        return str(self.name)


class Distances(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    week = models.IntegerField()
    distance = models.DecimalField(max_digits=200, decimal_places=1, default=0)
    points = models.DecimalField(max_digits=200, default=0, decimal_places=1)
    def __str__(self):
        return self.club.name + 'week'+ str(self.week)

class Secret(models.Model):
    name = models.TextField(max_length=200, default="aa")
    client_id = models.IntegerField(default=0)
    client_secret = models.TextField(max_length=200)
    access_token = models.TextField(max_length=200)
    refresh_token = models.TextField(max_length=200)
    def __str__(self):
        return str(self.name)