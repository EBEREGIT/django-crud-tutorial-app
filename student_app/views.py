from django.shortcuts import render, HttpResponse
from .models import Student


# Create your views here.
def home(request):
    return render(request, "home.html")


# view all
def students(request):
    if request.method == "GET":
        students = Student.objects.all()

    if request.method == "POST":
        student = Student()
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.about = request.POST.get("about")
        student.pub_date = request.POST.get("pub_date")

        student.save()
        return HttpResponse("<h1>Upload Successful</h1>")

    return render(request, "students.html", {"students": students})


def student(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == "GET":
        return render(request, "student.html", {"student": student})

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.about = request.POST.get("about")
        student.pub_date = request.POST.get("pub_date")

        student.save()
        return HttpResponse("<h1>Student Update Successful</h1>")


def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return HttpResponse("<h1>Student Deleted Successfully</h1>")
