import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Weather, WeatherService
import datetime

url = 'http://dataservice.accuweather.com/currentconditions/v1/295863?apikey=ICseysmELVRIU8R8EF1lle8lR88uJgX6&details=true'
res = requests.get(url).json()
now = datetime.date.today()

checkdate = Weather.objects.filter(date__date=now, service=1)

if checkdate.exists():
    a = True
else: a = False

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