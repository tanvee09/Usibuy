from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=500, default='')
    price = models.IntegerField(default=0)
    author = models.CharField(max_length=200, default='')
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to="media/profile_pics")

    def __str__(self):
        return self.title
