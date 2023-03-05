from django.db import models


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=21)
    surname = models.CharField(max_length=21)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()
