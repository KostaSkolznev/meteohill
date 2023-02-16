import requests
from django.shortcuts import render
from .models import Weather, City, WeatherService, WeatherStatus
import datetime

# class for weather data
class WeatherData:
    def __init__(self, url, service_select):
         self.url = url
         self.service_select = service_select

    # check if exist in DB
    def checkdate(self):
        now = datetime.date.today()
        checkdate = Weather.objects.filter(date__date=now, service = self.service_select)
        return checkdate.exists()

    # get data from database
    def get_data(self):
        now = datetime.date.today()
        get_weather = Weather.objects.filter(date__date=now, service = self.service_select)
        for el in get_weather:
            weather_info = {
            'temp': el.temperature_day,
            'tempnight': el.temperature_night,
            'humidity': el.humidity,
            'precipitation': el.precipitation_type.precipitation,
            'clouds': el.precipitation_type.cloud_cover,
            'wind': el.wind,
            'windgust': el.wind_gusts,
        }
        
        return weather_info

    def select_weather_status(self, select_precipitation, clouds):
        if select_precipitation == "None" and clouds == "Cloudy":
            return 1
        elif select_precipitation == "Rain" and clouds == "Cloudy":
            return 2
        elif select_precipitation == "Rain" and clouds == "Sun":
            return 3
        elif select_precipitation == "Snow" and clouds == "Cloudy":
            return 4
        elif select_precipitation == "Snow" and clouds == "Sun":
            return 5
        elif select_precipitation == "Thunderstorm" and clouds == "Cloudy":
            return 6
        else: return 7

    # add data to database
    def add_weather(self,
                    city,
                    service,
                    humidity,
                    wind,
                    wind_gusts,
                    temperature_day,
                    temperature_night,
                    precipitation_type,
                    ):
        add_this_weather = Weather(
            city = City.objects.get(id = 1),
            service = WeatherService.objects.get(id = 1),
            humidity = weather_info['humidity'],
            wind = weather_info['wind'],
            wind_gusts = weather_info['windgust'],
            temperature_day = weather_info['temp'],
            temperature_night = weather_info['tempnight'],
            precipitation_type = WeatherStatus.objects.get(id = precipitation_type),
        )

        add_this_weather.save()

# create object accuweather
accuweather = WeatherData('http://dataservice.accuweather.com/currentconditions/v1/295863?apikey=ICseysmELVRIU8R8EF1lle8lR88uJgX6&details=true', 1)
res = requests.get(accuweather.url).json()
# if accuweather data exist, then read it

if accuweather.checkdate() is True:
    weather_info = accuweather.get_data()

# if not exist then get api and add to DB
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

    weather_status = accuweather.select_weather_status(
        weather_info['precipitation'],
        weather_info['clouds']
    )

    accuweather.add_weather(
        City.objects.get(id = 1),
        WeatherService.objects.get(id = 1),
        weather_info['humidity'],
        weather_info['wind'],
        weather_info['windgust'],
        weather_info['temp'],
        weather_info['tempnight'],
        weather_status,
    )