from django.shortcuts import render, redirect

import requests

from .models import Cities

def clima_app(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=596b625b10896975a2e0bdd9724877d6'
    weather_data=[]
    cities_list = Cities.objects.all()

    if request.method =='POST':
        city = request.POST.get('city')
        if city:
            add_city = Cities.objects.create(city=city)
            add_city.save()
            return redirect('/')

    for city in cities_list:
        try:
            get_weather = requests.get(url.format(city)).json()
            
            weather = {
                'city': city,
                'temp': get_weather['main']['temp'],
                'desc': get_weather['weather'][0]['description'],
                'icon': get_weather['weather'][0]['icon'],
            }
            weather_data.append(weather)
        except KeyError as e:
            print(f"Error retrieving weather data for {city}: {e}")
            # Tratar o erro de chave ausente, talvez definindo valores padrão ou ignorando a cidade com erro
        except Exception as e:
            print(f"An unexpected error occurred for {city}: {e}")
            # Tratar outros erros de forma apropriada

    context = {'weather_data': weather_data}
    return render(request, "weather/weather_page.html", context)
