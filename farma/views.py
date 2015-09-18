from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate

def get_order(get):
    if "o" in get:
        return get["o"]

def inicio(request):
    return render(request, "inicio.html")

def altafarmacia(request):
	return render(request, "altafarmacia.html")

def altaMedicamento(request):
	return render(request, "altaMedicamento.html")

def pedidoLaboratorio(request):
	return render(request, "pedidoLaboratorio.html")

def recepcionPedidoLaboratorio(request):
	return render(request, "recepcionPedidoLaboratorio.html")

def pedidoDeFarmacia(request):
	return render(request, "pedidoDeFarmacia.html")

def pedidoDeClinica(request):
	return render(request, "pedidoDeClinica.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
               if user.is_active:
                   login(request, user)
                   return redirect('inicio')
               else:
                   return HttpResponse('inactive')
    return render(request, "login.html")
