"""mytask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from accounts import views as accounts_view
from django.contrib.auth import views as auth_views
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),

    path('register/', accounts_view.register, name='account-register'),
    path('profile/', accounts_view.profile, name='account-profile'),
    path('profile-update/', accounts_view.profile_update, name='account-profile-update'),
    path('', auth_views.LoginView.as_view(template_name='task/accounts/login.html'), name='account-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='task/accounts/logout.html'), name='account-logout'),

    path('export/excel', views.export_users_xls, name='export_excel'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password-reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),


 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

