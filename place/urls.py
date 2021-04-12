from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place/', views.PlaceListView.as_view(), name='place'),
    path('place/<int:pk>/', views.PlaceDetailView.as_view(), name="place"),
    path('sortcity', views.sortcity, name="sort_by_city"),
    path('create/', views.PlaceCreate.as_view(), name="new-place"),
]
