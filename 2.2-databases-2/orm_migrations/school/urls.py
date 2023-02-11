from django.urls import path

from school.views import students_view

urlpatterns = [
    path('', students_view, name='students'),
]
