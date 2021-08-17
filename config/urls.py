"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
    # path(주소, 뷰, 주소의 별명)
    # 1차 -> 2차 -> 3차
    # http://127.0.0.1/wordboard/?
    # http://127.0.0.1/중앙창구/외과
    # http://127.0.0.1/즁앙창구/내과
]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
