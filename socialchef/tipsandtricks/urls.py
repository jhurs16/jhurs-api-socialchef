from django.urls import path
from .views import ListTipsandTricks

urlpatterns = [
    path('', ListTipsandTricks.as_view(), name="tipsandtricks"),
    # path('latest-articles/', ListLatestArticles.as_view(), name="latest-articles"),
]