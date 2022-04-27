from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Review, Dish, Restaurant


class SignUpForm(UserCreationForm):
    """
    creates a form to update djangos User model
    """
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class DishForm(forms.ModelForm):
    """
    creates a form to add a new dish for a restaurant
    """
    class Meta:
        model = Dish
        exclude = ('restaurant', 'posted_by',)


class EditDishForm(forms.ModelForm):
    """
    creates a form to add a new dish for a restaurant
    """
    class Meta:
        model = Dish
        exclude = ('restaurant',)


class ReviewForm(forms.ModelForm):
    """
    creates a form to add a new review for a restaurant
    """
    class Meta:
        model = Review
        exclude = ('restaurant', 'approved',)


class RestaurantForm(forms.ModelForm):
    """
    creates a form to add a new restaurant 
    """
    class Meta:
        model = Restaurant
        fields = (
            'name', 'description', 'adress', 'townCity', 'image',
        )


class ManageReviewsForm(forms.ModelForm):
    """
    creates a form to add a manage reviews
    """
    class Meta:
        model = Review
        fields = (
            'approved',
        )