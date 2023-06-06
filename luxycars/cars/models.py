from django.db import models
from django.urls import reverse


class Status(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    status = models.CharField(max_length=20, verbose_name='Status of the Car')
    images = models.ImageField(upload_to='car_images/', null=True)
    about = models.TextField()

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('car_status', kwargs={'status_slug': self.slug})

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status of the Car"


class Cars(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    brand = models.CharField(max_length=100, verbose_name='Brand')
    model = models.CharField(max_length=100, verbose_name='Model')
    type = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Price')
    about = models.TextField()
    images = models.ImageField(upload_to='car_images/')
    rating = models.FloatField()
    other = models.TextField()
    is_published = models.BooleanField(default=True, verbose_name="Published")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Status')

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})

    class Meta:
        verbose_name = "Cars"
        verbose_name_plural = "Cars"
        ordering = ['slug']

