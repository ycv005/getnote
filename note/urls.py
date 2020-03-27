from django.urls import path
from accounts import urls
from .views import addNoteView

urlpatterns = [
    path("add/",addNoteView,name='add_note'),
]