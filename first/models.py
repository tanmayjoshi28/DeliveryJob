from django.db import models
from django.urls import reverse


class Areawise(models.Model):
    name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    dilvry_pday = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '--' + self.pincode + '--' + self.dilvry_pday

    def get_absolute_url(self):
        return reverse('first:input_person', kwargs={'pk': self.pk})


class Person(models.Model):
    areawise = models.ForeignKey(Areawise, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=100, unique=True)
    vehicle = models.CharField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.p_name + '--' + str(self.areawise) + '--' + self.vehicle + '--' + self.phone_no
