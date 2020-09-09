from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='shop-home'),
    path('contact/', views.contact, name='shop-contact'),
    path('item/<pk>-<name>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('users/<pk>-<first_name>/', views.OwnerItemListView.as_view(), name='owner-item-detail'),
    path('sell-item/new/', views.ItemCreateView.as_view(), name='item-create'),
]