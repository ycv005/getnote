from django.contrib import admin

# Register your models here.
from .models import Note, Image, Tag

admin.site.register(Image)

class NoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Note, NoteAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # new

admin.site.register(Tag, TagAdmin)