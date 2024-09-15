from django.db import models
from accounts.models import *
#from accounts.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    
    image = models.ImageField(default='media/default.jpg')
    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True) 
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags = TaggableManager()
    category =  models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    login_require = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    published_date =models.DateTimeField(null=True , default=0)
    created_date = models.DateTimeField(auto_now_add=True )
    updated_date = models.DateTimeField(auto_now=True )
    
    
    def __str__(self):
        return self.title
    
    def snippets(self):
        return self.content[:200] + '...'
    
    def get_absolute_url(self):
        return reverse ('blog:blog_single' , kwargs={'pid' : self.id})
    
         
class Comment(models.Model):
    
    post = models.ForeignKey(Post , on_delete=models.CASCADE , null=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    approveh = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=False , null=True)
    updated_date = models.DateTimeField(auto_now_add=False , null=True)
    
    
    def __str__(self):
        return self.name