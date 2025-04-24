from django.contrib import admin
from django.urls import path
from . import views
from main import models
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name='home'),
    path("production", views.production, name='production'),
    path("services", views.services, name='services'),
    path("contacts", views.contacts, name='contacts'),
    path("our_works", views.our_works, name='our_works'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
