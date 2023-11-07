from django.urls import path
from student_fees import views

urlpatterns = [
    path('student_fees', views.studentfees, name='student_fees'),
]