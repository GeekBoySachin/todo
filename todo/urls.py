from django.urls import path
from . import views

urlpatterns = [
    #To Do
    path('addTask/',views.addTask,name='addTask')
]