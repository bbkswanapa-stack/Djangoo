
from django.urls import path
from info.views import info_home


urlpatterns = [
    path('', info_home),
]