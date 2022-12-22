from django.urls import path ,include
from . import views


urlpatterns = [
    path('', views.games_home, name='download_home'),
    path('<int:myid>/<str:mynam>',views.games_download , name='download_game'),
    path('<int:myid>/<str:mynam>/download',views.games_d_download , name='download_game_2'),
    path('11/12/gamepoastcomment/',views.postGcomment , name='post_game_comment'),
    path('<str:mycat>/',views.games_categary , name='download_game_cat'),
]