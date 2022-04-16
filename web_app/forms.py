from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Review, Dish


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
