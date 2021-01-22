from django.db import models
from category.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product/images/', blank=True)

    def __str__(self):
        return self.name
