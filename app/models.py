from django.db import models

# Create your models here.
from django.core import validators
class School(models.Model):
    Sname=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(5)])
    Sid=models.IntegerField(primary_key=True,validators=[validators.MaxValueValidator(999)])
    Saddress=models.TextField()
    def __str__(self):
        return str(self.Sid)