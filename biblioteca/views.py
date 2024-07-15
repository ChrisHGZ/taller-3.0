from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm,PerfilForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import AutForm
from django.http import JsonResponse
from rest_framework import viewsets
from.serializer import ServicioSerializer

from django.shortcuts import render, redirect
from .models import Servicio
from .forms import ServiciosForm, RegistroUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import CambiarContrasenaForm
# Create your views here.
def autos(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def juego(request):
    return render(request, 'juego.html')

def shop(request):
    return render(request, 'shop.html')

def shop1(request):
    return render(request, 'shop-single1.html')

def prueba(request):
    return render(request, 'prueba.html')

def rest(request):
    return render(request, 'crud.html')

@login_required
def perfil(request):
    if request.method == 'POST':
        formulario = PerfilForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            update_session_auth_hash(request, request.user)  # Mantiene al usuario logueado después de actualizar su perfil
            return redirect('profile')  # Redirige a la página de perfil después de guardar los cambios
    else:
        formulario = PerfilForm(instance=request.user)
        
    return render(request, 'perfil.html', {'form': formulario})
    

def logout_view(request):
    logout(request)
    return redirect('autos') 
    

def registrar(request):
    data = {'form': UserForm()}  # Instancia inicial del formulario vacío
    if request.method == "POST":
        formulario = UserForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()  # Guarda el nuevo usuario y retorna el objeto user
            # Autentica al nuevo usuario
            user = authenticate(username=formulario.cleaned_data["username"], 
                                 password=formulario.cleaned_data["password1"])
            if user is not None:
                login(request, user)  # Inicia la sesión del usuario
                return redirect('autos')  # Redirige a la página principal
            else:
                # Manejo de casos inusuales donde la autenticación falla
                data['error'] = "Ha ocurrido un problema al iniciar sesión. Por favor, intente de nuevo."
        # Si el formulario no es válido, los errores se mostrarán en la plantilla
        data["form"] = formulario
    return render(request, 'registration/register.html', data)

@login_required
def crear_servicio(request):
    if request.method=="POST":
        servicioform=ServiciosForm(request.POST,request.FILES)
        if servicioform.is_valid():
            servicioform.save()     #similar al insert en función
            return redirect ('servicios')
    else:
        servicioform=ServiciosForm()
    return render (request, 'crear.html', {'servicioform': servicioform})
    


def login_view(request):
    if request.method == "POST":
        form = AutForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('autos')  # Redirige a la página principal después de un login exitoso
            else:
                # Autenticación fallida
                form.add_error(None, "El nombre de usuario o la contraseña son incorrectos.")
    else:
        form = AutForm()  # Inicializa el formulario vacío para GET requests
    return render(request, 'registration/login.html', {'form': form})

@login_required
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})


def mostrar_servicios(request):
    servicios = Servicio.objects.all()
    for servicio in servicios:
        print(servicio.imagen.url)  
    return render(request, 'shop.html', {'servicios': servicios})
    

@login_required
def modificar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    if request.method == "POST":
        servicioform = ServiciosForm(request.POST, request.FILES, instance=servicio)
        if servicioform.is_valid():
            servicioform.save()
            return redirect('servicios')
    else:
        servicioform = ServiciosForm(instance=servicio)
    return render(request, 'crear.html', {'servicioform': servicioform, 'modificar': True})


@login_required
def eliminar_servicio(request, id): 
    servicioEliminado = Servicio.objects.get(id=id) #similar a select * from... where...
    servicioEliminado.delete()
    return redirect ('servicios')


@login_required
def eliminar_shop(request, id): 
    servicioEliminado = Servicio.objects.get(id=id) #similar a select * from... where...
    servicioEliminado.delete()
    return redirect ('shop')

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Servicio, Carrito, ElementoCarrito
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def agregar_al_carrito(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    elemento, created = ElementoCarrito.objects.get_or_create(carrito=carrito, servicio=servicio)
    if not created:
        elemento.cantidad += 1
        elemento.save()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        elementos = carrito.elementos.all()
        total = sum(elemento.total_precio for elemento in elementos)
        html = render_to_string('carrito.html', {'carrito': carrito, 'total': total})
        return JsonResponse({'html': html})

    return redirect('ver_carrito')


@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'carrito.html', {'carrito': carrito})

