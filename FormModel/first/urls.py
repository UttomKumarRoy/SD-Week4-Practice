from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('about/', views.about, name='about'),
    path('model/', views.model, name='model'),
    path('delete/<int:roll>', views.delete_student, name='delete_student'),
   
]