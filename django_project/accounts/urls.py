from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'Accounts'

urlpatterns = [
    # /accounts/register/
    path('register/', views.register, name='register'),

    # /accounts/profile/
    path('profile/', views.profile, name='profile'),

    # /accounts/login/
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # /accounts/logout/
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
