from django.urls import path
from .views      import CategoryView

urlpatterns = [
    path('/store', CategoryView.as_view()),
]
