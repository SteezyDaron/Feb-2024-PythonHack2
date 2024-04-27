import requests
from django.shortcuts import render

def weather_view(request):
    api_key = 'YOUR_API_KEY'
    city = 'London'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    context = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }
    return render(request, 'weather.html', context)
