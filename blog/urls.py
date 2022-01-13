from django.urls import path
from . import views #imports blog app views.py bc they are in same folder u can use.

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]
