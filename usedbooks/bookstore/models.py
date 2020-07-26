from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STREAM_CHOICES = {
    ('Engineering', 'Engineering'),
    ('Medical', 'Medical'),
    ('Commerce', 'Commerce'),
    ('Humanities', 'Humanities'),
}

class Book(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=500, default='')
    price = models.IntegerField(default=0)
    author = models.CharField(max_length=200, default='')
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="media/profile_pics")
    stream = models.CharField(default='Engineering', choices=STREAM_CHOICES, max_length=15)
    college = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title

class Note(models.Model):
    topic = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to="notes/pdfs/")

    def __str__(self):
        return self.title

class College(models.Model):
    name = models.CharField(max_length=100, default='')