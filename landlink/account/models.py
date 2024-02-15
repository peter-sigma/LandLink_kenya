from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    BUYER = 'buyer'
    SELLER = 'seller'
    LAWYER = 'lawyer'
    USER_TYPES = [
        (BUYER, 'Buyer'),
        (SELLER, 'Seller'),
        (LAWYER, 'Land Lawyer'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default=BUYER)

    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"

