from django.urls import path
from MobikeApp import views
from django.contrib.auth.views import LoginView, login_required,logout_then_login
from .views import Registro, login, AdminListarUsuario, AdminReportes, AdminCrearUsuario, AdminView,UsuarioView, FuncionarioView, FuncionarioReporte, AdminEditarUsuario

urlpatterns = [
    path('', views.login, name="Login"),
    path('registro/', Registro.as_view(), name="Registro"),
    path('admin-mobike/', AdminView.as_view(), name="Admin-mobike"),
    path('admin-mobike/gestionar-usuario/', AdminListarUsuario.as_view(), name="GestionarUsuarios"),
    path('admin-mobike/gestionar-usuario/crear', AdminCrearUsuario, name="CrearUsuarios"),
    path('admin-mobike/reportes/', AdminReportes.as_view(), name="Admin-Reportes"),
    path('usuario/', UsuarioView.as_view(),name="Usuario"),
    path('funcionario/', FuncionarioView.as_view(),name="Funcionario"),
    path('funcionario/reportes/', FuncionarioReporte.as_view(),name="FuncionarioReportes"),
    path('admin-mobike/gestionar-usuario/editar/<int:id_usuario>',AdminEditarUsuario.as_view(),name="EditarUsuario"),
]
 
