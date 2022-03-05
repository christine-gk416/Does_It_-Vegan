from django.shortcuts import render
from django.viewa import generic
from .models import Restaurant

class RestaurantList(generic.ListView):
    """
    creates generic list view for restaurants
    """
    model = Restaurant
    queryset = Restaurant.objects.filter(status=1).order_by('-updated_on')
    template_name = 'index.html'
    paginate_by = 6
