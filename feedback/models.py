from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

class Topic(models.Model):
    name = models.CharField(max_length=160)
    def __str__(self):
        return self.name

class Arvosana(models.IntegerChoices):
        välttävä_1 = 1
        tyydyttävä_2 = 2
        hyvä_3 = 3
        kiitettävä_4 = 4
        erinomainen_5 = 5

class Feedback(models.Model):
    aihe = models.ForeignKey(Topic, on_delete=models.CASCADE)
    arvosana = models.IntegerField(choices=Arvosana.choices, default=5)
    ruusut = models.TextField(max_length=2000, blank=True)
    risut = models.TextField(max_length=2000, blank=True)
    ideat = models.TextField(max_length=2000, blank=True)
    nimi = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.date}"
