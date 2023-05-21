from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpRequest
from django.shortcuts import render
from django.utils import timezone
from python_weather import Client, Locale


async def index(request: HttpRequest):
    g = GeoIP2(path="GeoLite2-City.mmdb")
    ip = '31.41.57.141'
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Moscow'
    weather_client = Client()
    weather = await weather_client.get(city)
    today = timezone.now().strftime("%A %d %B")
    data = {
        "locate": city,
        "today": today,
        "temperature": weather.current.temperature,
        "weather": weather.current.kind.name
    }
    await weather_client.close()
    return render(request, 'weatherapp/index.html', data)


async def detail(request: HttpRequest, city: str):
    weather_client = Client()
    weather = await weather_client.get(city, locale=Locale.RUSSIAN)
    today = timezone.now().strftime("%A %d %B")
    data = {
        "locate": city,
        "today": today,
        "temperature": weather.current.temperature,
        "weather": weather.current.kind.name
    }
    await weather_client.close()
    return render(request, 'weatherapp/index.html', data)
