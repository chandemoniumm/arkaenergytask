from django.urls import path
from .views import student_list, adult_students

urlpatterns = [
    path('api/students/', student_list, name='student-list'),
    path('api/students/adults', adult_students, name='adult-student-list'),
]

