from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','text']

class NoteFullForm(NoteForm):
    note_id = forms.IntegerField(required=False)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    tags = forms.CharField(max_length=50, required=False)

    class Meta(NoteForm.Meta):
        fields = NoteForm.Meta.fields + ['images','tags','note_id']