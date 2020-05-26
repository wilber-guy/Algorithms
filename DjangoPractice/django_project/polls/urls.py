from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='poll-home'),
    path('about/', views.about, name='poll-about'),
]
