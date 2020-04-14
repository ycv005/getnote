from django.db import models
from django.db.models.signals import pre_save
from getnote import settings
import os
from django.template.defaultfilters import slugify

def user_directory_path(instance,filename):
    base_name = os.path.basename(filename)
    name,ext = os.path.splitext(base_name)

    return "note/user/"+ str(instance.note.user.id) + "/"+ str(instance.note.id)+ "/"+"IMG_" + str(instance.note.id)+ext
    
class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(null=False,unique=True)
    class Meta:
        ordering= ['name']

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField(null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False,unique=True)
    # color =
    # pin =
    # collaborator =

    class Meta:
        ordering= ['-last_modified']

    def getNoteTags(self):
        return self.tags.all()

    def __str__(self):
        return self.title

class Image(models.Model):
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path,null=True,blank=True)

    def __str__(self):
        return self.note.title + " Img"

def get_unique_slug(sender, instance, **kwargs):
    num = 1
    slug = slugify(instance.title)
    unique_slug = slug
    while Note.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    instance.slug=unique_slug

pre_save.connect(get_unique_slug,sender=Note)