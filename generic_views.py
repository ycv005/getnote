from django.views.generic import ListView
from note.models import Note

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