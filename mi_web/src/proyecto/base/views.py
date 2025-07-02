# Importaciones necesarias de Django para vistas, autenticación y modelos
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tarea

# Vista para el inicio de sesión de usuarios
class Logueo(LoginView):
    template_name = 'base/login.html'  # Plantilla a usar
    fields = '__all__'
    redirect_authenticated_user = True  # Redirige si ya está autenticado

    def get_success_url(self):
        # Redirige a la lista de tareas después de iniciar sesión
        return reverse_lazy('tareas')

# Vista para el registro de nuevos usuarios
class PaginaRegistro(FormView):
    template_name = 'base/registro.html'  # Plantilla a usar
    form_class = UserCreationForm  # Formulario de creación de usuario
    redirect_authenticated_user = True  # Redirige si ya está autenticado
    success_url = reverse_lazy('tareas')  # Redirección tras registro exitoso

    def form_valid(self, form):
        # Si el formulario es válido, crea el usuario y lo inicia sesión
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)

    def get(self, *args, **kwargs):
        # Si el usuario ya está autenticado, redirige a tareas
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro, self).get(*args, **kwargs)

# Vista para listar las tareas pendientes del usuario autenticado
class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea  # Modelo a usar
    context_object_name = 'tareas'  # Nombre del contexto en la plantilla

    def get_context_data(self, **kwargs):
        # Personaliza el contexto para filtrar tareas por usuario y búsqueda
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()

        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
            context['valor_buscado'] = valor_buscado
        return context

# Vista para mostrar el detalle de una tarea específica
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea  # Modelo a usar
    context_object_name = 'tarea'  # Nombre del contexto en la plantilla
    template_name = 'base/tarea.html'  # Plantilla a usar

# Vista para crear una nueva tarea
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea  # Modelo a usar
    fields = ['titulo', 'descripcion', 'completo']  # Campos del formulario
    success_url = reverse_lazy('tareas')  # Redirección tras creación

    def form_valid(self, form):
        # Asigna el usuario autenticado a la tarea antes de guardar
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)

# Vista para editar una tarea existente
class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea  # Modelo a usar
    fields = ['titulo', 'descripcion', 'completo']  # Campos editables
    success_url = reverse_lazy('tareas')  # Redirección tras edición

# Vista para eliminar una tarea existente
class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea  # Modelo a usar
    context_object_name = 'tarea'  # Nombre del contexto en la plantilla
    success_url = reverse_lazy('tareas')  # Redirección tras eliminación
