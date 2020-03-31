from django.urls import path

from .views import(
    CartView,
    ShipView,
    FeedView,
    payment_done,
    payment_canceled,
)

app_name = 'cart'
urlpatterns = [
    path('view/', CartView.as_view(), name='cart'),
    path('shipping/', ShipView.as_view(), name='shipping'),
    path('feedback/', FeedView.as_view(), name='feedback'),
    path('done/', payment_done, name='done'),
    path('canceled/', payment_canceled, name='cancelled'),
]