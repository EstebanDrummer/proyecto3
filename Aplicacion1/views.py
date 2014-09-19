from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from Aplicacion1.forms import ContactoForm
from Aplicacion1.forms import SeleccionForm
from Aplicacion1.forms import ValorForm
from django.core.mail import EmailMessage

def mensaje(request):
	return HttpResponse("Saludo")

def index(request):
	return render_to_response('index.html')	

def DolaresAPesos(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			contenido1 = int(formulario.cleaned_data['valor'])
			contenido2= 1890*contenido1
			result="%i Dolares equivalen a %i  pesos Colombianos" % (contenido1, contenido2)
			##formulario = ContactoForm()
			return render_to_response('contactoform.html', {'formulario':formulario, 'result': result}, context_instance=RequestContext(request))
			##return HttpResponse("%i Dolares equivalen a %i  pesos Colombianos" % (contenido1, contenido2))
	else:
		formulario = ContactoForm()
		
	return render_to_response('contactoform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def PesosADolares(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			contenido1 = int(formulario.cleaned_data['valor'])
			contenido2= contenido1/1890
			result="%i Pesos equivalen a %i  Dolares" % (contenido1, contenido2)
			return render_to_response('contactoform.html', {'formulario':formulario, 'result': result}, context_instance=RequestContext(request))
	else:
		formulario = ContactoForm()
		
	return render_to_response('contactoform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def Seleccion(request):
	if request.method=='POST':
		seleccion = SeleccionForm(request.POST)
		if seleccion.is_valid():
			contenido1 = seleccion.cleaned_data['Monedas']
			valor=ValorForm()
			#return HttpResponse("%s es el valor" % (contenido1))
			#Enviamos a renderizar el Valor
			return render_to_response('valorform.html', {'valor':valor, 'contenido1': contenido1}, context_instance=RequestContext(request))
	else:
		seleccion = SeleccionForm()
	
	return render_to_response('seleccionform.html', {'seleccion':seleccion}, context_instance=RequestContext(request))	

def Valor(request,var):

#	return HttpResponse("Hola %s" % id)
	if request.method=='POST':
		valor = ValorForm(request.POST)
		if valor.is_valid():
			inicial = int(valor.cleaned_data['valor'])
			if var == 'PAD':
				final=inicial/1890
				mensaje="%i Pesos equivalen a %i  Dolares" % (inicial, final)
			else:
				final=inicial*1890
				mensaje="%i Dolares equivalen a %i  pesos Colombianos" % (inicial, final)
			return render_to_response('respuestaform.html', {'mensaje':mensaje}, context_instance=RequestContext(request))
	else:
		valor = ValorForm()
	
	#return HttpResponse(" pepe es el valor" )
	return render_to_response('valorform.html', {'valor':valor, 'contenido1': var}, context_instance=RequestContext(request))	
