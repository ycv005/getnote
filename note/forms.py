from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','text']

class NoteFullForm(NoteForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)

    class Meta(NoteForm.Meta):
        fields = NoteForm.Meta.fields + ['images',]