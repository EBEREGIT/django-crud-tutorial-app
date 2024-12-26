from django.shortcuts import render, HttpResponse, redirect
from .models import Student
from .form import StudentForm, RegisterForm


# Create your views here.
def home(request):
    return render(request, "home.html")

def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "accounts/profile.html")


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("<h1>Registration Successful</h1>")
    return render(request, "registration/register.html", {"form": form})


# view all
def students(request):
    try:
        form = StudentForm(request.POST)

        if request.method == "GET":
            students = request.user.students.all()
            return render(
                request, "students.html", {"students": students, "form": form}
            )

        # django form
        if request.method == "POST":
            if form.is_valid():
                form.save()
                request.user.students.add(form.instance)
                return HttpResponse("<h1>Upload Successful</h1>")

        # regular form
        # if request.method == "POST":
        #     student = Student()
        #     student.owner = request.POST.get(request.user)
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
            if request.user.username == student.owner.username:
                return render(request, "student.html", {"student": student, "form": form})
            else:
                return HttpResponse("<h1>Unauthorized</h1>")

        # django
        if request.method == "POST":
            if request.user.username == student.owner.username:
                if form.is_valid():
                    form.save()
                    return HttpResponse("<h1>Upload Successful</h1>")
            else:
                return HttpResponse("<h1>Unauthorized</h1>")

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
        
        if request.user.username == student.owner.username:
            student.delete()
            return HttpResponse("<h1>Student Deleted Successfully</h1>")
        else:
            return HttpResponse("<h1>Unauthorized</h1>")
    except:
        return HttpResponse("<h1>Delete Failed</h1>")
