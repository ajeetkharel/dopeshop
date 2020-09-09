from django.contrib import admin
from django.urls import path
from . import views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.ItemListView.as_view(), name='shop-home'),
    path('contact/', views.contact, name='shop-contact'),
    path('item/<pk>-<name>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('update-item/<pk>-<name>/', views.ItemUpdateView.as_view(), name='item-update'),
    path('delete-item/<pk>-<name>/', views.ItemDeleteView.as_view(), name='item-delete'),
    path('users/<pk>-<first_name>/', views.OwnerItemListView.as_view(), name='owner-item-detail'),
    path('profile/', user_views.profile, name='owner-profile'),
    path('sell-item/new/', views.ItemCreateView.as_view(), name='item-create'),
]  + static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)