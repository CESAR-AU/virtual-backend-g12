from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

class SoloAdminPuedeEscribir(BasePermission):
    message = 'Este usuario no tiene permisos'
    def has_permission(self, request:Request, view):
        print(request.user)
        print(request.user.nombre)
        print(request.user.rol)
        print(request.auth)
        print(request.method)
        print(SAFE_METHODS)
        # if(request.user.rol) == 'ADMINISTRADOR': return True
        # else: return False
        # if(request.method in SAFE_METHODS): return True
        # else: return request.user.rol == 'ADMINISTRADOR' 
        # return request.method in SAFE_METHODS and  request.user.rol == 'ADMINISTRADOR'

        return True if (request.method in SAFE_METHODS) else request.user.rol == 'ADMINISTRADOR'

class SoloMozoPuedeEscribir(BasePermission):
    message = 'Solo un MOZO puede agregar pedidos'
    def has_permission(self, request:Request, view):
        return True if (request.method in SAFE_METHODS) else request.user.rol == 'MOZO'