from django.urls import path

# Local
<<<<<<< HEAD
from .views import GameView, about, GameListView, MainView


urlpatterns = [
    path('<int:game_id>/', GameView.as_view()),
    path('list/', GameListView.as_view()),
    path('', MainView.as_view()),
    path('about/', about),
=======
from .views import index, about, get_game , games


urlpatterns = [
    path('', index),
    path('about/', about),
    path('<int:game_id>/', get_game),
    path('game/', games)
>>>>>>> 984084a2207a36f6070aed74c596a38203909407
]
