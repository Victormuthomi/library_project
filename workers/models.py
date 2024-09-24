from django.db import models

# Create your models here.
class Worker(models.Model):
    """The model for the workers"""
    name = models.CharField(max_length=25)
    id_number = models.IntegerField()
    member_number = models.IntegerField()

    def __str__(self):
        return self.name
