from django.db import models


class Cars(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    info = models.TextField()
    images = models.ImageField(upload_to='car_images/')
    status = models.CharField(max_length=20)
    rating = models.FloatField()
    other = models.TextField()