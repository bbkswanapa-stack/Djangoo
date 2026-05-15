from django.urls import path
from home.views import home, home_json, welcome

urlpatterns = [
    path('home/' , home, name="home"),
    path('json/', home_json, name="json-data"),
    path('homepage/', welcome, name='page')
]