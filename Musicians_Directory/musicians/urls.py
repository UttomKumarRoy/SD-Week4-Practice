from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('musicians/', views.musician_list, name='musician_list'),
    path('musicians/<int:musician_id>/', views.musician_detail, name='musician_detail'),
    path('musicians/<int:musician_id>/edit/', views.edit_musician, name='edit_musician'),
    path('albums/<int:album_id>/edit/', views.edit_album, name='edit_album'),
    path('albums/<int:album_id>/delete/', views.delete_album, name='delete_album'),
]
