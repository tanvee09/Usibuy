from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length = 200,default = '')
    description = models.TextField(default = '')
    price = models.IntegerField(default = 0)
    author = models.CharField(max_length = 200, default = '')
    author_id = models.ForeignKey(User, on_delete = models.CASCADE,default = '')
    #author_id = models.ForeignKey(User, on_delete = models.CASCADE, default='')
    def __str__(self) :
        return self.title
