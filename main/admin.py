from django.contrib import admin
from .models import City
from .models import WeatherStatus
from .models import WeatherService
from .models import Weather

admin.site.register(City)
admin.site.register(WeatherStatus)
admin.site.register(WeatherService)
admin.site.register(Weather)
