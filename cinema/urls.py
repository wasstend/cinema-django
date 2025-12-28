from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.session_list, name='session_list'),
    path('session/<int:session_id>/buy/', views.buy_ticket, name='buy_ticket'),
    path('success/', views.success, name='success'), 
]
