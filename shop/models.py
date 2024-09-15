from django.db import models
from accounts.models import User

class Product(models.Model): 
    
    price = models.DecimalField(max_digits=10, decimal_places=0)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    category = models.ManyToManyField('SubCategory')
    status = models.BooleanField(default=False)
    quantity = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return self.name
    

class MainCategory(models.Model):
    
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    main_category =models.ForeignKey(MainCategory , on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name    
    
    
    
class Order(models.Model):
    
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    order_data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
class OrderItem(models.Model):    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)        
    product = models.ForeignKey(Product ,null=True , on_delete=models.SET_NULL)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product_cast = models.DecimalField(max_digits=10, decimal_places=0)
    product_count = models.PositiveIntegerField()
    
    def __str__(self):
        return self.id
    
class Invoice(models.Model):    
    order = models.ForeignKey(Order,null=True , on_delete=models.SET_NULL)        
    invoice_data = models.DateField(auto_now_add=True)
    Authority = models.CharField( max_length=200 , blank=True , null=True)

    def __str__(self):
        return self.id
class Transaction(models.Model): 
    
    STATUS_CHOICES = (
        
        ('pending' , 'Pending'),
        ('failed' , 'Failed'),
        ('completed' , 'Completed'),
        
    )  
    
    invoice = models.ForeignKey(Invoice, null=True ,on_delete=models.SET_NULL) 
    transaction_data = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=10 , choices=STATUS_CHOICES , default='pending')
    
    def __str__(self):
        return self.id