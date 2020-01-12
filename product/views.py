from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View

from .models import (
    Game,
    Team,
    Item,
)

# Create your views here.

class GameView(View):
    
    def get(self,request):
        return render(request,'games.html',{})

class TeamView(View):
    
    def get(self,request,name):

        game_id = get_object_or_404(Game,name=name).id
        team_names = get_list_or_404(Team,game=game_id)

        context = {
            'team_names':team_names
        }
  
        return render(request,'teams.html',context)

class ItemView(View):

    def get(self,request,name):

        team_id = get_object_or_404(Team,name=name).id
        item_names = get_list_or_404(Item,team=team_id)

        context = {
            'item_names':item_names
        }

        return render(request,'items.html',context)


