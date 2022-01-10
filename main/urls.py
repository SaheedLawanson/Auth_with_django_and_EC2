from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home2"),
    path("<int:id>", views.todos, name="index"),
    path('create/', views.create, name="create"),
    path('view/', views.view, name="view"),
]