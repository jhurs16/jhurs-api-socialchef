from django.urls import path
from article.views import ListArticles, ListLatestArticles

urlpatterns = [
    path('', ListArticles.as_view(), name="articles"),
    path('latest-articles/', ListLatestArticles.as_view(), name="latest-articles"),
]