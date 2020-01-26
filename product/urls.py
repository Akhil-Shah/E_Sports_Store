from django.urls import path

from .views import(
    GameView,
    TeamView,
    ItemView,
)

app_name = 'product'
urlpatterns = [
    path('games/', GameView.as_view(), name='index'),
    path('<name>/teams/', TeamView.as_view(), name='team_names'),
    path('<name>/items/', ItemView.as_view(), name='item_names'),
]