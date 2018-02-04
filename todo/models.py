from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=100)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
