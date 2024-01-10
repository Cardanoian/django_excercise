from django.urls import path
from . import views

# register the app namespace
# URL NAMES
app_name = "my_app"

urlpatterns = [
    path("", views.example_view, name="example"),  # / my_apps --> PROJECT urls.py
    path("variable/", views.variable_view, name="variable"),
]
