from django.db import models


class Food(models.Model):
    foodName = models.CharField(max_length=256)
    foodType = models.CharField(max_length=256)
    score = models.IntegerField()
