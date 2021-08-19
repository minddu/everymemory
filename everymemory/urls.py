from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", main, name="main"), 
    path("memory/", memory1, name="memory1"),
    path("memory/testsheet/", testsheet, name="testsheet"),
    path("study/", study, name="study"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 