from django.urls import path
# from task_manager_app.views import index
from .views import *

urlpatterns = [
    # path()
    path('add/', UserAddTeamApi.as_view()),
    path('team/', TeamForIdApi.as_view()),

]
