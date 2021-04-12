from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import PlaceForm
from django.contrib import messages

from .models import Place


def index(request):
    return render(request, 'index.html')


def sortcity(request):
    distinct_cities = Place.objects.distinct('city')
    return render(request, 'place/sortcity.html', context={'distinct_cities': distinct_cities})


def all_place_in_city(request, cityname):
    list_of_place = Place.objects.filter(city=cityname)
    return render(request, 'place/sorted_by_city.html', context={'list_of_place': list_of_place})


def add_place(request):
    form = PlaceForm()
    return render(request, 'place/add_places.html', {"form": form})


class PlaceDetailView(generic.DetailView):
    model = Place
    template_name = 'place/place.html'
    context_object_name = 'place'
    paginate_by = 2
    queryset = Place.objects.filter(location__isnull=False)


class PlaceListView(generic.ListView):
    model = Place
    template_name = 'place/places.html'
    context_object_name = 'places'
    paginate_by = 2
    queryset = Place.objects.filter(location__isnull=False)
