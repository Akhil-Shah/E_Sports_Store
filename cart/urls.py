from django.urls import path


from .views import(
    CartView,
    ShipView,
)

app_name = 'cart'
urlpatterns = [
    path('view/', CartView.as_view(), name='cart'),
    path('shipping/', ShipView.as_view(), name='shipping')
]