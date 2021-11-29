from . import views
from django.urls import path
from django.views.generic.base import RedirectView


urlpatterns = [
    path("", views.home, name="home"),
    path("favicon.ico", RedirectView.as_view(url="static/home/favicon.ico")),
]
