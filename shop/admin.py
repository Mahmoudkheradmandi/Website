from django.contrib import admin
from .models import *


class ProductAdminPage(admin.ModelAdmin):
    
    
    list_display = ['id' ,'name' ,'price' , 'quantity' , 'status']
    list_display_links = ['id' , 'name' , 'price' ]
    
admin.site.register(Product , ProductAdminPage)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Invoice)
admin.site.register(Transaction)
