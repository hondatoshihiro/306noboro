from django.db import models
from setuptools import SetuptoolsDeprecationWarning

# Create your models here.

class Noboro(models.Model):
    volno = models.IntegerField()
    year = models.IntegerField()
    season = models.CharField(max_length=8)

    def __str__(self):
        return '<Noboro:id=' + str(self.id) + ', ' + str(self.volno) + '>'
