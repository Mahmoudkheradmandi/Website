from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView , ListView , DeleteView , DetailView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import User
from django.views.generic import TemplateView
from digi.models import Post


# class LoginViewSet(TemplateView):
    
#     template_name = 'login.html'
    
#     def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
#         return super().get(request, *args, **kwargs)
    
#     def get_context_data(self, *args ,**kwargs):
#         posts = Post.objects.all()
#         context = {'posts':posts}
#         return context
    
    
    
    
class LoginViewSet(ListView):
    
    model = Post
    context_object_name = "posts"
    template_name = 'login.html'
    # context_object_name = 'post'
    
    def get_queryset(self):
        return super().get_queryset()
    
    
    def get_context_data(self, *args ,**kwargs):
        posts = Post.objects.filter(status = 0)
        context = {'status':posts}
        return context
    