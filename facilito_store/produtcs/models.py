from django.db import models

class product(models.Model):
    title = models.CharField(max_length=50)
    description =models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    created_at = models.DateField(auto_now_add=True)
