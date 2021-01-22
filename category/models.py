from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
