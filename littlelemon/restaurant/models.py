from django.db import models
import datetime

# Create your models here.
class Booking(models.Model):
    Name=models.CharField(max_length=255)
    No_of_guests=models.IntegerField(max_length=6)
    BookingDate=models.DateTimeField(default=datetime.datetime.now)

class Menu(models.Model):
    def __str__(self):
        return f'{self.Title} : {self.Price}'
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=6,decimal_places=2)
    Inventory=models.IntegerField(max_length=5)