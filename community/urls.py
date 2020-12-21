from django.urls import path
from community.views import Posting


urlpatterns = [
    path('/posting', Posting.as_view()),
]