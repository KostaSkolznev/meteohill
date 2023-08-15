import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from main.weatherdata import weather_info, openweather_info
from main.clock import oclock
from userpage.models import Profile

def index(request):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/295863?apikey=ICseysmELVRIU8R8EF1lle8lR88uJgX6'
    res = requests.get(url).json()

    context = {
        'info': weather_info,
        'clock': oclock,
        'openweather_info': openweather_info,
        'selected_city': Profile.objects.get(UserID = request.user).SelectedCity,
        'user_id': request.user,
    }

    return render(request, 'main/index.html', context)

def accuweather(request):

    context = {
        'info': weather_info
    }

    return render(request, 'main/accuweather.html', context)

def openweather(request):

    context = {
        'openweather_info': openweather_info
    }

    return render(request, 'main/openweather.html', context)

def about(request):
    return render(request, 'main/about.html')