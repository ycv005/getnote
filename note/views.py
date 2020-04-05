from django.shortcuts import render
from .forms import NoteForm, NoteFullForm
from .models import Note, Image, Tag
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
import datetime

def addNoteView(request):
    if request.method == "POST" and request.is_ajax():
        form = NoteFullForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            tags = form.cleaned_data['tags'].strip().split(",")
            note_obj = Note.objects.create(user=user,title=title,text=text) #create will create as well as save too in db.
            for i in tags:
                tag_obj, created = Tag.objects.get_or_create(name=i)
                note_obj.tags.add(tag_obj)
            for f in files:
                Image.objects.create(note=note_obj,image=f)
            date = datetime.datetime.now().strftime('%B') +" "+ datetime.datetime.now().strftime('%d')+", "+datetime.datetime.now().strftime('%Y')
            response_data = {
            "title":title,
            "text":text,
            "last_mod": date
            }
            return JsonResponse(response_data)
        else:
            print("Form invalid, see below error msg")
            print(form.errors)
    # if GET method form, or anything wrong then we will create blank form
    else:
        form = NoteFullForm()
    return HttpResponseRedirect('/')
