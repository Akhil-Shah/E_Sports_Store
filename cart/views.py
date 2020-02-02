from django.shortcuts import render
from django.views import View

from .forms import ShippingForm

from django.http import HttpResponse 

from product.models import Game

# Create your views here.

class CartView(View):
    
    def get(self,request):

        test = Game.objects.all()

        context = {
            'test':test
        }

        return render(request,'cart_home.html',context)

class ShipView(View):

    def get(self,request):
        form = ShippingForm()

        try:
            details = []
            for key,value in request.session['ship_details'].items():
                details.append("{} - {}".format(key,value))
        except:
            details = "No information Added"

        context = {
            'form':form,
            'details':details
        }

        return render(request,'ship_details.html',context)

    def post(self,request):
        form = ShippingForm(request.POST)

        if form.is_valid():
            request.session['ship_details'] = form.cleaned_data
            form = ShippingForm()

        try:
            details = []
            for key,value in request.session['ship_details'].items():
                details.append("{} - {}".format(key,value))
        except:
            details = "No information Added"

        context = {
            'form':form,
            'details':details,
            'status':'Success !'
        }

        return render(request,'ship_details.html',context)


        
