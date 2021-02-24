from django.db import models
from base_user.models import MyUser
from teams.models import Team


# Create your models here.
class Tasks(models.Model):
    users = models.ManyToManyField(MyUser,related_name='users')
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
