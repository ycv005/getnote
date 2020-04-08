from django.urls import path
from accounts import urls
from .views import addNoteView, TagFilterView

urlpatterns = [
    path("add/",addNoteView,name='add_note'),
    path("tag/<slug:slug>/",TagFilterView.as_view(),name='tag_filter'),
]