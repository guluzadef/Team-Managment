from rest_framework import permissions


class IsTaskManager(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_task_manager == True:
            return True
        else:
            return False


# class MyTeam(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
