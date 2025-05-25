from django.db import models
from django.utils import timezone


# Create your models here.
class chaivarirty(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI')
    ]
    name=models.TextField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)

    def __str__(self):
        return self.name
    

class ChaiDetails(models.Model):
    chai = models.OneToOneField(chaivarirty, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

def __str__(self):
        return f"Details of {self.chai.name}"