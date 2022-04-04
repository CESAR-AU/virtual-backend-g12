import unittest
from app import app
from datetime import datetime

class TestInicioFlask(unittest.TestCase):
    def setUp(self):
        self.nombre = 'Juan'
        # inicia mi aplicacion de flask coun cliente test
        self.aplicacion_flask = app.test_client()
        # return super().setUp()
    
    @unittest.skip('Lo salte por que si')
    def testNombre(self):
        self.assertEqual(self.nombre, 'Juan')
    
    def testEndpointStatus(self):
        '''Deberia de retornar un la hora del servidor y su estado'''
        respuesta = self.aplicacion_flask.get('/status')
        print(respuesta.status)
        print(respuesta.json)
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json.get('success'), True)
        self.assertEqual(respuesta.json.get('hora_del_servidor'), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    def testLoginJWTExitoso(self):
        '''Deberia de retornar un un token para poder ingresar a las rutas protegidas'''
        body={
            'correo':'ricardo@c-innova.pe',
            'password':'123'
        }
        respuesta = self.aplicacion_flask.post('/login_jwt', json=body)
        self.assertEqual(respuesta.status_code, 200)
        # self.assertEqual(respuesta.json.get('access_token'), not None)
        self.assertNotEqual(respuesta.json.get('access_token'), None)

    def testLoginJWTCredencialesIncorrectas(self):
        '''Deberia de retornar un error si las credenciales son incorrectas'''
        body={
            'correo':'ricardo@c-innova.pe',
            'password':'123sss'
        }
        respuesta = self.aplicacion_flask.post('/login_jwt', json=body)
        print(respuesta.json)
        self.assertEqual(respuesta.status_code, 401)
        self.assertEqual(respuesta.json.get('access_token'), None)
    

class TestPerfil(unittest.TestCase):
    def setUp(self):
        self.aplicacion_flask = app.test_client()
        body={
            'correo':'ricardo@c-innova.pe',
            'password':'123'
        }
        respuesta = self.aplicacion_flask.post('/login_jwt', json=body)
        self.token = respuesta.json.get('access_token')
    
    def testNoHayJWT(self):
        '''Debera retornar false si no se pasa el token de acceso'''
        respuesta = self.aplicacion_flask.get('/perfil')
        print('NO HAY TOKEN: ', respuesta.json)
        self.assertEqual(respuesta.status_code, 401)
        self.assertEqual(respuesta.json.get('error'), 'Authorization Required')
        self.assertEqual(respuesta.json.get('description'), 'Request does not contain an access token')
    
    def testPerfil(self):
        '''Debera retornar True y el perfil de usuario'''
        respuesta = self.aplicacion_flask.get('/perfil', headers={'Authorization':'Bearer {}'.format(self.token)})
        print(respuesta)
        self.assertEqual(respuesta.status_code, 200)
        self.assertNotEqual(respuesta.json.get('message'), None)

class TestMovimientos(unittest.TestCase):
    # TODO: hacer los test para extraer los movimientos creados del usuario, hacer el caso cuando se pase una JWT, cuando no se pase una token, cuando no tenga movimientos y cuando tenga movimientos
    pass