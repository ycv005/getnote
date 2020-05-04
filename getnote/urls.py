"""getnote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import urls
from django.conf import settings
from django.conf.urls.static import static
from generic_views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePage.as_view() ,name='home_page'),
    path('', include(('accounts.urls','accounts'),namespace='accounts')),
    path('note/', include(('note.urls','note'),namespace='note')),
]

if settings.DEBUG:
# https://docs.djangoproject.com/en/3.0/howto/static-files/#serving-static-files-during-development
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "getNote Admin"
admin.site.site_title = admin.site.index_title = admin.site.site_header