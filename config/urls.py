from django import urls
from django.contrib import admin
from django.urls import path, include
from .views import index, memory
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index), 
    path('memory/', memory),
    path('everymemory/', include('everymemory.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
