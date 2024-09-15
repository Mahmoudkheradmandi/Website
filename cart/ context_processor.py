# from .cart import Cart

# def cart(request):
#     return {'cart': Cart(request)}

from .cart import Cart

def cart(request):
    cart = Cart(request)
    print(f"Cart contains {len(cart)} items")  # Debugging line
    return {'cart': cart}