from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from home.models import Student
from home.forms import StudentForm

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

def student_list(request):
    student = Student.objects.all()
    context = {
        "student":student
    }
    return render(request, "student/index.html", context)

def student_create(request):
    if request.method == "POST":
        print(request.POST)
        data = request.POST
        Student.objects.create(
            name = data['student_name'],
            number = data['number'],
            DOB = data['DOB']
        )
        return redirect('/home/student_list')


    return render(request, 'student/create.html')

def student_create2(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/student_list')
        else:
            print(form.errors)
    context = {
        'form':form
    }
  
    return render(request, 'student/create2.html', context)