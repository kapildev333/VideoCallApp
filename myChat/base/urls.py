from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_lobby),
    path('room/', views.render_room),
]
