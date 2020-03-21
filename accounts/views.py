from django.shortcuts import render
from django.views import generic
from .admin import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login_view') #checkout below, why using reverse_lazy
    template_name = 'accounts/signup.html'

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('') #checkout below, why using reverse_lazy
    template_name = 'accounts/login.html'

"""
Why to use the reverse_lazy
https://learndjango.com/tutorials/django-signup-tutorial
The reason is that for all generic class-based 
views, the urls are not loaded when the file is imported, 
so we have to use the lazy form of reverse to load them later when they're available.
"""