from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('current/', views.current, name='current'),
    path('completed/', views.completed, name='completed'),
    path('deleted/', views.deleted, name='deleted'),
    path('profile/', views.profile, name='profile'),
]
