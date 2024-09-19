from django.db import models

# Create your models here.


class Car(models.Model):
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self) -> str:
         return f'{self.model} ({self.price})'


class Football(models.Model):
    name = models.CharField(max_length=30)
    team = models.TextField()


    def __str__(self) -> str:
         return f'{self.name} ({self.team})'

    
class Ufc(models.Model):
    fighter = models.CharField(max_length=50)
    rating = models.IntegerField()    


    def __str__(self) -> str:
         return f'{self.fighter} ({self.rating})'
    