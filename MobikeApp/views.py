from django.shortcuts import render, HttpResponse, redirect
from MobikeApp.forms import FormularioLogin, FormularioCrearUsuario
from django.views.generic.base import TemplateView
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
                return render(request, "MobikeApp/admin.html")

            elif form.get('usuario') == "funcionario":
                return render(request, "Mobikeapp/funcionario.html")

            elif form.get('usuario') == "usuario":
                return render(request, "Mobikeapp/usuario.html")
            
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


def AdminListarUsuario(request):
   
    usuarios = UsuarioMobike.objects.all()

    data = {
        'usuarios':usuarios
    }
    
    return render(request, "MobikeApp/admin-gestionar-usuario.html", data)







class AdminReportes(TemplateView):

    template_name = "MobikeApp/admin-reportes.html"

#-----------------------------------------------------------------------# 
class UsuarioView(TemplateView):
    template_name = "MobikeApp/usuario.html"

#-----------------------------------------------------------------------# 
class FuncionarioView(TemplateView):
    template_name = "MobikeApp/funcionario.html"

class FuncionarioReporte(TemplateView):
    template_name = "MobikeApp/funcionario-reportes.html"