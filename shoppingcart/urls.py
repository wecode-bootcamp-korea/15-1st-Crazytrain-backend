from django.urls import path,include
from .views import Cart

urlpatterns = [
    path('/cart', Cart.as_view()),   
]
