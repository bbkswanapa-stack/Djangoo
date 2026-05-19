from django.urls import path
from home.views import home, home_json, welcome, student_list, student_create, student_create2

urlpatterns = [
    path('' , home, name="home"),
    path('json/', home_json, name="json-data"),
    path('homepage/', welcome, name='page'),
    path('student_list/', student_list, name='student'),
    path('student_create/', student_create,name="create"),
    path('student_create2/', student_create2,name="create2"),
]