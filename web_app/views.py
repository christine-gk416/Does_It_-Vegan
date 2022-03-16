from django.shortcuts import render
from django.views import generic, View
from .models import Restaurant, Dish

class RestaurantList(generic.ListView):
    """
    creates generic list view for restaurants
    """
    model = Restaurant
    queryset = Restaurant.objects.filter(status=1).order_by('-updated_on')
    template_name = 'index.html'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['dish'] = Dish.objects.all()
        return context
