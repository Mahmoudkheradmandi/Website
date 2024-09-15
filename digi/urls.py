


from django.urls import path , include
from . import views

app_name = 'digi'

urlpatterns = [
    
    path('' , views.home_page , name='Home'),
    # path('posts' , views.PostPage.as_view() , name='posts'),
    path('<int:pk>/', views.detail_post , name='detail'),
    path('posts/', views.post_page , name='posts'),
    # path('contact/', views.Contact.as_view() , name='contact'),
    # path('comment/<int:pk>', views.ContactComment.as_view() , name='comment'),
    # path('<int:pk>/edit/', views.PostForm.as_view() , name='edit'),
    # path('<int:pk>/delete/', views.DeletePost.as_view() , name='delete '),
    # path('about/', views.About.as_view() , name='about'),
]