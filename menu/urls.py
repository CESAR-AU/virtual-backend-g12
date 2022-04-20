from django.urls import path
from .views import PlatoApiView, StockApiView, PedidoApiView, AgregarDetallePedidoApiView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', PlatoApiView.as_view()),
    path('stock', StockApiView.as_view()),
    path('pedido', PedidoApiView.as_view()),
    path('agregar-detalle-pedido', AgregarDetallePedidoApiView.as_view()),
]