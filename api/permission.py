from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        if request.method == 'POST':
            return request.user.is_authenticated
        

class UserDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_authenticated





class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return request.user.is_staff      


class CategoryDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_staff





class PostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return True
        
class PostDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:
            return True
            
                