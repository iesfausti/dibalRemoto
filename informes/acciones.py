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
from django.utils.encoding import * 

import sys

from django.http import HttpResponse

from geraldo.generators import PDFGenerator
from febal.models import *

from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField,BAND_WIDTH, Label,  Line,SubReport,FIELD_ACTION_COUNT,FIELD_ACTION_SUM, BAND_WIDTH


from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_RIGHT, TA_CENTER


class informeTickets(Report):
    title = 'Lista de Tickets'
    author = 'John Smith Shoes'

    page_size = landscape(A4)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0.5*cm
        force_new_page = True
        elements=(
            ObjectValue(attribute_name='cod_ticket', left=0.5*cm),
            ObjectValue(attribute_name='vendedor', left=3*cm),
            ObjectValue(attribute_name='importe', left=10*cm),
            
            )

    class band_page_header(ReportBand):
        height = 1.3*cm
        elements = [
                SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                Label(text="ID", top=0.8*cm, left=0.5*cm),
                Label(text=u"Creation Date", top=0.8*cm, left=3*cm),
                SystemField(expression=u'Page %(page_number)d of %(page_count)d', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'bottom': True}
    
    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
                Label(text='Martin Reports', top=0.1*cm),
                SystemField(expression=u'Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}
        
        
    subreports = [
            SubReport(
                queryset_string = '%(object)s.lineaticketventafebal_set.all()',
                band_header = ReportBand(
                    height=0.5*cm,
                    elements=[
                    Label(text='nº', top=0, left=1*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Artículo', top=0, left=3*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Peso', top=0, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Importe(€)', top=0, left=15*cm, style={'fontName': 'Helvetica-Bold'}),
                    ],
                    borders={'top': True, 'left': True, 'right': True},
                   ),            
                detail_band = ReportBand(
                    height=0.5*cm,
                    elements=[
                        ObjectValue(attribute_name='cod_linea_ticket', top=0, left=1*cm),
                        ObjectValue(attribute_name='nombre_articulo', top=0, left=3*cm),
                        ObjectValue(attribute_name='peso', top=0, left=13*cm),
                        ObjectValue(attribute_name='importe', top=0, left=15*cm),
                        ]
                    ),
                
                band_footer = ReportBand(
                    height=0.5*cm,
                    elements=[
                        ObjectValue(attribute_name='cod_linea_ticket', left=4*cm,
                                    action=FIELD_ACTION_COUNT, display_format='%s lineas de ticket',
                                    style={'fontName': 'Helvetica-Bold'}),
                        ObjectValue(attribute_name='importe', left=15*cm,
                                    action=FIELD_ACTION_SUM, display_format='%s euros',
                                    style={'fontName': 'Helvetica-Bold'}),


                    ],
                    borders={'bottom': True, 'left': True, 'right': True},
                    ),                
                ),
            ]    

def creaInformeTickets(request):
    resp = HttpResponse(content_type='application/pdf')

    tickets = CabeceraTicketVentaFebal.objects.order_by('cod_ticket').filter(cod_ticket__lte=12)
    report = informeTickets(queryset=tickets)
    report.generate_by(PDFGenerator, filename=resp)

    return resp

