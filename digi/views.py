from django.shortcuts import render , redirect
from digi.models import Post , Comment
from shop.models import Product , SubCategory , MainCategory
from django.views.generic import TemplateView , UpdateView, CreateView, ListView , DeleteView , DetailView , FormView
from .forms import PostForm

from django.urls import reverse_lazy

# class HomePage(ListView):
    
#     model = Post
#     context_object_name = "posts"
#     template_name = 'index.html'
#     paginate_by = 3
    
#     def get_context_data(self, *args ,**kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['posts'] = Post.objects.filter(status=1)[:3]
#         context['products'] = Product.objects.filter(status=1)[:6]
#         return context
    
    
def home_page (request):
    
    posts = Post.objects.filter(status=1)
    products = Product.objects.filter(status=1) 
    context = {'posts': posts  , 'products' : products}
    
    return render(request , 'index.html' , context)
    


def detail_post(request , pk):
    
    posts = Post.objects.get(id=pk , status = 1)
    sub_category = SubCategory.objects.all()
    main_category = MainCategory.objects.all()
    
    context = {'posts': posts,
               'sub_category' : SubCategory,
               'main_category' : MainCategory}
    
    print(context)
    return render(request , 'single-posts.html' , context)


def post_page(request):
    
    posts = Post.objects.filter(status=1).order_by('-id')
    context = {'posts': posts}
    return render(request , 'posts.html' , context)

    
    
# class DetailPost(DetailView):
    
#     model = Post
#     template_name = 'single-posts.html'
#     context_object_name = 'posts'
    
# class PostPage(ListView):
    
#     model = Post
#     template_name = 'posts.html'
#     context_object_name = 'posts'
#     paginate_by = 6
    
   
# class Contact(CreateView):
    
#     model = Comment
#     template_name = 'contact.html'
#     context_object_name = 'comment'
#     fields = ['name' , 'email' , 'subject' , 'message']
#     success_url = reverse_lazy('Home')
    
    
    
# class ContactComment(CreateView):
    
#     model = Comment
#     template_name = 'blog/blog-single.html'
#     context_object_name = 'comment'
#     fields = ['name' , 'email' , 'subject' , 'message']
#     success_url = reverse_lazy('Detail')
    
#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)
        
#     def get_success_url(self):
#         return reverse_lazy('Detail', kwargs={'pk': self.kwargs['pk']})
    
    
# class PostForm(UpdateView):
#     model = Post
#     form_class = PostForm
#     success_url = reverse_lazy('Home')
    

# class DeletePost(DeleteView):
    
#     model = Post
#     form_class = PostForm
#     success_url = reverse_lazy('Home')  
    
    
# class About(ListView):
          
#     model = Post
#     context_object_name = "posts"
#     template_name = 'about.html'
    

    