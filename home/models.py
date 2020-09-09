from django.db import models
from django.utils import timezone
from users.models import Owner
from django.urls import reverse
from users.models import Category

USAGE_CHOICES = (
    ('N', 'New'),
    ('U', 'Used'),
)

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    usage = models.CharField(max_length=1, choices=USAGE_CHOICES)
    condition = models.CharField(max_length=255, blank=True)
    subcategory = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(default='default_item.jpg', upload_to='item_images')

    def __str__(self):
        return f"{self.subcategory}<{self.name}>"
    
    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk':self.pk, 'name':self.name})

