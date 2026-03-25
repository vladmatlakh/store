from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField(max_length=300, blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    item_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)