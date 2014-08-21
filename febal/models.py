# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import *

class Importacion(models.Model):
    '''
    Representa la base de datos extraida del fichero 'imexalum.xml' que proviene de la opción del ITACA
    de exportar un centro. Cada conjunto de datos exportados tienen una fecha y pueden coexistir en la misma aplicación
    Marcar la opción 'ocultar' en las importaciones anteriores es lo normal al inicio del curso. 
    '''
    codigo = models.CharField(max_length=10L, blank=True)
    usuario = models.ForeignKey(User)
    clientefebal = models.CharField(max_length=255L, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    ultimoticket = models.IntegerField(null=True,  blank=True)
    ultimocliente = models.IntegerField(null=True,  blank=True) 
    ultimoarticulo = models.IntegerField(null=True,  blank=True) 
    version = models.CharField(max_length=10L, blank=True)
    ocultar  = models.BooleanField(blank=True,default = True)
    rutaDibalRMS = models.CharField(max_length=255L, blank=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s total(%s)' % (self.clientefebal ,self.ultimoticket) 
class Vendedor(models.Model):
    id = models.AutoField(null=False,primary_key=True)    
    importacion = models.ForeignKey(Importacion)
    codigo = models.IntegerField(null=False, blank=True)
    nombre = models.CharField(max_length=48, db_column='Nombre', blank=True)
    nif = models.CharField(max_length=9, db_column='NIF', blank=True)
    direccion = models.CharField(max_length=48, db_column='Direccion', blank=True)
    poblacion = models.CharField(max_length=24, db_column='Poblacion', blank=True)
    provincia = models.CharField(max_length=24, db_column='Provincia', blank=True)
    cod_postal = models.IntegerField(null=True, db_column='Cod_Postal', blank=True)
    telefono = models.CharField(max_length=15, db_column='Telefono', blank=True)
    telefono2 = models.CharField(max_length=15, db_column='Telefono2', blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s %s' % (self.codigo,self.nombre)  
class Cliente(models.Model):
    id = models.AutoField(null=False,primary_key=True)    
    importacion = models.ForeignKey(Importacion)
    codigo = models.IntegerField(null=False, blank=True)
    nombre = models.CharField(max_length=48, db_column='Nombre', blank=True)
    nif = models.CharField(max_length=9, db_column='NIF', blank=True)
    direccion = models.CharField(max_length=48, db_column='Direccion', blank=True)
    poblacion = models.CharField(max_length=24, db_column='Poblacion', blank=True)
    provincia = models.CharField(max_length=24, db_column='Provincia', blank=True)
    cod_postal = models.IntegerField(null=True, db_column='Cod_Postal', blank=True)
    telefono = models.CharField(max_length=15, db_column='Telefono', blank=True)
    fax = models.CharField(max_length=15, db_column='Fax', blank=True)
    contacto1 = models.CharField(max_length=48, db_column='Contacto1', blank=True)
    contacto2 = models.CharField(max_length=48, db_column='Contacto2', blank=True)
    forma_pago = models.CharField(max_length=15, db_column='Forma_Pago', blank=True)
    observaciones = models.CharField(max_length=200, db_column='Observaciones', blank=True)


    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s' % (self.nombre)        



class Articulo(models.Model):
    id = models.AutoField(null=False,primary_key=True)    
    importacion = models.ForeignKey(Importacion)
    cod_articulo = models.IntegerField(null=False, blank=True)
    cod_familia = models.SmallIntegerField(null=True, blank=True)
    cod_subfamilia = models.SmallIntegerField(null=True, blank=True)
    tipo = models.SmallIntegerField(null=True, blank=True)
    cod_rapido = models.SmallIntegerField(null=True, blank=True)
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, blank=True)
    caducidad = models.IntegerField(null=True, blank=True)
    iva = models.SmallIntegerField(null=True, blank=True)
    departamento = models.IntegerField(null=True, blank=True)
    seccion = models.SmallIntegerField(null=True, blank=True)
    tara = models.IntegerField(null=True, blank=True)
    formato = models.SmallIntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=32, blank=True)
    nombre2 = models.CharField(max_length=32, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s %s' % (self.cod_articulo,self.nombre)        


class CabeceraTicketVentaFebal(models.Model):
    id = models.AutoField(null=False,primary_key=True)    
    importacion = models.ForeignKey(Importacion)
    cod_ticket = models.IntegerField(null=False, blank=True)
    tienda = models.SmallIntegerField(null=True, blank=True)
    numtramo = models.SmallIntegerField(null=True, blank=True)
    seccion = models.SmallIntegerField(null=True,  blank=True)
    balanza = models.SmallIntegerField(null=True, blank=True)
    num_ticket = models.IntegerField(null=True, blank=True)
    clave = models.CharField(max_length=1, blank=True)
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, blank=True)
    vendedor =  models.ForeignKey(Vendedor)# models.IntegerField(null=True, db_column='Vendedor', blank=True)
    nombre_vendedor = models.CharField(max_length=50, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    hora = models.CharField(max_length=5, blank=True)
    num_operaciones = models.IntegerField(null=True, blank=True)
    importe_dto = models.DecimalField(decimal_places=4, null=True, max_digits=19, blank=True)
    parametro20 = models.SmallIntegerField(null=True, blank=True)
    exportado = models.SmallIntegerField(null=True, blank=True)
    findiatratado = models.SmallIntegerField(null=True, blank=True)
    nummensajetramo = models.SmallIntegerField(null=True, blank=True)
    numerocliente =  models.ForeignKey(Cliente)#models.IntegerField(null=True, db_column='NumeroCliente', blank=True)
    modopago1 = models.SmallIntegerField(null=True, blank=True)
    importemodopago1 = models.DecimalField(decimal_places=4, null=True, max_digits=19,  blank=True)
    modopago2 = models.SmallIntegerField(null=True, blank=True)
    importemodopago2 = models.DecimalField(decimal_places=4, null=True, max_digits=19, blank=True)
    chequeado = models.SmallIntegerField(null=True, blank=True)
    importepagado = models.FloatField(null=True, blank=True)
    pagado = models.SmallIntegerField(null=True,blank=True)
    fechapagado = models.DateTimeField(null=True, blank=True)
    nalbaran = models.IntegerField(null=True, blank=True)
    fechaalbaran = models.DateTimeField(null=True, blank=True)
    descuentototal = models.IntegerField(null=True, blank=True)
    redondeo = models.IntegerField(null=True, blank=True)
    ticket_fiscal = models.IntegerField(null=True, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s ,  %s , %s, (%s €)' % (self.cod_ticket, self.fecha.strftime('%d-%m-%Y'),self.numerocliente ,self.importe)        

		
class LineaTicketVentaFebal(models.Model):
    id = models.AutoField(null=False,primary_key=True)
    importacion = models.ForeignKey(Importacion)
    cod_ticket = models.ForeignKey(CabeceraTicketVentaFebal)#models.IntegerField(null=False, db_column='Cod_Ticket', blank=True)
    cod_linea_ticket = models.IntegerField(null=False, blank=True)
    codigo = models.ForeignKey(Articulo)
    nombre_articulo = models.CharField(max_length=50, blank=True)
    peso = models.FloatField(null=True, blank=True)
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, blank=True)
    tipo_operacion = models.CharField(max_length=1, db_column='Tipo_Operacion', blank=True)
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True)
    facturado = models.SmallIntegerField(null=True, db_column='Facturado', blank=True)
    cod_pedido = models.IntegerField(null=True, db_column='Cod_Pedido', blank=True)
    tipoiva = models.SmallIntegerField(null=True, db_column='TipoIVA', blank=True)
    porcentajeiva = models.FloatField(null=True, db_column='PorcentajeIVA', blank=True)
    importeiva = models.FloatField(null=True, db_column='ImporteIVA', blank=True)
    preciocoste = models.FloatField(null=True, db_column='PrecioCoste', blank=True)

    
    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s %s' % (self.cod_ticket,self.cod_linea_ticket)        

class AgrupadoCabeceraTicket(models.Model):
    id = models.AutoField(null=False,primary_key=True)
    importacion = models.ForeignKey(Importacion)
    fecha = models.DateTimeField(null=True, blank=True)
    tickets = models.ManyToManyField(CabeceraTicketVentaFebal)
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        st = ""
        for t in self.tickets.all():
            st = st + (u' %s,' % t.cod_ticket)
        return u'[%s]' % (st)        

class AgrupadoLineaTicket(models.Model):
    importacion = models.ForeignKey(Importacion)
    id = models.AutoField(null=False,primary_key=True)
    ticket_agrupado = models.ForeignKey(AgrupadoCabeceraTicket)
    cod_linea_ticket = models.ForeignKey(LineaTicketVentaFebal,null=False) 
    fecha = models.DateTimeField(null=True, blank=True)
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, blank=True)
    incluir = models.NullBooleanField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s %s, (%s €)' % (self.ticket_agrupado,self.fecha.strftime('%d-%m-%Y'),self.importe)        
    