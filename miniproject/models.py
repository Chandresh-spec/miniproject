from django.db import models
from django.utils import timezone


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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
    ingredients = models.ManyToManyField(Ingredient, related_name='chai_varieties')

    def __str__(self):
        return self.name
    

class ChaiDetails(models.Model):
    chai = models.OneToOneField(chaivarirty, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
          return f"Details of {self.chai.name}"
    

class ChaiReview(models.Model):
    chai = models.ForeignKey(chaivarirty, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name}'s review on {self.chai.name}"