from django.urls import path, include
from .views import home_view, signup_view, login_view, logout_view

# api
from .views import HealthCheckApi

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("home/", home_view, name="home"),
    # API
    path("api/v1/health/", HealthCheckApi.as_view()),
    path("api/", include("core.api.urls")),
]
