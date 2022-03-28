from django.shortcuts import render
from django.views import generic, View
from .models import Restaurant, Dish
from django.db.models import Q

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
        

class SearchResultsView(generic.ListView):
    model = Restaurant
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Restaurant.objects.filter(
            Q(townCity__icontains=query)
        )
        return object_list