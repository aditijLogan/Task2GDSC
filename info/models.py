from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.TextField()
    rollno = models.TextField()

    def __str__(self):
        return self.name