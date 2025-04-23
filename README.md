# Ex02 Django ORM Web Application
## Date: 23/04/2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![Screenshot 2025-04-23 192519](https://github.com/user-attachments/assets/6518a3ff-133f-4b8d-8757-fb0383f6e1ad)

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
models.py

from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
  name=models.CharField(max_length=100)
  ifsc=models.CharField(max_length=30)
  accno=models.IntegerField(primary_key='accno')
  loanamt=models.IntegerField()
  mobileno=models.IntegerField()

class BankloanAdmin(admin.ModelAdmin):
  list_display=('name','ifsc','accno','loanamt','mobileno')
admin.py

from django.contrib import admin
from.models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin) 




## OUTPUT
![Screenshot 2025-04-23 192354](https://github.com/user-attachments/assets/23844a0d-e494-4514-abec-1fb134e78ca4)

Include the screenshot of your admin page.


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
