from django.db import models
from getnote import settings

# Create your models here.

class Note(models.Model):
    uesr = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=1000,null=True,blank=True)
    # color =
    # pin =
    # tag = 
    # collaborator = 
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

# class Images(models.Model):