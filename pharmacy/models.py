from django.db import models

# pharmacy/models.py
from django.db import models
from accounts.models import PharmacyProfile 

class Medicine(models.Model):
   
    
    pharmacy = models.ForeignKey(
        PharmacyProfile, 
        on_delete=models.CASCADE, 
        related_name='medicines'  
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    in_stock = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.name} - ({self.pharmacy.user.username})"