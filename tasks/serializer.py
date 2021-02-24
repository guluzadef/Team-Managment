from django.contrib.auth import get_user_model
from rest_framework import serializers
from teams.models import Team
from teams.serializer import TeamListSerializer
from .models import Tasks

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    team = TeamListSerializer(read_only=True)

    class Meta:
        model = Tasks
        fields = ('id', 'team', 'users', 'title', 'description', 'deadline', 'status'
                  )
        read_only_fields = ('id',)
        extra_kwargs = {
            'users': {'required': True},

        }

    def create(self, validated_data):
        users = validated_data.get('users')
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        team = Team.objects.filter(id=user.team.id).last()

        validated_data.pop('users')
        task = Tasks.objects.create(**validated_data)
        task.team = team
        task.users.add(*users)
        return task


class TaskSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'team', 'users', 'title', 'description', 'deadline', 'status'
                  )
        read_only_fields = ('id',)
