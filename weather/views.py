import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
	if(request.method == "POST"):
		form = CityForm(request.POST)
		form.save()


	appid = '9c9b27f15bae471953a6675f78e97b9e'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
	form = CityForm()

	cities = City.objects.all()

	allcities = []

	for city in cities:

		res = requests.get(url.format(city.name)).json()

		cityinfo = {
			'city': city.name,
			'temperature': res["main"]["temp"],
			'icon': res['weather'][0]['icon']
		}

		allcities.append(cityinfo)

		if len(allcities) > 7:
			allcities.remove(allcities[0])


	context = {'all_info':allcities, 'form':form}

	return render(request, 'index.html', context)