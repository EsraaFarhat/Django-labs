from django.shortcuts import render
from django.http import HttpResponse
from lab1.models import Student, Track
# Create your views here.

def home(request):
    return HttpResponse("<h1>This is a Home Page</h1>")

def getStudent(request, st_id):
    st = Student.objects.get(id = st_id)
    context = {'student': st}
    return render(request, 'lab1/student_details.html', context)

def getAllStudents(request):
    all_students = Student.objects.all()
    context = {'students': all_students}
    return render(request, 'lab1/students.html', context)