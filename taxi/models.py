from django.db import models


class Taxi(models.Model):
    taxi_name = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    passenger_capacity = models.FloatField
    car_model = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

