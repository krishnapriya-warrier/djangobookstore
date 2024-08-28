from django.db import models

# Create your models here.
class Books(models.Model):

    Book_name = models.CharField(unique=True,max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.Book_name