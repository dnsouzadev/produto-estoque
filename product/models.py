from django.db import models

# Create your models here.
class Product(models.Model):
    CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não')
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    available = models.CharField(max_length=1, choices=CHOICES, default='S')
    photo = models.ImageField(upload_to='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

