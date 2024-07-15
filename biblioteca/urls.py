from django.urls import path, include
from .views import *
from biblioteca.views import * 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from biblioteca import views

router=routers.DefaultRouter()
router.register(r'servicio', views.ServicioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', autos, name="autos"),
    path('about' , about, name="about"),
    path('contact' , contact, name="contact"),
    path('juego' , juego, name="juego"),
    path('shop' , mostrar_servicios, name="shop"),
    path('shop1' , shop1, name="shop1"),
    path('prueba', prueba, name="prueba"),
    path('login', login_view, name="login"),
    path('register', registrar, name="register"),
    path('perfil', perfil, name="perfil"),
    path('logout',logout_view,name="logout"),
    path('servicios/', servicios, name="servicios"),
    path('crear/', crear_servicio, name="crear"),
    path('eliminar/<int:id>/',eliminar_servicio, name='eliminar'),
    path('eliminar_shop/<int:id>/',eliminar_shop, name='eliminar_shop'),
    path('modificar/<int:servicio_id>/',modificar_servicio, name='modificar'),
    path('agregar_al_carrito/<int:servicio_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('actualizar_elemento_carrito/<int:elemento_id>/<str:accion>/', actualizar_elemento_carrito, name='actualizar_elemento_carrito'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('actualizar-perfil/', ActualizarPerfilView.as_view(), name='actualizar_perfil'),
    path('cambiar-contrasena/', CambiarContrasenaView.as_view(), name='cambiar_contrasena'),
    path('limpiar_carrito/', LimpiarCarritoView.as_view(), name='limpiar_carrito'),
    path('boleta/', BoletaView.as_view(), name='boleta'),
    path('comprar/', ComprarView.as_view(), name='comprar'),
    path('eliminar_elemento_carrito/<int:elemento_id>/', EliminarElementoCarritoView.as_view(), name='eliminar_elemento_carrito'),
    path('limpiar_carrito_desde_boleta/', LimpiarCarritoDesdeBoletaView.as_view(), name='limpiar_carrito_desde_boleta'),
    path('search/', search_servicios, name='search_servicios'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)