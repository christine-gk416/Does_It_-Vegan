from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='home'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("sign_up/", views.SignUpView.as_view(), name="sign_up"),
    path('', include('django.contrib.auth.urls')),
]
