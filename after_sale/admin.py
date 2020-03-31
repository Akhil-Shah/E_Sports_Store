from django.contrib import admin

# Register your models here.

from .models import (
    ShippingAddress,
    ShippingProducts,
    ShippingTracker,
)
# Register your models here.

admin.site.register([ShippingAddress,ShippingProducts,ShippingTracker])