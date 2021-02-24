from django.contrib.auth import get_user_model
from rest_framework import serializers

# from base_user.models import User
# from tasks.serializer import TaskSerializer
from .models import Team

User = get_user_model()


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'id', 'name', 'address', 'phone_number')


class UsersSerializer(serializers.ModelSerializer):
    # team = TeamListSerializer()

    class Meta:
        model = User
        fields = ('id', "username", 'last_name', 'email', 'password', 'team'
                  )
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'required': True, 'allow_blank': False, 'min_length': 6},
            # 'tasks': {'required': False},
            # 'team': {'required': False},

        }
