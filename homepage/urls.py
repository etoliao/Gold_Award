from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('', views.post_list, name='post_list'),
]