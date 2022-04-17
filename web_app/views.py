from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import DetailView
from django.db.models import Q
from .models import Restaurant, Dish, User, Review
from .forms import SignUpForm, DishForm, ReviewForm, RestaurantForm


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
        context['review'] = Review.objects.all()
        return context


class AddDishView(CreateView):
    """
    veiw for add dish page
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
            'index.html',
        )


class AddRestaurantView(CreateView):
    """
    veiw for add review page
    """
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'add_restaurant.html'
    success_url = "/"

    def form_valid(self, form):
        Restaurant = form.save(commit=False)
        name = Restaurant.name.replace(" ", "-")
        Restaurant.slug = name
        Restaurant.added_by = self.request.user
        return super().form_valid(form)


class AddReviewView(CreateView):
    """
    veiw for add review page
    """
    model = Restaurant
    form_class = ReviewForm
    template_name = 'add_review.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['review'] = Review.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.save()
        else:
            review_form = reviewForm()

        return render(
            request,
            'index.html',
        )


class EditDishView(UpdateView):
    """
    veiw for editing dishes page
    """
    model = Dish
    form_class = DishForm
    template_name = 'edit_dish.html'
    success_url = "/"


class EditReviewView(UpdateView):
    """
    veiw for editing dishes page
    """
    model = Review
    form_class = ReviewForm
    template_name = 'edit_review.html'
    success_url = "/"


class DeleteDishView(DeleteView):
    """
    veiw for deleting dishes
    """
    model = Dish
    success_url = reverse_lazy('home')


class DeleteReviewView(DeleteView):
    """
    veiw for deleting dishes
    """
    model = Dish
    success_url = reverse_lazy('home')