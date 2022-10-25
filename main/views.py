import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

def index(request):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/295863?apikey=ICseysmELVRIU8R8EF1lle8lR88uJgX6'
    res = requests.get(url).json()

    weather_info = {
        'temp': round(res[0]["Temperature"]["Metric"]["Value"]),
        'precipitation': res[0]["PrecipitationType"],
        'clouds': res[0]["WeatherText"]
    }

    context = {
        'info': weather_info
    }

    return render(request, 'main/index.html', context)

def accuweather(request):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/295863?apikey=ICseysmELVRIU8R8EF1lle8lR88uJgX6&details=true'
    res = requests.get(url).json()

    weather_info = {
        'temp': round(res[0]["Temperature"]["Metric"]["Value"]),
        'tempnight': round(res[0]["TemperatureSummary"]["Past24HourRange"]["Minimum"]["Metric"]["Value"]),
        'humidity': res[0]["RelativeHumidity"],
        'precipitation': res[0]["PrecipitationType"],
        'clouds': res[0]["WeatherText"],
        'wind': res[0]["Wind"]["Speed"]["Metric"]["Value"],
        'windgust': res[0]["WindGust"]["Speed"]["Metric"]["Value"],
    }

    context = {
        'info': weather_info
    }

    return render(request, 'main/accuweather.html', context)