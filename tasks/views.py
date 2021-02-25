from threading import Thread

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from task_manager_app.tasks import send_mail


from custom_permission.permission import IsTaskManager
from .serializer import *


class TaskCreateApi(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        task_data = super().create(request, *args, **kwargs).data
        task = Tasks.objects.get(pk=task_data['id'])
        data = {
            'id': task.id,
            'description': task_data['description'],
            'title': task_data['title'],

        }
        for e in task.users.all():
            background_job = Thread(target=send_mail, args=(e.email,))
            background_job.start()
        return Response(data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = self.get_serializer(request.user)
            return Response(serializer.data, status=200)
        return Response(status=401)


class TaskListApi(APIView):  # GET
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        teams = Tasks.objects.filter(id=id)
        serializer = TaskSerializerList(teams, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
