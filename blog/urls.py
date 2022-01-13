from django.urls import path
from . import views #imports blog app views.py bc they are in same folder u can use.

app_name = 'blog' #now when u want to reference any url from here you have to specify "blog:x"

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
