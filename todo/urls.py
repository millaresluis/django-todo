from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from todo import views as todo_views

router = routers.DefaultRouter()
router.register('todos', todo_views.TodoView, 'todo')

urlpatterns = [
    path('', include(router.urls))
]
