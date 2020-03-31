from django.urls import path

from .views import (
    ReceiptView,
    HelpView,
)

app_name = 'after_sale'
urlpatterns = [
    path('receipt', ReceiptView.as_view(), name='receipt'),
    path('help', HelpView.as_view(), name='help'),
]