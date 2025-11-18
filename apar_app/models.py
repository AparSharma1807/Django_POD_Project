from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_id} - {self.brand_name}"