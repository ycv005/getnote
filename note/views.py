from django.shortcuts import render
from .forms import NoteForm
from .models import Note
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def addNoteView(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            print("here is the form",form)
            user = request.user
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            note_obj = Note.objects.create(user=user,title=title,text=text)
            # after calling obj.save, then database will be modified
            note_obj.save()
            # return HttpResponseRedirect('/')
    # if GET method form, or anything wrong then we will create blank form
    else:
        form = NoteForm()
    return HttpResponseRedirect('/')
