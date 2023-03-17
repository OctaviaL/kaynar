from rest_framework.permissions import BasePermission

class  IsAdminUser(BasePermission):
    """Проверка , являеться ли пользователь администратором"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff