from django.shortcuts import render ,get_object_or_404
from django.views.generic import TemplateView , UpdateView, CreateView, ListView , DeleteView , DetailView , FormView
from .models import Product , SubCategory ,Order
from cart.forms import CartAddProductForm
from cart.cart import Cart
from decimal import Decimal
from . import models
from django.views import View
from zeep import Client

class ShopPage(ListView):
    
    model = Product
    context_object_name = "products"
    template_name = 'shop.html'
    paginate_by = 6
    
    
    
class BuyProducts(ListView , DetailView , DeleteView):    

    model = Product
    context_object_name = "products"
    template_name = 'single-product.html'
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cart_form'] = CartAddProductForm()
        return context
 
    
class Checkout(View):
    template_name = 'checkout.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        cart = Cart(self.request)
        for item in cart:
            item['update_product_count_form'] = CartAddProductForm(
                initial={
                    'product_count': item['product_count'],
                    'update': True
                }
            )
        return cart        
            

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, self.template_name, {'cart': cart})

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        order = models.Order.objects.create(customer=request.user)
        for item in cart:
            models.OrderItem.objects.create(
                order=order,
                product=item['product'],
                product_price=item['price'],
                product_count=item['product_count'],
                product_cost=Decimal(item['product_count']) * Decimal(item['price'])
            )
        # order.customer = request.user
        # order.save()
        cart.clear()
        return render(request, 'order_detail.html', {'order': order})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context
      
      
class Order(ListView):
    
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'
          
          
class to_bank(ListView):
    
    def get_queryset(self , request , order_id):
        
        order = get_object_or_404(models.Order , id=order_id)
        amount = 0
        order_items = models.OrderItem.objects.filter(order=order)
        
        for item in order_items: 
            amount += item.product_cast
            
        client = Client('https://www.zarinpal.com/pg/webGate/wsdl') 
        callback_url = 'http://http://127.0.0.1:8000/callback/'
        mobile = ''
        email = ''
        description = 'test'
        merchant = '**********************'
        result = client.service.PaymentRequest(merchant , amount , mobile, description , callback_url )
        
        if result.Status == 100 and len(result.Authority)==36:   
            pass      
    
    
    
    
      