from django.db import models
from .forms import MyForm
# Create your models here.
class MyModel(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = "register"