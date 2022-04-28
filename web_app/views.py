from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import DetailView, ListView
from django.db.models import Q
from .models import Restaurant, Dish, User, Review
from .forms import SignUpForm, DishForm, ReviewForm, RestaurantForm, ManageReviewsForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


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

    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully')
        return super().form_valid(form)


class RestaurantDetailView(DetailView):
    """
    creates  view for restaurant details page
    """

    model = Restaurant
    template_name = 'restaurant_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the models
        context['dish'] = Dish.objects.all()
        context['review'] = Review.objects.all()
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddDishView(SuccessMessageMixin, CreateView):
    """
    veiw for add dish page. can only be viewed if logged in
    """
    model = Dish
    form_class = DishForm
    template_name = 'add_dish.html'
    success_message = "Dish successfully added!"

    def form_valid(self, form):
        form.instance.restaurant = Restaurant.objects.get(pk=self.kwargs['pk'])
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        pk=self.kwargs['pk']
        return reverse("restaurant_detail", args=(self.kwargs['pk'],))


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddRestaurantView(SuccessMessageMixin, CreateView):
    """
    veiw for add review page
    """
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'add_restaurant.html'
    success_url = "/"
    success_message = "restaurant successfully added!"

    def form_valid(self, form):
        Restaurant = form.save(commit=False)
        name = Restaurant.name.replace(" ", "-")
        Restaurant.slug = name
        Restaurant.added_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddReviewView(SuccessMessageMixin, CreateView):
    """
    veiw for add review page
    """
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_message = "Review successfully added!"

    def form_valid(self, form):
        form.instance.restaurant = Restaurant.objects.get(pk=self.kwargs['pk'])
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        pk=self.kwargs['pk']
        return reverse("restaurant_detail", args=(self.kwargs['pk'],))


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EditDishView(SuccessMessageMixin, UpdateView):
    """
    veiw for editing dishes page
    """
    model = Dish
    form_class = DishForm
    template_name = 'edit_dish.html'
    success_message = "Dish successfully updated!"


    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        pk = self.kwargs['pk']
        dish = Dish.pk
        print(dish.restaurant)
        
        return reverse("restaurant_detail", args=(pk,))

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EditReviewView(UpdateView):
    """
    veiw for editing dishes page
    """
    model = Review
    form_class = ReviewForm
    template_name = 'edit_review.html'
    success_url = "home"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DeleteDishView(DeleteView):
    """
    veiw for deleting dishes
    """
    model = Dish
    success_url = reverse_lazy('home')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DeleteReviewView(DeleteView):
    """
    veiw for deleting dishes
    """
    model = Review
    success_url = reverse_lazy('home')


class SiteAdminView(generic.ListView):
    """
    veiw for user sing up page
    """

    model = Restaurant
    template_name = 'site_admin.html'


class ManageReviewsView(generic.ListView):
    """
    veiw for editing dishes page
    """
    model = Review
    template_name = 'manage_reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = Review.objects.all()
        return context


class ApproveReviewView(UpdateView):
    """
    veiw for approving reviews
    """
    model = Review
    form_class = ManageReviewsForm
    template_name = 'approve_review.html'
    success_url = "/"


class UserListView(ListView):
    """
    veiw for vieing list of users
    """
    model = User
    template_name = 'manage_users.html'


class DeleteUserView(DeleteView):
    """
    veiw for deleting dishes
    """
    model = User
    success_url = reverse_lazy('home')