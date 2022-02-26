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
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="restaurant_added")
    updated_on = models.DateField(auto_now=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='restaurant_likes', blank=True)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        """
        will order class based on crrated on date.
        inspired by code institue blog walk through project
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        django docs recamends to define this method
        """
        return self.name

    def number_of_likes(self):
        """
        tracks number of likes to be displayed.
        taken from code insttute blog site walkthrough project
        """
        return self.likes.count()


class Review(models.Model):
    """
    model for restaurant reviews
    """
    title = models.CharField(max_length=200, unique=True)
    restaurant = models.ForeignKey(
        Restaurants, on_delete=models.CASCADE, related_name='reviews')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        """
        will order class based on crrated on date.
        inspired by code institue blog walk through project
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        django docs recamends to define this method
        """
        return f"Comment {self.body} by {self.title}"
