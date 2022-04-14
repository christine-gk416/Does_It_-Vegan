from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import DetailView
from django.db.models import Q
from .models import Restaurant, Dish, User
from .forms import SignUpForm, DishForm


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
    """
    create view for search results page
    """
    model = Restaurant
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        restaurant_list = Restaurant.objects.filter(
            Q(townCity__iexact=query)
        )
        return restaurant_list


class SignUpView(CreateView):
    """
    veiw for user sing up page
    """
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'


class RestaurantDetailView(DetailView):
    """
    creates  view for restaurant details page
    """

    model = Restaurant
    template_name = 'restaurant_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['dish'] = Dish.objects.all()
        return context


class AddDishView(CreateView):
    """
    veiw for user sing up page
    """
    model = Restaurant
    form_class = DishForm
    template_name = 'add_dish.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['dish'] = Dish.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        dish_form = DishForm(data=request.POST)

        if dish_form.is_valid():
            dish = dish_form.save(commit=False)
            dish.save()
        else:
            dish_form = DishForm()

        return render(
            request,
            f"restaurant_detail/{restaurant.pk}",
        )
