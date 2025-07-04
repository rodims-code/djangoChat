from datetime import datetime
from django.db import models

# Create your models here.

class Room (models.Model) : 
    name = models.CharField(max_length=1000000)

class Message(models.Model) : 
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now , blank = True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)