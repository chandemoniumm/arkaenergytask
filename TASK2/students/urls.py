from django.urls import path
from .views import student_list, adult_students

urlpatterns = [
    path('', student_list, name='student-list'),
    path('adults', adult_students, name='adult-student-list'),
]

