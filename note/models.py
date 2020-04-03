from django.db import models
from getnote import settings
import os

def user_directory_path(instance,filename):
    base_name = os.path.basename(filename)
    name,ext = os.path.splitext(base_name)

    return "note/user/"+ str(instance.note.id) + "/"+"IMG_" + str(instance.pk)+ext

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

    class Meta:
        ordering= ['-last_modified']

    def __str__(self):
        return self.title

class Images(models.Model):
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path,null=True,blank=True)

    def __str__(self):
        return self.note.title + " Img"