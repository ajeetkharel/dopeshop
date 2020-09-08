from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Category

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    subcategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(default='default_item.jpg', upload_to='item_images')

    def __str__(self):
        return f"{self.subcategory}<{self.name}>"
    
    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk':self.pk, 'name':self.name})

