import time

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from threading import Thread
from base_user.models import MyUser

from task_manager_app.tasks import send_mail

# User = get_user_model()
from tasks.models import Tasks

print("SIGNALLLL")


@receiver(post_save, sender=MyUser, dispatch_uid='start_task')
def start_task(*args, **kwargs):
    obj = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        background_job = Thread(target=send_mail, args=(obj.email,))
        print('ADDED User')
        background_job.start()



