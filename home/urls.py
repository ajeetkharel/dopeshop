from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='shop-home'),
    path('contact/', views.contact, name='shop-contact'),
    path('item/<pk>-<name>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('update-item/<pk>-<name>/', views.ItemUpdateView.as_view(), name='item-update'),
    path('delete-item/<pk>-<name>/', views.ItemDeleteView.as_view(), name='item-delete'),
    path('users/<pk>-<first_name>/', views.OwnerItemListView.as_view(), name='owner-item-detail'),
    path('profile/', views.profile, name='owner-profile'),
    path('sell-item/new/', views.ItemCreateView.as_view(), name='item-create'),
]