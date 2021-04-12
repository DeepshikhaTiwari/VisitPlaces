from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Place


def index(request):
    return render(request, 'index.html')


def sortcity(request):
    return render(request, 'sortcity.html')


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
    fields = ['title', 'location', 'description', 'address', 'phone', 'city', 'type']
    template_name = 'place/add_places.html'
