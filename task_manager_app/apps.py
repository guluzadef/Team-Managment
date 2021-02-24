from django.apps import AppConfig


class TaskManagerAppConfig(AppConfig):
    name = 'task_manager_app'

    def ready(self):
        import task_manager_app.signals