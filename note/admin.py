from django.contrib import admin

# Register your models here.
from .models import Note, Images

admin.site.register(Note)
admin.site.register(Images)