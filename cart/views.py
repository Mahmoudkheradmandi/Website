from django.shortcuts import render , get_object_or_404 , redirect 
from .cart import Cart
from shop.models import Product
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm



@require_POST 
def cart_add (request , product_id):
    
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid(): 
        form_data = form.cleaned_data
        cart.add(product=product, 
                 product_count=form_data['product_count'],
                 update_count=form_data['update'])
        
    return redirect(reverse('cart:cart_details'))


def cart_detail(request):
    
    cart = Cart(request)
    for item in cart:
        item['update_product_count_form'] = CartAddProductForm(
            initial={
                'product_count' : item['product_count'] , 
                'update' : True
            }
        )
    context = {'cart' : cart}
    return render(request , 'cart.html' , context)

def cart_remove(request , product_id):
    
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(reverse('cart:cart_details'))