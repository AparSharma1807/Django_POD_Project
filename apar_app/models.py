from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200 ,blank=True, null=True)
    image = models.ImageField(upload_to='uploads/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_id} - {self.brand_name}"