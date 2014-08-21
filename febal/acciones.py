# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os, sys, time, zipfile
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper


from febal.models import *
from django.db import connection, transaction

from django.db import connections
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist    
from datetime import datetime

from django.forms.models import model_to_dict

from django.http import HttpResponseRedirect

def crearAgrupadoTickets_Lista(request,lista_tickets):
	#Creo un agrupado
	if lista_tickets.count() == 0:
		return HttpResponseRedirect('/admin/')
	
	nimport = Importacion.objects.all().filter(usuario = request.user)[0]
	agrupado = AgrupadoCabeceraTicket( fecha = datetime.now(),importacion = nimport )
	agrupado.save()
	importe_total = 0
	for ticket in lista_tickets:
		agrupado.tickets.add(ticket) 
		for linea in ticket.lineaticketventafebal_set.all():
			
			agrupado_linea = AgrupadoLineaTicket(ticket_agrupado = agrupado,importacion = nimport)
			agrupado_linea.cod_ticket_agrupado = agrupado
			agrupado_linea.cod_linea_ticket = linea
			agrupado_linea.fecha = datetime.now()
			agrupado_linea.importe = linea.importe
			agrupado_linea.incluir = True
			importe_total = importe_total +linea.importe
			agrupado_linea.save()

	agrupado.importe = importe_total
	agrupado.save()

	return HttpResponseRedirect('/admin/')