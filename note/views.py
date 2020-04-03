from django.shortcuts import render
from .forms import NoteForm, NoteFullForm
from .models import Note, Images
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def addNoteView(request):
    if request.method == "POST":
        form = NoteFullForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            note_obj = Note.objects.create(user=user,title=title,text=text) #create will create as well as save too in db.
            for f in files:
                Images.objects.create(note=note_obj,image=f)
        else:
            print("Form invalid")
    # if GET method form, or anything wrong then we will create blank form
    else:
        form = NoteFullForm()
    return HttpResponseRedirect('/')
