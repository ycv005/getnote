from django.shortcuts import render
from .forms import NoteForm, NoteFullForm
from .models import Note, Image, Tag
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
import datetime
from django.db.models import Q
from django.views.generic import ListView


def addNoteView(request):
    if request.method == "POST" and request.is_ajax():
        form = NoteFullForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            note_created = True
            user = request.user
            title = form.cleaned_data['title']
            note_id = form.cleaned_data['note_id']
            text = form.cleaned_data['text']
            tags = tagsInDic(form.cleaned_data['tags'].strip())
            tags_dic = tags.copy()
            if not note_id:
                note_obj = Note.objects.create(user=user,title=title,text=text) #create will create as well as save too in db.
                for k in tags.keys():
                    tag_obj, created = Tag.objects.get_or_create(name=k)
                    note_obj.tags.add(tag_obj) #it won't add duplicated as stated in django docs
            else:
                # handling all cases of the tags
                note_obj = Note.objects.get(id=note_id)
                for t in note_obj.tags.all():
                    if t.name not in tags_dic:
                        note_obj.tags.remove(t)
                    else: #deleting pre-existing element so that we could know what's new tags are
                        del tags_dic[t.name]
                for k,v in tags_dic.items():
                    tag_obj, created = Tag.objects.get_or_create(name=k)
                    note_obj.tags.add(tag_obj)
                note_created = False
            for f in files:
                Image.objects.create(note=note_obj,image=f)
            note_obj.title = title
            note_obj.text = text
            note_obj.save() #last_modified field won't update on chaning other model field, save() trigger change
            return getNoteResponseData(note_obj,tags,note_created)
        else:
            print("Form invalid, see below error msg")
            print(form.errors)
    # if GET method form, or anything wrong then we will create blank form
    else:
        form = NoteFullForm()
    return HttpResponseRedirect('/')

def modifyNote(request):
    if request.is_ajax() and request.method=="POST":
        note_id = request.body
        note_obj = Note.objects.get(id=note_id)
        tags = []
        for t in note_obj.tags.all():
            tags.append(t.name)
        note_created = False
        return getNoteResponseData(note_obj,tags,note_created)

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
            tags = getDistinctUserTags(self.request)
            for q in tags:
                tagList+=q.name+","
            context['tagList']=tagList[:len(tagList)-1]
            context['tags'] = tags
        return context

def getDistinctUserTags(request):
    user = request.user
    return Tag.objects.filter(note__user=user).distinct()

def getNoteResponseData(note_obj,tags,note_created):
    date = datetime.datetime.now().strftime('%B') +" "+ datetime.datetime.now().strftime('%d')+", "+datetime.datetime.now().strftime('%Y')
    note_obj.refresh_from_db()
    response_data = {
            "id": note_obj.id,
            "title":note_obj.title,
            "text":note_obj.text,
            "tags": tags,
            "last_mod": date,
            "note_created": note_created
            }
    return JsonResponse(response_data)


class SearchNote(ListView):
    """Class to render search results"""
    model = Note
    template_name = "base/home_page.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Note.objects.filter(
            Q(title__icontains=query) | Q(tags__name__icontains=query)
            # | Q(text__icontains=query) # will not work bcoz of encryption
        ).distinct()
        return queryset

def tagsInDic(tags):
    """Convert comma separated tags into dictionary"""
    last_ind = 0
    res = {}
    for i, c in enumerate(tags):
        if c == ',':
            res[tags[last_ind:i]] = 1
            last_ind = i + 1
    res[tags[last_ind:]] = 1
    return res
