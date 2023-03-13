from django.urls import path
from djoser.views import TokenCreateView, TokenDestroyView

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", TokenCreateView.as_view(), name="login"),
    path("logout/", TokenDestroyView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
]
