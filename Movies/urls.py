from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.movie_list, name='movies-list'),
    path('show/<int:pk>/', views.movie_detail, name='movies-detail'),
    path('show/<int:pk>/vote/<int:pk_comment>/<str:up_or_down>/', views.vote, name='comment-vote'),
    path('delete/<int:pk>/', views.movie_delete, name='movies-delete'),
    path('add/', views.movie_create, name='movies-create'),
]