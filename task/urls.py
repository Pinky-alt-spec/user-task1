from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('current/', views.current, name='dashboard-current'),
    path('current_delete/<int:pk>/', views.current_delete, name='dashboard-current-delete'),
    path('completed/', views.completed, name='dashboard-completed'),
    path('deleted/', views.deleted, name='dashboard-deleted'),
]
