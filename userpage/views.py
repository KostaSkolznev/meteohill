from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from .models import City
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def index(request):

    context = {
        'cities': City.objects.all(),
        'selected_city': Profile.objects.get(UserID=request.user)
        }
        
    if request.user.is_authenticated:
        return render(request, 'userpage/index.html', context)
    else:
        return render(request, 'registration/login.html')

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/')
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)