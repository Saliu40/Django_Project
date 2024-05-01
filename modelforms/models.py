from django.db import models

# Create your models here.


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)
    class Meta:
        # Specify custom table name
        db_table = 'modelform'
