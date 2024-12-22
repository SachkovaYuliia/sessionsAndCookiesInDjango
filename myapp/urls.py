from django.urls import path
from .views import login, welcome, logout

urlpatterns = [
    path("", login, name="login"),
    path("welcome/", welcome, name="welcome"),
    path("logout/", logout, name="logout"),
]