from django.urls import path
from .views import home,about


urlpatterns = [
    path("",home),
    path("property-details",about,name="property-details")
]
