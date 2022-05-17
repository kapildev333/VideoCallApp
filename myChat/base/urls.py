from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_lobby),
    path('room/', views.render_room),
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),

]
