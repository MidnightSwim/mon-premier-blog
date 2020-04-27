# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:28:45 2020

@author: Jean-Christophe
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]