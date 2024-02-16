from django.db import models
from account.models import CustomUser

class Land(models.Model):
    LOCALITY_CHOICES = [
        ('rural', 'Rural'),
        ('semi_urban', 'Semi-Urban'),
        ('urban', 'Urban'),
    ]

    image = models.ImageField(upload_to='land_images/')
    title = models.CharField(max_length=100)
    locality = models.CharField(max_length=20, choices=LOCALITY_CHOICES, default='rural')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'seller'})
    location = models.CharField(max_length=100, blank=True, null=True, help_text="Enter the latitude and longitude coordinates (e.g., 'latitude,longitude') for the location of the land.")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
