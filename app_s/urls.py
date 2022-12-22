from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.apps_home, name='download_home'),
    path('11/12/apppoastcomment/',views.postAcomment , name='post_game_comment'),
    path('<int:myid>/<str:mynam>',views.apps_download , name='download_app'),
    path('<int:myid>/<str:mynam>/download',views.apps_d_download , name='download_app'),
    path('<str:mycat>/',views.apps_categary , name='download_app_cat'),
    path('<str:mycat>/',views.apps_categary , name='developer cats'),
]