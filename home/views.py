from django.shortcuts import render
from home.brain import get_weather_by_address

def index(request):
    return render(request, 'index.html')

def show(request):
    weather_data = ""
    if request.method == "POST":
        city = request.POST.get('city')
        weather_data = get_weather_by_address(city)  # Call your function to get weather data
    
    return render(request, 'show.html', {'weather_data': weather_data})

def get_weather(request):
    weather_data = ""
    if request.method == "POST":
        city = request.POST.get('city')
        weather_data = get_weather_by_address(city)  # Call your function to get weather data
    
    return render(request, 'show.html', {'weather_data': weather_data})