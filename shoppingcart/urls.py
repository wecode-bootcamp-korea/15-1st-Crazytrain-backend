from django.urls import path,include
from .views import CartView

urlpatterns = [
    path('/cart', CartView.as_view()),   
]
