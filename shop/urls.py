from django.urls import path , include
from . import views


app_name = 'shop'

urlpatterns = [
    
    path('' , views.ShopPage.as_view(), name='shop'),
    path('<int:pk>/' , views.BuyProducts.as_view(), name='detail_shop'),
    path('checkout/' , views.Checkout.as_view(), name='checkout'),
    path('order/' , views.Order.as_view(), name='order'),
]