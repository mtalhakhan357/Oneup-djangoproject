"""oneup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'ONE UP ADMIN'
admin.site.site_title = 'ONE UP ADMIN'
admin.site.index_title =  'Welcome To Admin Pannel'
urlpatterns = [
    path('developer-area/', admin.site.urls),
    path('', include('main.urls') , name='home'),
    path('games/',include('games.urls'),name="games"),
    path('apps/',include('app_s.urls'),name='apps'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
