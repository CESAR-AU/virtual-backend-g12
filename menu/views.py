from .models import Plato
from .serializers import PlatoSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import (AllowAny, #Controlador publica
IsAuthenticated, #Solisita una token
IsAuthenticatedOrReadOnly, #Solisita una token, solo GET no requiere
IsAdminUser, # Valida si es super usuario
)
from rest_framework.request import Request
from rest_framework.response import Response
from cloudinary import CloudinaryImage
from os import environ

# Create your views here.
class PlatoApiView(ListCreateAPIView):
    serializer_class = PlatoSerializer
    queryset = Plato.objects.all()
    # Permisos
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request:Request):
        data = self.serializer_class(instance=self.get_queryset(), many = True)
        for index in range(len(data.data)):
            print(data.data[index].get('foto'))
            # link = CloudinaryImage(data.data[index].get('foto')).image(secure=True)
            link = environ.get('CLOUDINARY_URL') + environ.get('CLOUDINARY_NAME') + '/' + data.data[index].get('foto')
            data.data[index]['foto'] = link
            print(link)
        return Response(data={
            'message':'Listado de platos',
            'data':data.data
        })
