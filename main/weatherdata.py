import requests
from django.shortcuts import render
from .models import Weather, City, WeatherService, WeatherStatus
import datetime

url = 'http://dataservice.accuweather.com/currentconditions/v1/295863?apikey=ICseysmELVRIU8R8EF1lle8lR88uJgX6&details=true'
res = requests.get(url).json()
now = datetime.date.today()

checkdate = Weather.objects.filter(date__date=now, service=1)

if checkdate.exists():
    for el in checkdate:
        weather_info = {
            'temp': el.temperature_day,
            'tempnight': el.temperature_night,
            'humidity': el.humidity,
            'precipitation': el.precipitation_type,
            'clouds': el.precipitation_type,
            'wind': el.wind,
            'windgust': el.wind_gusts,
        }

else:
    weather_info = {
        'temp': round(res[0]["Temperature"]["Metric"]["Value"]),
        'tempnight': round(res[0]["TemperatureSummary"]["Past24HourRange"]["Minimum"]["Metric"]["Value"]),
        'humidity': res[0]["RelativeHumidity"],
        'precipitation': res[0]["PrecipitationType"],
        'clouds': res[0]["WeatherText"],
        'wind': res[0]["Wind"]["Speed"]["Metric"]["Value"],
        'windgust': res[0]["WindGust"]["Speed"]["Metric"]["Value"],
    }

    add_weather = Weather(
        city = City.objects.get(id = 1),
        service = WeatherService.objects.get(id = 1),
        humidity = weather_info['humidity'],
        wind = weather_info['wind'],
        wind_gusts = weather_info['windgust'],
        temperature_day = weather_info['temp'],
        temperature_night = weather_info['tempnight'],
        precipitation_type = WeatherStatus.objects.get(id = 1),
    )

    add_weather.save()