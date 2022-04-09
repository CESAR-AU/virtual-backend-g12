from django.test import TestCase
from rest_framework.test import  APITestCase

# Create your tests here.
class EtiquetasTestCase(APITestCase):
    def test_crear_etiqueta_success(self):
        request = self.client.post('/app/etiquetas', {
            'nombre':'Demo test'
        })
        self.assertEqual(request.status_code, 201)
        self.assertEqual(1 , 1)
    
    def test_listar_etiqueta_success(self):
        request = self.client.get('/app/etiquetas')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(1 , 1)
