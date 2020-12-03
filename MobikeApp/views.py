from django.shortcuts import render, HttpResponse, redirect
from MobikeApp.forms import FormularioLogin, FormularioCrearUsuario
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib import messages
from .models import UsuarioMobike

#-----------------------------------------------------------------------# 
class Registro(TemplateView):

    template_name = "MobikeApp/registro.html"
#-----------------------------------------------------------------------# 

def login(request):

    if request.method == "POST":
        miFormulario = FormularioLogin(request.POST)

        if miFormulario.is_valid():

            form=miFormulario.cleaned_data

            if form.get('usuario') == "admin":
                return redirect(to="Admin-mobike")

            elif form.get('usuario') == "funcionario":
                return redirect(to="Funcionario")

            elif form.get('usuario') == "usuario":
                return redirect(to="Usuario")
            
            else:
                return render(request, "Mobikeapp/inicioMal.html")

    else:
        miFormulario = FormularioLogin()
        return render(request, "Mobikeapp/login.html", {"form": miFormulario})

#-----------------------------------------------------------------------# 


class AdminView(TemplateView):
    template_name = "MobikeApp/admin.html"



def AdminCrearUsuario(request):

    data = {
        'form':FormularioCrearUsuario()
    }

    if request.method == 'POST':
        datosForm = FormularioCrearUsuario(data=request.POST)

        if datosForm.is_valid():
            datosForm.save()
            return redirect(to='GestionarUsuarios')
            
    return render(request, "MobikeApp/admin-crear-usuario.html", data)


class AdminListarUsuario(View):
    def get(self, request):
        usuarios = UsuarioMobike.objects.all()
        data = {
            'usuarios':usuarios,
        }    
        return render(request, "MobikeApp/admin-gestionar-usuario.html", data)
    
    def post(self, request):        
        if "edit" in request.POST["accion"]:
            id = request.POST["accion"].split("-")[1]
            return redirect(to="EditarUsuario",id_usuario=id)         
            
        elif "del" in request.POST["accion"]:
            id = request.POST["accion"].split("-")[1]
            print(request.POST["accion"])
            nombre = UsuarioMobike.objects.get(id=id).nombres            
            UsuarioMobike.objects.get(id=id).delete()
            messages.info(request, f"Usuario {nombre} fue eliminado correctamente")
            return redirect(to="GestionarUsuarios")


class AdminEditarUsuario(View):
    def get(self, request, id_usuario):
        user = UsuarioMobike.objects.get(id=id_usuario)
        context = {"user":user}
        return render(request, 'MobikeApp/admin-editar-usuario.html', context)
    def post(self, request, id_usuario):
        if request.POST["accion"]=="editar":
            nombre=request.POST.get("nombre")
            direccion=request.POST.get("direccion")
            email=request.POST.get("email")
            UsuarioMobike.objects.filter(id=request.POST.get("id")).update(direccion=direccion,email=email)
            messages.info(request, f"Usuario {nombre} fue editado correctamente")
            return redirect(to="GestionarUsuarios") 
        else:
            return redirect(to="GestionarUsuarios") 






class AdminReportes(TemplateView):

    template_name = "MobikeApp/admin-reportes.html"

#-----------------------------------------------------------------------# 
class UsuarioView(View):
    def get(self, request):
        return render(request,'MobikeApp/usuario.html',{'estacionamiento':0})
    def post(self, request):
        if request.POST["estacionamiento"] == "est1":
            return render(request,'MobikeApp/usuario.html',{'estacionamiento':1})
        elif request.POST["estacionamiento"] == "est2":
            return render(request,'MobikeApp/usuario.html',{'estacionamiento':2})
        elif request.POST["estacionamiento"] == "est3":
            return render(request,'MobikeApp/usuario.html',{'estacionamiento':3})
    
#-----------------------------------------------------------------------# 
class FuncionarioView(TemplateView):
    template_name = "MobikeApp/funcionario.html"

class FuncionarioReporte(TemplateView):
    template_name = "MobikeApp/funcionario-reportes.html"