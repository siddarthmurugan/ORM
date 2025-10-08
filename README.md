# Ex02 Django ORM Web Application
## Date: 08-10-2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admins.py
from django.contrib import admin
from.models import car,carAdmin
admin.site.register(car,carAdmin)

models.py
from django.db import models
from django.contrib import admin
class car(models.Model):
    car_name = models.CharField()
    car_colour = models.CharField()
    release_date = models.DateField()

class carAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_colour', 'release_date')
```


## OUTPUT

![alt text](<Screenshot (14).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
