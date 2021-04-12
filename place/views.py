from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Place


def index(request):
    return render(request, 'index.html')


def sortcity(request):
    distinct_city = Place.objects.distinct('city')
    return render(request, 'place/sortcity.html', context={'distinct_city' : distinct_city})


def sorted_by_city(request, cityname):
    cities = Place.objects.filter(city=cityname)
    return render(request, 'place/sorted_by_city.html', context={'cities': cities})


class PlaceDetailView(generic.DetailView):
    model = Place
    template_name = 'place/place.html'
    context_object_name = 'place'
    paginate_by = 5
    queryset = Place.objects.filter(location__isnull=False)


class PlaceListView(generic.ListView):
    model = Place
    template_name = 'place/places.html'
    context_object_name = 'places'
    paginate_by = 5
    queryset = Place.objects.filter(location__isnull=False)


class PlaceCreate(generic.CreateView):
    model = Place
    fields = ['title', 'location', 'description', 'address', 'city', 'type']
    template_name = 'place/add_places.html'
