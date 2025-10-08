from django.db import models
from django.contrib import admin
class car(models.Model):
    car_name = models.CharField()
    car_colour = models.CharField()
    release_date = models.DateField()

class carAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_colour', 'release_date')