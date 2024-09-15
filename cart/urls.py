from django.urls import path , include
from .views import cart_detail , cart_add , cart_remove

app_name = 'cart'

urlpatterns = [
    
    path('' , cart_detail, name='cart_details'),
    path('add/<int:product_id>/' , cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    
]