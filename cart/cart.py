from django.conf import settings
from shop.models import Product
from decimal import Decimal



class Cart :
    
    def __init__(self , request):
        
        """ Manage cart app  """
        
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID) # session cart in database 
        if not cart : 
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
        
    def add(self , product, product_count=1, update_count=False ):
         
        ''' Add one or many Product in cart ,
            we just save id and ... in dict
            
        '''
        
        product_id = str(product.id)
        if product_id not in self.cart : 
            self.cart[product_id] = {'product_count' : 0 , 
                                     'price' : str(product.price)}  
        if update_count :
            self.cart[product_id]['product_count'] = product_count
        else : 
            self.cart[product_id]['product_count'] += product_count
        self.save()
        
   
        
    def save(self):
        ''' Save all order steps '''
        self.session[settings.CART_SESSION_ID] = self.cart        
        self.session.modified = True  
        
        
    def __iter__(self):
        
        ''' show all product in cart '''
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        for product in products:
            self.cart[str(product.id)]['product'] = product
        
        """ sum Total one product """    
        for item in self.cart.values():
            item['price'] =  Decimal(item['price'])
            item['total_price'] = item['price'] * item['product_count']   
            yield item  
        # return self.cart.values()                 
    
    def __len__(self):
        """ Count all items in the cart """
        return sum(item['product_count'] for item in self.cart.values())
    
    def get_total_price(self):
        
        """ sum Total all products """ 
        return sum(Decimal(item['price']) * item['product_count'] for item in self.cart.values())
           
            
    def remove(self , product):
        
        product_id = str(product.id)
        if product_id in self.cart :
            del self.cart[product_id]
            self.save() 
           
                     