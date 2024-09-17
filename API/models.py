from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Books(models.Model):

    Book_name = models.CharField(unique=True,max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.Book_name
    
class Carts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Book = models.ForeignKey(Books,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    
    Book = models.ForeignKey(Books,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment