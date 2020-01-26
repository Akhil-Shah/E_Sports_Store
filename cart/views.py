from django.shortcuts import render
from django.views import View

from product.models import Game
# Create your views here.

class CartView(View):
    
    def get(self,request):

        test = Game.objects.all()

        context = {
            'test':test
        }

        return render(request,'cart_home.html',context)
