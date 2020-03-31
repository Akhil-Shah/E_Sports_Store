from django.db import models

# Create your models here.

class ShippingAddress(models.Model):

    id = models.UUIDField(primary_key = True,editable=False) 
    first_name = models.CharField(max_length=50,null=False,blank=False)
    last_name = models.CharField(max_length=50,null=False,blank=False)
    email = models.CharField(max_length=50,null=False,blank=False)
    address = models.CharField(max_length=50,null=False,blank=False)
    phone = models.CharField(max_length=50,null=False,blank=False)
    country = models.CharField(max_length=50,null=False,blank=False)
    state = models.CharField(max_length=50,null=False,blank=False)
    city = models.CharField(max_length=50,null=False,blank=False)
    zip_code = models.CharField(max_length=50,null=False,blank=False)
    choice_field = models.CharField(max_length=50,null=False,blank=False)


class ShippingProducts(models.Model):

    id = models.UUIDField(primary_key = True,editable=False)
    product_list = models.CharField(max_length=50,null=False,blank=False)


class ShippingTracker(models.Model):

    id = models.UUIDField(primary_key = True,editable=False)
    no_of_days = models.IntegerField(default=3,null=False,blank=False)