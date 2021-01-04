from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    number = models.IntegerField()

    def __str__(self):
        return self.first_name
