from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

# Create your views here.
def home(request):
    print("Hello from Django!!")
    return HttpResponse ("<i> Hello from Django!! <i>")



def home_json(request):
    data = {
        'name' : 'Kmc',
        'address' : 'Kathmandu'
    }
    return JsonResponse(data)

def welcome(request):
    user_info = {
        'name' : 'Bibek Swanapa'
    }
    return render(request, "demo/index.html", user_info)