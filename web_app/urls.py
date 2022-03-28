from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='home'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("sign-up/", views.SearchResultsView.as_view(), name="sign_up"),
]
