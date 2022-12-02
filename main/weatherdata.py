import requests
from django.shortcuts import render
from .models import Weather, City, WeatherService, WeatherStatus
import datetime

url = 'http://dataservice.accuweather.com/currentconditions/v1/295863?apikey=ICseysmELVRIU8R8EF1lle8lR88uJgX6&details=true'
res = requests.get(url).json()
now = datetime.date.today()

checkdate = Weather.objects.filter(date__date=now, service=1)

if checkdate.exists():
    a = True
    weather_info = {
        'temp': checkdate.temperature_day,
        'tempnight': checkdate.temperature_night,
        'humidity': checkdate.humidity,
        'precipitation': checkdate.precipitation_type,
        'clouds': checkdate.precipitation_type,
        'wind': checkdate.wind,
        'windgust': checkdate.windgusts,
        'datenow': a,
    }

else:
    a = False
    weather_info = {
        'temp': round(res[0]["Temperature"]["Metric"]["Value"]),
        'tempnight': round(res[0]["TemperatureSummary"]["Past24HourRange"]["Minimum"]["Metric"]["Value"]),
        'humidity': res[0]["RelativeHumidity"],
        'precipitation': res[0]["PrecipitationType"],
        'clouds': res[0]["WeatherText"],
        'wind': res[0]["Wind"]["Speed"]["Metric"]["Value"],
        'windgust': res[0]["WindGust"]["Speed"]["Metric"]["Value"],
        'datenow': a,
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