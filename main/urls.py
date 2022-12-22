from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('results/',views.search ,name='search'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about_us'),
    path('sign-up/', views.singup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.ulogin, name='ulogin'),
    path('logout/', views.ulogout, name='ulogout'),
    path('terms-of-use/', views.terms_of_use, name='term-of-use'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    
]