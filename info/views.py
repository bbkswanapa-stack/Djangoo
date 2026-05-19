
from django.http import HttpResponse

# Create your views here.
def info_home(request):
    return HttpResponse("This is INFO app page")