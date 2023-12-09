from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myform/', views.my_form_view, name='my_form'),
    path('blog/', views.blog_post_list, name='blog_post_list'),
]