from django.urls import path
# from task_manager_app.views import index
from rest_framework.routers import DefaultRouter

from .views import *
from rest_framework import routers
urlpatterns = [
    path('tasks/', TaskCreateApi.as_view()),
    path('tasklist/<int:id>/', TaskListApi.as_view()),
    # router.register('tasks/', BookViewSet, basename='tasks')

]
