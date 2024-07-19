from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.apiOverview, name="Routes"),
    path('reviews/', views.getReviews, name="Reviews"),
    path('recipes/', views.getRecipes, name="Recipes")
]