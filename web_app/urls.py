from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('add_dish/<int:pk>', views.AddDishView.as_view(), name='add_dish'),
    path(
        'add_restaurant/', views.AddRestaurantView.as_view(),
        name='add_restaurant'
    ),
    path(
        'edit_dish/<int:pk>', views.EditDishView.as_view(), name='edit_dish'
    ),
    path(
        'delete/<int:pk>', views.DeleteDishView.as_view(),
        name='dish_confirm_delete'
    ),
    path(
        'delete/<int:pk>', views.DeleteReviewView.as_view(),
        name='review_confirm_delete'
    ),
    path(
        'add_review/<int:pk>', views.AddReviewView.as_view(), name='add_review'
    ),
    path(
        'edit_review/<int:pk>', views.EditReviewView.as_view(),
        name='edit_review'
    ),
    path(
        'restaurant_detail/<int:pk>',
        views.RestaurantDetailView.as_view(),
        name='restaurant_detail'
    ),
    path(
        'site_admin/',
        views.SiteAdminView.as_view(),
        name='site_admin'
    ),
    path(
        'manage_reviews/',
        views.ManageReviewsView.as_view(),
        name='manage_reviews'
    ),
    path(
        'approve_review/<int:pk>',
        views.ApproveReviewView.as_view(),
        name='approve_review'
    ),
    path('', include('django.contrib.auth.urls')),
]
