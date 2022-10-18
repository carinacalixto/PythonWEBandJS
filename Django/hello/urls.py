from unicodedata import name
from django.urls import path
from . import views

app_name = "hello"

urlpatterns = [
    path("", views.index, name="index"),
    path("carina", views.carina, name="carina"),
    path("david", views.david, name="david"),
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greet, name="greet")
]
