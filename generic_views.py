from django.views.generic import ListView
from note.models import Note, Tag

class HomePage(ListView):
    template_name = "base/home_page.html"
    model = Note
    
    def get_queryset(self):
        queryset = super(HomePage, self).get_queryset()
        if self.request.user.is_authenticated:
            user = self.request.user
            queryset = Note.objects.filter(user_id=user.id)
        else:
            queryset = Note.objects.none()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        user = self.request.user
        tagList = ""
        for q in Tag.objects.filter(note__user=user).distinct():
            tagList+=q.name+","
        context['tagList']=tagList[:len(tagList)-1]
        return context
    