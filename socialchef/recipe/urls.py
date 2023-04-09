from django.urls import path
from recipe.views import ListRecipes, ListLatestRecipes, FeaturedRecipe

urlpatterns = [
    path('', ListRecipes.as_view(), name="recipes"),
    path('latest-recipes/', ListLatestRecipes.as_view(), name="latest-recipes"),
    path('featured-recipe/', FeaturedRecipe.as_view(), name="featuredrecipe"),
]