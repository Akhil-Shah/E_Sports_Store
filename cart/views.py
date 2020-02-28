from django.shortcuts import render, get_object_or_404 ,get_list_or_404, reverse, redirect
from django.views import View

from .forms import ShippingForm

from django.http import HttpResponse 

from product.models import (
    Game,
    Team,
    Item,
)

from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')
 
 
@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html')

class CartView(View):
    
    def get(self,request):

        if 'cart_details' not in request.session:
            print("Nothing")
        else:
            cart = request.session['cart_details']
            item_list = []
            for item_id in cart:

                item_obj = Item.objects.get(pk=item_id)
                item_list.append(item_obj)
     

        item_names = ""
        for each in item_list:
            item_names = item_names + each.name + " "

        host = request.get_host()
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': '500',
            'item_name': item_names,
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host,
                                            reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                            reverse('cart:done')),
            'cancel_return': 'http://{}{}'.format(host,
                                            reverse('cart:cancelled')),
        }

        form = PayPalPaymentsForm(initial=paypal_dict)

        context = {
            'item_list':item_list,
            'form':form
        }
 
        return render(request,'cart_home.html',context)

    def post(self,request):

        item_id = request.POST.get('item_id')

        saved_list = request.session['cart_details']
        saved_list.remove(item_id)
        request.session['cart_details'] = saved_list

        return redirect('cart:cart')

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


        
