from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    discount = models.FloatField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_set = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail',kwargs={'pk':self.pk})
