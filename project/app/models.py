from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    date = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.name
