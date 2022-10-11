from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=150)

    def __str__(self):
        return self.city_name

class WeatherStatus(models.Model):
    precipitation = models.CharField(max_length=25)
    cloud_cover = models.CharField(max_length=25)
    cloud_img = models.CharField(max_length=25)

class WeatherService(models.Model):
    service_name = models.CharField(max_length=25)
    service_url = models.CharField(max_length=250)
    api_url = models.CharField(max_length=250)

    def __str__(self):
        return self.service_name