# -*- coding: utf-8 -*-
from django.urls import path
from app import views


urlpatterns = [
    path('', views.List, name='list'),
    path('hitung/', views.Hitung, name='hitung'),
    path('view/<int:pk>', views.Detail, name='detail'),
    path('create/', views.Create, name='create'),
    path('update/<int:pk>/', views.Update, name='update'),
    path('delete/<int:pk>/', views.Delete, name='delete'),
    path('cari/', views.Cari, name='cari'),
    path('person_csv/', views.Person_csv, name='person_csv'),
    
]
