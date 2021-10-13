from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('current/', views.current, name='dashboard-current'),
    path('completed/', views.completed, name='dashboard-completed'),
    path('deleted/', views.deleted, name='dashboard-deleted'),
    path('profile/', views.profile, name='profile'),
]
