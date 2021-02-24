from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from .serializer import *
from base_user.serializer import UserSerializer

User = get_user_model()


# Create your views here.


class TeamForIdApi(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        # team_id = request.user.team_id
        user = User.objects.filter(team_id=request.user.team_id)
        serializer = UsersSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserAddTeamApi(CreateAPIView):
    permission_classes = (permissions.AllowAny,)  # deyishh!!!
    serializer_class = UsersSerializer

    def get(self, request):
        return Response(status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            password = serializer.data.pop('password')
            team = Team.objects.filter(id=request.user.team.id).last()
            user = User(**serializer.data)
            try:
                user.set_password(password)
                user.team = team
                user.save()
                response = self.get_serializer(instance=user)
                return Response(response.data, status=status.HTTP_201_CREATED)
            except:
                return Response({
                    "message": "This User Already Exists "
                }, status=status.HTTP_409_CONFLICT)
        else:
            return Response({
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = self.get_serializer(request.user)
            return Response(serializer.data, status=200)
        return Response(status=401)
