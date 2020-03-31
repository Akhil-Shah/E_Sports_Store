from django.urls import path

from .views import(
    GameView,
    TeamView,
    ItemView,
    YTView,
)

app_name = 'product'
urlpatterns = [
    path('', GameView.as_view(), name='index'),
    path('<name>/teams/', TeamView.as_view(), name='team_names'),
    path('<name>/items/', ItemView.as_view(), name='item_names'),
    path('yt/',YTView.as_view(), name='yt'),
]