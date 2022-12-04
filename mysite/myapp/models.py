from django.db import models

# Create your models here.
class Person(models.Model):
    # Especificar los atributos de mi clase
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, default="")
    reference = models.CharField(max_length=200, default="")
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + self.address