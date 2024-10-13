from django.urls import path
from . import views

urlpatterns = [
    path('drinks/', views.drink_list, name='drink_list'),  # URL: /drinks/
    path( 'drinks/<int:id>', views.drink_detail, )
]
