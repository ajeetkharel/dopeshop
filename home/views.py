from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import urllib
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def contact(request):
    return render(request, 'home/contact.html', context={'title':'Contact Us'})

class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'home/home.html' #app/model_viewtype.html
    ordering = ['-date_added']
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ItemListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Home'
        return context

class ItemDetailView(DetailView):
    model = Item


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    condition = forms.CharField()
    fields = ['name', 'subcategory', 'price', 'usage', 'condition', 'description', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    condition = forms.CharField()
    fields = ['name', 'subcategory', 'price', 'usage', 'condition', 'description', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.owner:
            return True
        return False

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = '/'
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.owner:
            return True
        return False


class OwnerItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'home/owner_items_list.html'
    ordering = ['-date_added']

    def get_queryset(self):
        return Item.objects.filter(owner_id=self.kwargs['pk'])

    def get_context_Announcedata(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(OwnerItemListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Items by ' + self.model.owner.first_name
        return context

@login_required
def profile(request):
    return render(request, 'users/profile.html', context={'title':'Profile'})
