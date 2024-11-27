from django.shortcuts import render, HttpResponse
from .models import Student
from .form import StudentForm


# Create your views here.
def home(request):
    return render(request, "home.html")


# view all
def students(request):
    try:
        form = StudentForm(request.POST)

        if request.method == "GET":
            students = Student.objects.all()
            return render(request, "students.html", {"students": students, "form": form})

        # django form
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return HttpResponse("<h1>Upload Successful</h1>")

        # regular form
        # if request.method == "POST":
        #     student = Student()
        #     student.name = request.POST.get("name")
        #     student.email = request.POST.get("email")
        #     student.about = request.POST.get("about")
        #     student.pub_date = request.POST.get("pub_date")

        #     student.save()
        #     return HttpResponse("<h1>Upload Successful</h1>")
        
    except:
        return HttpResponse("<h1>Upload Failed</h1>")
        


def student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        form = StudentForm(request.POST, instance=student)

        if request.method == "GET":
            return render(request, "student.html", {"student": student, "form": form})

        # django
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return HttpResponse("<h1>Upload Successful</h1>")


        # html
        # if request.method == "POST":
        #     student.name = request.POST.get("name")
        #     student.email = request.POST.get("email")
        #     student.about = request.POST.get("about")
        #     student.pub_date = request.POST.get("pub_date")

        #     student.save()
        #     return HttpResponse("<h1>Student Update Successful</h1>")
    except:
        return HttpResponse("<h1>Update Failed</h1>")


def student_delete(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return HttpResponse("<h1>Student Deleted Successfully</h1>")
    except:
        return HttpResponse("<h1>Delete Failed</h1>")