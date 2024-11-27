from django.urls import path
from .views import home, students, student, student_delete

urlpatterns = [
    path("", home, name="home"),
    path("students/", students, name="students"),
    path("students/<int:pk>", student, name="student"),
    path("students/<int:pk>/delete", student_delete, name="student_delete"),
]
