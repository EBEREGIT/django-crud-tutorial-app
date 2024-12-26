from django.urls import path
from .views import home, students, student, student_delete, register, profile

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("accounts/profile/", profile, name="profile"),
    path("students/", students, name="students"),
    path("students/<int:pk>", student, name="student"),
    path("students/<int:pk>/delete", student_delete, name="student_delete"),
]
