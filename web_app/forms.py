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
        fields = (
            'name', 'description', 'price', 'image', 'type', 'restaurant',
        )


class ReviewForm(forms.ModelForm):
    """
    creates a form to add a new dish for a restaurant
    """
    class Meta:
        model = Review
        fields = (
            'title', 'body', 'posted_by', 'restaurant',
        )


class RestaurantForm(forms.ModelForm):
    """
    creates a form to add a new restaurant 
    """
    class Meta:
        model = Restaurant
        fields = (
            'name', 'description', 'adress', 'townCity', 'image',
        )