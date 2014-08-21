# Create your views here.


# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template import RequestContext,loader
from django.db.models import *
from forms import *
from acciones import *

from django.core.paginator import Paginator

def informeTickets(request):
	resp = creaInformeTickets(request)
	if request.method == 'POST': # If the form has been submitted...
		form = importacionesDibalForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Importo
			# ...
			
			return HttpResponseRedirect('/admin') # Redirect after POST
	else:
		form = informesTicketsDibalForm() # An unbound form

	return resp
