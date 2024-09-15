from django.urls import path , include
from . import views



urlpatterns = [
    
    path('login/' , views.LoginViewSet.as_view() , name='login'),
]