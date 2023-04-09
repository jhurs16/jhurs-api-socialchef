from django.urls import path
from .views import ListUsers, FeaturedUser

urlpatterns = [
    path('', ListUsers.as_view(), name="users"),
    path('featured-member/', FeaturedUser.as_view(), name="featureuser"),
    # path('latest-recipes/', ListLatestRecipes.as_view(), name="latest-recipes"),
]