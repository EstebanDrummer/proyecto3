from django.http import HttpResponse
from django.shortcuts import render_to_response 
from django.template import RequestContext

def mensaje(request):
	return HttpResponse("Saludo1")

def index(request):
	variable = 'Hola, soy la pagina inicial'
	return render_to_response('PrincipalMDP.html', {'variable': variable}, context_instance=RequestContext(request))	
	#return render_to_response('PrincipalMDP.html')	

def primerBlog(request):
	variable = 'Hola'
	return render_to_response('vista1MDP.html', {'blog_entries':[{"title":"Primero", "body":"Esto hace parte del cuerpo uno"}, {"title":"Segundo", "body":"Esto hace parte del cuerpo dos"}, {"title":"Tercero", "body":"Esto hace parte del cuerpo tres"}]}, context_instance=RequestContext(request))	
	#return render_to_response('PrincipalMDP.html')

def segundoBlog(request):
	variable = 'Hola'
	return render_to_response('vista1MDP.html', {'blog_entries':[{"title":"Cuarto", "body":"Esto hace parte del cuerpo cuatro"}, {"title":"Quinto", "body":"Esto hace parte del cuerpo cinco"}, {"title":"Sexto", "body":"Esto hace parte del cuerpo seis"}]}, context_instance=RequestContext(request))	
	#return render_to_response('PrincipalMDP.html')				