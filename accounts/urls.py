from django.contrib import admin
from django.urls import path
from accounts import urls
from .views import SignUpView, LoginView, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/",LoginView.as_view(),name='login_page'),
    path("signup/",SignUpView.as_view(),name='signup_page'),
    path("logout/",logout_view,name='logout'),
    path("password/reset/", auth_views.PasswordResetView.as_view(), name='password_reset'),
    path("password/reset/done", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("reset/done", auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]