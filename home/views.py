from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.views.generic import ListView, DetailView, CreateView
import urllib
from django import forms

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

class ItemCreateView(CreateView):
    model = Item
    condition = forms.CharField()
    fields = ['name', 'subcategory', 'price', 'usage', 'condition', 'description', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        
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
