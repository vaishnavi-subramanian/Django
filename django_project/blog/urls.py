from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    # /blog/
    path('', views.home, name='home'),

    # /blog/about/
    path('about/', views.about, name='about'),
]