@login_required
def actualizar_elemento_carrito(request, elemento_id, accion):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id, carrito__usuario=request.user)
    
    if accion == 'aumentar':
        elemento.cantidad += 1
    elif accion == 'reducir':
        elemento.cantidad -= 1
    
    if elemento.cantidad == 0:
        elemento.delete()
    else:
        elemento.save()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        carrito = elemento.carrito
        elementos = carrito.elementos.all()
        total = sum(elemento.total_precio for elemento in elementos)
        html = render_to_string('carrito.html', {'carrito': carrito, 'total': total})
        return JsonResponse({'html': html})

    return redirect('ver_carrito')

class PerfilView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'perfil.html'
    form_class = PerfilForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        messages.success(self.request, "Tu perfil ha sido actualizado con éxito.")
        return redirect('perfil')

class ActualizarPerfilView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'actualizar_perfil.html'
    form_class = PerfilForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        messages.success(self.request, "Tu perfil ha sido actualizado con éxito.")
        return redirect('perfil')

class CambiarContrasenaView(PasswordChangeView):
    template_name = 'cambiar_contraseña.html'
    form_class = CambiarContrasenaForm
    success_url = reverse_lazy('perfil')  # Redirige a la página de perfil después del cambio de contraseña

from django.shortcuts import render
from django.views import View
from .models import Carrito

class BoletaView(View):
    def get(self, request):
        carrito = Carrito.objects.get(usuario=request.user)
        elementos = carrito.elementos.all()
        
        # Calcular el total del carrito
        total = sum(elemento.total_precio for elemento in elementos)

        context = {
            'elementos': elementos,
            'total': total,
        }

        return render(request, 'boleta.html', context)

    def post(self, request):
        # Obtén el carrito del usuario actual
        carrito = get_object_or_404(Carrito, usuario=request.user)

        # Limpiar el carrito
        carrito.elementos.all().delete()

        # Redirigir a la página de compras para continuar comprando
        return redirect('shop')
    
    
class ComprarView(View):
    def get(self, request):
        # Aquí podrías realizar acciones adicionales relacionadas con la compra
        # por ejemplo, generar una orden de compra, procesar un pago, etc.

        # Redirigir a la página de boleta después de realizar la compra
        return redirect('boleta')

    def post(self, request):
        # Obtén el carrito del usuario actual
        carrito = get_object_or_404(Carrito, usuario=request.user)

        # Limpiar el carrito
        carrito.elementos.all().delete()

        # Redirigir a la página de compras para continuar comprando
        return redirect('shop')







from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Carrito, ElementoCarrito

@method_decorator(login_required, name='dispatch')
class EliminarElementoCarritoView(View):
    def get(self, request, elemento_id):
        elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
        carrito = Carrito.objects.get(usuario=request.user)
        carrito.elementos.filter(servicio=elemento.servicio).delete()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            elementos = carrito.elementos.all()
            total = sum(elemento.total_precio for elemento in elementos)
            html = render_to_string('carrito.html', {'carrito': carrito, 'total': total})
            return JsonResponse({'html': html})

        return redirect('ver_carrito')

@method_decorator(login_required, name='dispatch')
class LimpiarCarritoView(View):
    def get(self, request):
        carrito = Carrito.objects.get(usuario=request.user)
        carrito.elementos.all().delete()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            elementos = carrito.elementos.all()
            total = sum(elemento.total_precio for elemento in elementos)
            html = render_to_string('carrito.html', {'carrito': carrito, 'total': total})
            return JsonResponse({'html': html})

        return redirect('ver_carrito')
    

class LimpiarCarritoDesdeBoletaView(View):
    def post(self, request):
        # Obtén el carrito del usuario actual
        carrito = get_object_or_404(Carrito, usuario=request.user)

        # Limpiar el carrito
        carrito.elementos.all().delete()

        # Redirigir a la página de compras para continuar comprando
        return redirect('shop')

def search_servicios(request):
    query = request.GET.get('q')
    if query:
        resultados = Servicio.objects.filter(servicio__icontains=query)
    else:
        resultados = Servicio.objects.all()
    context = {
        'servicios': resultados
    }
    return render(request, 'shop.html', context)


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class= ServicioSerializer










from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm