from django.db import models
from getnote import settings

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField(null=True,blank=True)
    # color =
    # pin =
    # tag =
    # collaborator =
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# class Images(models.Model):
