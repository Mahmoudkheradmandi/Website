
from django.db import models


class User(models.Model):
    
    '''
    custom User Model for our app
    '''
    email = models.EmailField(max_length=254 , unique=True)
    phone_number = models.CharField( null=True , blank=True ,max_length=50)
    first_name = models.CharField(max_length=50 , blank=True , null=True)
    last_name = models.CharField(max_length=50 , blank=True , null=True)
    
    
    def __str__(self):
        return self.email
    
    