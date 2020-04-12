from django.shortcuts import render
from .forms import NoteForm, NoteFullForm
from .models import Note, Image, Tag
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
import datetime
from django.views.generic import ListView
import json

def addNoteView(request):
    if request.method == "POST" and request.is_ajax():
        form = NoteFullForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            note_id = form.cleaned_data['note_id']
            text = form.cleaned_data['text']
            tags = form.cleaned_data['tags'].strip().split(",")
            if not note_id:
                note_obj = Note.objects.create(user=user,title=title,text=text) #create will create as well as save too in db.
            else:
                note_obj = Note.objects.get(id=note_id)
            for i in tags:
                tag_obj, created = Tag.objects.get_or_create(name=i)
                note_obj.tags.add(tag_obj) #it won't add duplicated as stated in django docs
            for f in files:
                Image.objects.create(note=note_obj,image=f)
            date = datetime.datetime.now().strftime('%B') +" "+ datetime.datetime.now().strftime('%d')+", "+datetime.datetime.now().strftime('%Y')
            response_data = {
            "id": note_obj.id,
            "title":title,
            "text":text,
            "last_mod": date
            }
            return getNoteResponseData(note_obj)
        else:
            print("Form invalid, see below error msg")
            print(form.errors)
    # if GET method form, or anything wrong then we will create blank form
    else:
        form = NoteFullForm()
    return HttpResponseRedirect('/')

def modifyNote(request):
    if request.is_ajax():
        note_id = request.body
        note_obj = Note.objects.get(id=note_id)
        tags = []
        for t in note_obj.tags.all():
            tags.append(t.name)
        return getNoteResponseData(note_obj,tags)

class TagFilterView(ListView):
    template_name = "base/home_page.html"
    model = Note
    
    def get_queryset(self):
        tags = self.kwargs['slug']
        queryset = super(TagFilterView, self).get_queryset()
        if self.request.user.is_authenticated:
            user = self.request.user
            queryset = Note.objects.filter(user_id=user.id).filter(tags__name=tags)
        else:
            queryset = Note.objects.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TagFilterView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            tagList = ""
            for q in getDistinctUserTags(self.request):
                tagList+=q.name+","
            context['tagList']=tagList[:len(tagList)-1]
        return context

def getDistinctUserTags(request):
    user = request.user
    return Tag.objects.filter(note__user=user).distinct()

def getNoteResponseData(note_obj,tags=None):
    response_data = {
            "id": note_obj.id,
            "title":note_obj.title,
            "text":note_obj.text,
            "tags": tags,
            "last_mod": note_obj.last_modified
            }
    return JsonResponse(response_data)