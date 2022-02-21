from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Authorised"))

class Restaurants(models.Model):
    """
    model for restaurant data
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="restaurant_added")
    updated_on = models.DateField(auto_now=True)