from django.shortcuts import render, get_object_or_404 ,get_list_or_404, reverse, redirect
from django.views import View

from django.core.mail import send_mail

from .models import (
    ShippingAddress,
    ShippingProducts,
    ShippingTracker,
)

from product.models import (
    Item
)

import uuid

# Create your views here.

class ReceiptView(View):

    def get(self,request):

        cart = request.session['cart_details']
        item_list = []
        total_price = 0
        for item_id in cart:

            item_obj = Item.objects.get(pk=item_id)
            item_list.append(item_obj)

            total_price = total_price + item_obj.price

        try:
            details = []
            for key,value in request.session['ship_details'].items():
                details.append("{} - {}".format(key,value))
        except:
            details = ["No information Added"]
        
        
        temp = []
        for value in request.session['ship_details'].values():
            temp.append(value)

        uid = uuid.uuid4()
        ShippingAddress.objects.create(
            id=uid,
            first_name=temp[0],
            last_name=temp[1],
            email=temp[2],
            address=temp[3],
            phone=temp[4],
            country=temp[5],
            state=temp[6],
            city=temp[7],
            zip_code=temp[8],
            choice_field=temp[9] 
        )

        items = ""
        for item_id in cart:
            items = item_id  + "," + items
        ShippingProducts.objects.create(
            id = uid,
            product_list = items 
        )
        
        body = "Your Purchase UID: {}".format(uid)
        send_mail('ESS Purchase Order Confirmation', body, 'noreply@ESS.com',
                   [request.session['ship_details']['email'],],
                   fail_silently=True
        )

        ShippingTracker.objects.create(id=uid)

        context = {
            'item_list':item_list,
            'price':total_price,
            'ship_details':details,
            'uid':uid
        }

        return render(request, 'receipt.html',context)


class HelpView(View):

    def get(self,request):

        total_price = ""

        context = {
            'total_price':total_price
        }

        return render(request, 'help.html',context)


    def post(self,request):

        order_status = ""
        cancel_order = ""
        item_list = ""
        total_price = ""

        if 'order_status' in request.POST:
            uid = request.POST['UID']
            try:
                obj = get_object_or_404(ShippingTracker,id=uid)
                order_status = "Order will be delivered in {} days".format(obj.no_of_days)

                product_info = get_object_or_404(ShippingProducts,id=uid)
                temp = product_info.product_list
                temp = temp.split(',')[:-1]
                
                item_list = []
                total_price = 0
                for item_id in temp:

                    item_obj = Item.objects.get(pk=int(item_id))
                    item_list.append(item_obj)

                    total_price = total_price + item_obj.price
                
            except:
                order_status = "Invalid Purchase ID"

        if 'cancel_order' in request.POST:
            uid = request.POST['UID']
            try:

                obj = get_object_or_404(ShippingAddress,id=uid)
                obj.delete()

                obj = get_object_or_404(ShippingProducts,id=uid)
                obj.delete()

                obj = get_object_or_404(ShippingTracker,id=uid)
                obj.delete()

                cancel_order = "Order Successfully Cancelled"

                body = "Your Purchase UID: {} has been cancelled".format(uid)
                send_mail('ESS Purchase Order Cancellation', body, 'noreply@ESS.com', 
                          [request.session['ship_details']['email'],],
                           fail_silently=True
                )

            except:
                cancel_order = "Invalid Purchase ID"


        context = {
            'order_status':order_status,
            'cancel_order':cancel_order,
            'item_list':item_list,
            'total_price':total_price
        }

        return render(request, 'help.html',context)