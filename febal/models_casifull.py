# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
# -*- coding: utf-8 -*-
from django.db import models

class Articulo(models.Model):
    cod_articulo = models.IntegerField(null=True, primary_key=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    cod_familia = models.SmallIntegerField(null=True, db_column='Cod_Familia', blank=True) # Field name made lowercase.
    cod_subfamilia = models.SmallIntegerField(null=True, db_column='Cod_Subfamilia', blank=True) # Field name made lowercase.
    tipo = models.SmallIntegerField(null=True, db_column='Tipo', blank=True) # Field name made lowercase.
    cod_rapido = models.SmallIntegerField(null=True, db_column='Cod_Rapido', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    caducidad = models.IntegerField(null=True, db_column='Caducidad', blank=True) # Field name made lowercase.
    iva = models.SmallIntegerField(null=True, db_column='IVA', blank=True) # Field name made lowercase.
    departamento = models.IntegerField(null=True, db_column='Departamento', blank=True) # Field name made lowercase.
    seccion = models.SmallIntegerField(null=True, db_column='Seccion', blank=True) # Field name made lowercase.
    tara = models.IntegerField(null=True, db_column='Tara', blank=True) # Field name made lowercase.
    formato = models.SmallIntegerField(null=True, db_column='Formato', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=32, db_column='Nombre', blank=True) # Field name made lowercase.
    nombre2 = models.CharField(max_length=32, db_column='Nombre2', blank=True) # Field name made lowercase.
    texto1 = models.CharField(max_length=48, db_column='Texto1', blank=True) # Field name made lowercase.
    texto2 = models.CharField(max_length=48, db_column='Texto2', blank=True) # Field name made lowercase.
    texto3 = models.CharField(max_length=48, db_column='Texto3', blank=True) # Field name made lowercase.
    texto4 = models.CharField(max_length=48, db_column='Texto4', blank=True) # Field name made lowercase.
    texto5 = models.CharField(max_length=48, db_column='Texto5', blank=True) # Field name made lowercase.
    texto6 = models.CharField(max_length=48, db_column='Texto6', blank=True) # Field name made lowercase.
    texto7 = models.CharField(max_length=48, db_column='Texto7', blank=True) # Field name made lowercase.
    texto8 = models.CharField(max_length=48, db_column='Texto8', blank=True) # Field name made lowercase.
    texto9 = models.CharField(max_length=48, db_column='Texto9', blank=True) # Field name made lowercase.
    texto10 = models.CharField(max_length=48, db_column='Texto10', blank=True) # Field name made lowercase.
    precio_oferta = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Oferta', blank=True) # Field name made lowercase.
    fecha_extra = models.IntegerField(null=True, db_column='Fecha_Extra', blank=True) # Field name made lowercase.
    formato_ean = models.SmallIntegerField(null=True, db_column='Formato_EAN', blank=True) # Field name made lowercase.
    rentabilidad = models.SmallIntegerField(null=True, db_column='Rentabilidad', blank=True) # Field name made lowercase.
    promocion = models.BooleanField(db_column='Promocion') # Field name made lowercase.
    precio_promocion = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Promocion', blank=True) # Field name made lowercase.
    com_promocion = models.DateTimeField(null=True, db_column='Com_Promocion', blank=True) # Field name made lowercase.
    fin_promocion = models.DateTimeField(null=True, db_column='Fin_Promocion', blank=True) # Field name made lowercase.
    stock = models.BooleanField(db_column='Stock') # Field name made lowercase.
    existencias = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Existencias', blank=True) # Field name made lowercase.
    perdidas = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Perdidas', blank=True) # Field name made lowercase.
    stock_min = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Stock_Min', blank=True) # Field name made lowercase.
    stock_max = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Stock_Max', blank=True) # Field name made lowercase.
    aviso = models.BooleanField(db_column='Aviso') # Field name made lowercase.
    num_oper = models.IntegerField(null=True, db_column='Num_Oper', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    peso = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Peso', blank=True) # Field name made lowercase.
    margen_objetivo = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Margen_Objetivo', blank=True) # Field name made lowercase.
    precio_anterior = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Anterior', blank=True) # Field name made lowercase.
    promocion_actualizada = models.BooleanField(db_column='Promocion_Actualizada') # Field name made lowercase.
    precio_costo = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Costo', blank=True) # Field name made lowercase.
    cantidad_comprada = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Cantidad_Comprada', blank=True) # Field name made lowercase.
    precio_ultima_compra = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Ultima_Compra', blank=True) # Field name made lowercase.
    precio_medio_venta = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Medio_Venta', blank=True) # Field name made lowercase.
    cantidad_vendida = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Cantidad_Vendida', blank=True) # Field name made lowercase.
    precio_ultima_venta = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Ultima_Venta', blank=True) # Field name made lowercase.
    ean_scanner = models.CharField(max_length=13, db_column='EAN_Scanner', blank=True) # Field name made lowercase.
    peso_tramo1 = models.IntegerField(null=True, db_column='Peso_Tramo1', blank=True) # Field name made lowercase.
    precio_tramo1 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Tramo1', blank=True) # Field name made lowercase.
    peso_tramo2 = models.IntegerField(null=True, db_column='Peso_Tramo2', blank=True) # Field name made lowercase.
    precio_tramo2 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Tramo2', blank=True) # Field name made lowercase.
    peso_tramo3 = models.IntegerField(null=True, db_column='Peso_Tramo3', blank=True) # Field name made lowercase.
    precio_tramo3 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Tramo3', blank=True) # Field name made lowercase.
    oper_temp = models.IntegerField(null=True, db_column='Oper_temp', blank=True) # Field name made lowercase.
    num_oper_ult = models.IntegerField(null=True, db_column='Num_Oper_Ult', blank=True) # Field name made lowercase.
    peso_ult = models.FloatField(null=True, db_column='Peso_Ult', blank=True) # Field name made lowercase.
    importe_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Ult', blank=True) # Field name made lowercase.
    carne = models.IntegerField(null=True, db_column='Carne', blank=True) # Field name made lowercase.
    cod_vacuno = models.SmallIntegerField(null=True, db_column='Cod_Vacuno', blank=True) # Field name made lowercase.
    fecha_envasado = models.IntegerField(null=True, db_column='Fecha_Envasado', blank=True) # Field name made lowercase.
    tara_porcentual = models.SmallIntegerField(null=True, db_column='Tara_Porcentual', blank=True) # Field name made lowercase.
    formato_ean128 = models.SmallIntegerField(null=True, db_column='Formato_EAN128', blank=True) # Field name made lowercase.
    receta = models.SmallIntegerField(null=True, db_column='Receta', blank=True) # Field name made lowercase.
    logo = models.SmallIntegerField(null=True, db_column='Logo', blank=True) # Field name made lowercase.
    nombre3 = models.CharField(max_length=24, db_column='Nombre3', blank=True) # Field name made lowercase.
    texto4_lp2500 = models.CharField(max_length=255, db_column='Texto4_LP2500', blank=True) # Field name made lowercase.
    texto4_2_lp2500 = models.CharField(max_length=255, db_column='Texto4_2_LP2500', blank=True) # Field name made lowercase.
    precio_libre = models.SmallIntegerField(null=True, db_column='Precio_Libre', blank=True) # Field name made lowercase.
    clase = models.SmallIntegerField(null=True, db_column='Clase', blank=True) # Field name made lowercase.
    preciotarifa1 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='PrecioTarifa1', blank=True) # Field name made lowercase.
    preciotarifa2 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='PrecioTarifa2', blank=True) # Field name made lowercase.
    preciotarifa3 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='PrecioTarifa3', blank=True) # Field name made lowercase.
    ndespiece = models.SmallIntegerField(null=True, db_column='Ndespiece', blank=True) # Field name made lowercase.
    codigocompra = models.IntegerField(null=True, db_column='CodigoCompra', blank=True) # Field name made lowercase.
    textog = models.TextField(db_column='TextoG', blank=True) # Field name made lowercase. This field type is a guess.
    tipooferta = models.SmallIntegerField(null=True, db_column='TipoOferta', blank=True) # Field name made lowercase.
    codigo_conad = models.IntegerField(null=True, db_column='Codigo_Conad', blank=True) # Field name made lowercase.
    ean13_14 = models.CharField(max_length=14, db_column='EAN13_14', blank=True) # Field name made lowercase.
    tipoean = models.SmallIntegerField(null=True, db_column='TipoEan', blank=True) # Field name made lowercase.
    pesopieza = models.FloatField(null=True, db_column='PesoPieza', blank=True) # Field name made lowercase.
    conservacion = models.SmallIntegerField(null=True, db_column='Conservacion', blank=True) # Field name made lowercase.
    numerounidades = models.SmallIntegerField(null=True, db_column='NumeroUnidades', blank=True) # Field name made lowercase.
    nivel1 = models.SmallIntegerField(null=True, db_column='Nivel1', blank=True) # Field name made lowercase.
    nivel2 = models.SmallIntegerField(null=True, db_column='Nivel2', blank=True) # Field name made lowercase.
    nivel3 = models.SmallIntegerField(null=True, db_column='Nivel3', blank=True) # Field name made lowercase.
    umbraltrigger = models.FloatField(null=True, db_column='UmbralTrigger', blank=True) # Field name made lowercase.
    tiempoestablecimiento = models.SmallIntegerField(null=True, db_column='TiempoEstablecimiento', blank=True) # Field name made lowercase.
    tiempomedida = models.SmallIntegerField(null=True, db_column='TiempoMedida', blank=True) # Field name made lowercase.
    velocidadcintas = models.SmallIntegerField(null=True, db_column='VelocidadCintas', blank=True) # Field name made lowercase.
    centrado = models.SmallIntegerField(null=True, db_column='Centrado', blank=True) # Field name made lowercase.
    texto4_k = models.TextField(db_column='Texto4_K', blank=True) # Field name made lowercase. This field type is a guess.
    texto5_k = models.TextField(db_column='Texto5_K', blank=True) # Field name made lowercase. This field type is a guess.
    glaseado = models.FloatField(null=True, db_column='Glaseado', blank=True) # Field name made lowercase.
    pesominimo = models.IntegerField(null=True, db_column='PesoMinimo', blank=True) # Field name made lowercase.
    pesomaximo = models.IntegerField(null=True, db_column='PesoMaximo', blank=True) # Field name made lowercase.
    ean13_14_2 = models.CharField(max_length=14, db_column='EAN13_14_2', blank=True) # Field name made lowercase.
    tipoean_2 = models.SmallIntegerField(null=True, db_column='TipoEan_2', blank=True) # Field name made lowercase.
    formato_ean128_2 = models.SmallIntegerField(null=True, db_column='Formato_EAN128_2', blank=True) # Field name made lowercase.
    formato_ean_2 = models.SmallIntegerField(null=True, db_column='Formato_EAN_2', blank=True) # Field name made lowercase.
    tipocw = models.SmallIntegerField(null=True, db_column='TipoCW', blank=True) # Field name made lowercase.
    pesoobjetivo = models.FloatField(null=True, db_column='PesoObjetivo', blank=True) # Field name made lowercase.
    porcpesominimo = models.FloatField(null=True, db_column='PorcPesoMinimo', blank=True) # Field name made lowercase.
    porcpesomaximo = models.FloatField(null=True, db_column='PorcPesoMaximo', blank=True) # Field name made lowercase.
    nrechazosmin = models.IntegerField(null=True, db_column='NRechazosMin', blank=True) # Field name made lowercase.
    nrechazosmax = models.IntegerField(null=True, db_column='NRechazosMax', blank=True) # Field name made lowercase.
    nmedias = models.SmallIntegerField(null=True, db_column='NMedias', blank=True) # Field name made lowercase.
    modopesaje = models.SmallIntegerField(null=True, db_column='ModoPesaje', blank=True) # Field name made lowercase.
    pesoclasificacion1 = models.FloatField(null=True, db_column='PesoClasificacion1', blank=True) # Field name made lowercase.
    nrechazos1 = models.IntegerField(null=True, db_column='NRechazos1', blank=True) # Field name made lowercase.
    nsalida1 = models.SmallIntegerField(null=True, db_column='NSalida1', blank=True) # Field name made lowercase.
    pesoclasificacion2 = models.FloatField(null=True, db_column='PesoClasificacion2', blank=True) # Field name made lowercase.
    nrechazos2 = models.IntegerField(null=True, db_column='NRechazos2', blank=True) # Field name made lowercase.
    nsalida2 = models.SmallIntegerField(null=True, db_column='NSalida2', blank=True) # Field name made lowercase.
    pesoclasificacion3 = models.FloatField(null=True, db_column='PesoClasificacion3', blank=True) # Field name made lowercase.
    nrechazos3 = models.IntegerField(null=True, db_column='NRechazos3', blank=True) # Field name made lowercase.
    nsalida3 = models.SmallIntegerField(null=True, db_column='NSalida3', blank=True) # Field name made lowercase.
    pesoclasificacion4 = models.FloatField(null=True, db_column='PesoClasificacion4', blank=True) # Field name made lowercase.
    nrechazos4 = models.IntegerField(null=True, db_column='NRechazos4', blank=True) # Field name made lowercase.
    nsalida4 = models.SmallIntegerField(null=True, db_column='NSalida4', blank=True) # Field name made lowercase.
    pesoclasificacion5 = models.FloatField(null=True, db_column='PesoClasificacion5', blank=True) # Field name made lowercase.
    nrechazos5 = models.IntegerField(null=True, db_column='NRechazos5', blank=True) # Field name made lowercase.
    nsalida5 = models.SmallIntegerField(null=True, db_column='NSalida5', blank=True) # Field name made lowercase.
    pesoclasificacion6 = models.FloatField(null=True, db_column='PesoClasificacion6', blank=True) # Field name made lowercase.
    nrechazos6 = models.IntegerField(null=True, db_column='NRechazos6', blank=True) # Field name made lowercase.
    nsalida6 = models.SmallIntegerField(null=True, db_column='NSalida6', blank=True) # Field name made lowercase.
    pesoclasificacion7 = models.FloatField(null=True, db_column='PesoClasificacion7', blank=True) # Field name made lowercase.
    nrechazos7 = models.IntegerField(null=True, db_column='NRechazos7', blank=True) # Field name made lowercase.
    nsalida7 = models.SmallIntegerField(null=True, db_column='NSalida7', blank=True) # Field name made lowercase.
    pesoclasificacion8 = models.FloatField(null=True, db_column='PesoClasificacion8', blank=True) # Field name made lowercase.
    nrechazos8 = models.IntegerField(null=True, db_column='NRechazos8', blank=True) # Field name made lowercase.
    nsalida8 = models.SmallIntegerField(null=True, db_column='NSalida8', blank=True) # Field name made lowercase.
    simbolopeso = models.SmallIntegerField(null=True, db_column='SimboloPeso', blank=True) # Field name made lowercase.
    simboloprecio = models.SmallIntegerField(null=True, db_column='SimboloPrecio', blank=True) # Field name made lowercase.
    simboloimporte = models.SmallIntegerField(null=True, db_column='SimboloImporte', blank=True) # Field name made lowercase.
    logo1 = models.SmallIntegerField(null=True, db_column='Logo1', blank=True) # Field name made lowercase.
    logo2 = models.SmallIntegerField(null=True, db_column='Logo2', blank=True) # Field name made lowercase.
    logo3 = models.SmallIntegerField(null=True, db_column='Logo3', blank=True) # Field name made lowercase.
    logo4 = models.SmallIntegerField(null=True, db_column='Logo4', blank=True) # Field name made lowercase.
    logo5 = models.SmallIntegerField(null=True, db_column='Logo5', blank=True) # Field name made lowercase.
    numerolote = models.CharField(max_length=24, db_column='NumeroLote', blank=True) # Field name made lowercase.
    formatofechaenvasado = models.SmallIntegerField(null=True, db_column='FormatoFechaEnvasado', blank=True) # Field name made lowercase.
    formatofechacaducidad = models.SmallIntegerField(null=True, db_column='FormatoFechaCaducidad', blank=True) # Field name made lowercase.
    formatofechaextra = models.SmallIntegerField(null=True, db_column='FormatoFechaExtra', blank=True) # Field name made lowercase.
    formatofechacongelacion = models.SmallIntegerField(null=True, db_column='FormatoFechaCongelacion', blank=True) # Field name made lowercase.
    totalpeso = models.FloatField(null=True, db_column='TotalPeso', blank=True) # Field name made lowercase.
    margenpeso = models.FloatField(null=True, db_column='MargenPeso', blank=True) # Field name made lowercase.
    tiempodecoccion = models.SmallIntegerField(null=True, db_column='TiempoDeCoccion', blank=True) # Field name made lowercase.
    tiempofijo = models.SmallIntegerField(null=True, db_column='TiempoFijo', blank=True) # Field name made lowercase.
    controlstock = models.SmallIntegerField(null=True, db_column='ControlStock', blank=True) # Field name made lowercase.
    etiquetasstock = models.IntegerField(null=True, db_column='EtiquetasStock', blank=True) # Field name made lowercase.
    pesostock = models.FloatField(null=True, db_column='PesoStock', blank=True) # Field name made lowercase.
    ftoconsumo = models.SmallIntegerField(null=True, db_column='FtoConsumo', blank=True) # Field name made lowercase.
    clasificacion1 = models.FloatField(null=True, db_column='Clasificacion1', blank=True) # Field name made lowercase.
    salida1 = models.SmallIntegerField(null=True, db_column='Salida1', blank=True) # Field name made lowercase.
    clasificacion2 = models.FloatField(null=True, db_column='Clasificacion2', blank=True) # Field name made lowercase.
    salida2 = models.SmallIntegerField(null=True, db_column='Salida2', blank=True) # Field name made lowercase.
    clasificacion3 = models.FloatField(null=True, db_column='Clasificacion3', blank=True) # Field name made lowercase.
    salida3 = models.SmallIntegerField(null=True, db_column='Salida3', blank=True) # Field name made lowercase.
    clasificacion4 = models.FloatField(null=True, db_column='Clasificacion4', blank=True) # Field name made lowercase.
    salida4 = models.SmallIntegerField(null=True, db_column='Salida4', blank=True) # Field name made lowercase.
    codingredientes = models.IntegerField(null=True, db_column='CodIngredientes', blank=True) # Field name made lowercase.
    codtara = models.IntegerField(null=True, db_column='CodTara', blank=True) # Field name made lowercase.
    modoequipo = models.SmallIntegerField(null=True, db_column='ModoEquipo', blank=True) # Field name made lowercase.
    formatoetiquetae1 = models.SmallIntegerField(null=True, db_column='FormatoEtiquetaE1', blank=True) # Field name made lowercase.
    formatoetiquetae2 = models.SmallIntegerField(null=True, db_column='FormatoEtiquetaE2', blank=True) # Field name made lowercase.
    formatototales = models.SmallIntegerField(null=True, db_column='FormatoTotales', blank=True) # Field name made lowercase.
    formatonivel1 = models.SmallIntegerField(null=True, db_column='FormatoNivel1', blank=True) # Field name made lowercase.
    formatonivel2 = models.SmallIntegerField(null=True, db_column='FormatoNivel2', blank=True) # Field name made lowercase.
    formatonivel3 = models.SmallIntegerField(null=True, db_column='FormatoNivel3', blank=True) # Field name made lowercase.
    diasemanaoferta = models.SmallIntegerField(null=True, db_column='DiaSemanaOferta', blank=True) # Field name made lowercase.
    longitud = models.IntegerField(null=True, db_column='Longitud', blank=True) # Field name made lowercase.
    centradoe1 = models.SmallIntegerField(null=True, db_column='CentradoE1', blank=True) # Field name made lowercase.
    centradoe2 = models.SmallIntegerField(null=True, db_column='CentradoE2', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Articulo'

class ArticuloBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    direccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Direccion', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, primary_key=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    cod_rapido = models.SmallIntegerField(null=True, db_column='Cod_Rapido', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Articulo_Balanza'

class ArticuloTienda(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, primary_key=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    cod_familia = models.SmallIntegerField(null=True, db_column='Cod_Familia', blank=True) # Field name made lowercase.
    cod_subfamilia = models.SmallIntegerField(null=True, db_column='Cod_Subfamilia', blank=True) # Field name made lowercase.
    cod_rapido_def = models.BooleanField(db_column='Cod_Rapido_Def') # Field name made lowercase.
    cod_rapido = models.SmallIntegerField(null=True, db_column='Cod_Rapido', blank=True) # Field name made lowercase.
    precio_def = models.BooleanField(db_column='Precio_Def') # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    caducidad_def = models.BooleanField(db_column='Caducidad_Def') # Field name made lowercase.
    caducidad = models.IntegerField(null=True, db_column='Caducidad', blank=True) # Field name made lowercase.
    iva_def = models.BooleanField(db_column='IVA_Def') # Field name made lowercase.
    iva = models.SmallIntegerField(null=True, db_column='IVA', blank=True) # Field name made lowercase.
    departamento_def = models.BooleanField(db_column='Departamento_Def') # Field name made lowercase.
    departamento = models.IntegerField(null=True, db_column='Departamento', blank=True) # Field name made lowercase.
    seccion_def = models.BooleanField(db_column='Seccion_Def') # Field name made lowercase.
    seccion = models.SmallIntegerField(null=True, db_column='Seccion', blank=True) # Field name made lowercase.
    tara_def = models.BooleanField(db_column='Tara_Def') # Field name made lowercase.
    tara = models.IntegerField(null=True, db_column='Tara', blank=True) # Field name made lowercase.
    formato_def = models.BooleanField(db_column='Formato_Def') # Field name made lowercase.
    formato = models.SmallIntegerField(null=True, db_column='Formato', blank=True) # Field name made lowercase.
    precio_oferta_def = models.BooleanField(db_column='Precio_Oferta_Def') # Field name made lowercase.
    precio_oferta = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Oferta', blank=True) # Field name made lowercase.
    fecha_extra_def = models.BooleanField(db_column='Fecha_Extra_Def') # Field name made lowercase.
    fecha_extra = models.IntegerField(null=True, db_column='Fecha_Extra', blank=True) # Field name made lowercase.
    formato_ean_def = models.BooleanField(db_column='Formato_EAN_Def') # Field name made lowercase.
    formato_ean = models.SmallIntegerField(null=True, db_column='Formato_EAN', blank=True) # Field name made lowercase.
    rentabilidad_def = models.BooleanField(db_column='Rentabilidad_Def') # Field name made lowercase.
    rentabilidad = models.SmallIntegerField(null=True, db_column='Rentabilidad', blank=True) # Field name made lowercase.
    promocion_def = models.BooleanField(db_column='Promocion_Def') # Field name made lowercase.
    promocion = models.BooleanField(db_column='Promocion') # Field name made lowercase.
    precio_promocion = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Promocion', blank=True) # Field name made lowercase.
    com_promocion = models.DateTimeField(null=True, db_column='Com_Promocion', blank=True) # Field name made lowercase.
    fin_promocion = models.DateTimeField(null=True, db_column='Fin_Promocion', blank=True) # Field name made lowercase.
    stock_def = models.BooleanField(db_column='Stock_Def') # Field name made lowercase.
    stock = models.BooleanField(db_column='Stock') # Field name made lowercase.
    existencias = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Existencias', blank=True) # Field name made lowercase.
    perdidas = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Perdidas', blank=True) # Field name made lowercase.
    stock_min = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Stock_Min', blank=True) # Field name made lowercase.
    stock_max = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Stock_Max', blank=True) # Field name made lowercase.
    aviso = models.BooleanField(db_column='Aviso') # Field name made lowercase.
    num_oper = models.IntegerField(null=True, db_column='Num_Oper', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    peso = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Peso', blank=True) # Field name made lowercase.
    num_oper_ult = models.IntegerField(null=True, db_column='Num_Oper_Ult', blank=True) # Field name made lowercase.
    importe_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Ult', blank=True) # Field name made lowercase.
    peso_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Peso_Ult', blank=True) # Field name made lowercase.
    modificado = models.BooleanField(db_column='Modificado') # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado') # Field name made lowercase.
    precio_anterior = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Anterior', blank=True) # Field name made lowercase.
    promocion_actualizada = models.BooleanField(db_column='Promocion_Actualizada') # Field name made lowercase.
    precio_costo = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Costo', blank=True) # Field name made lowercase.
    cantidad_comprada = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Cantidad_Comprada', blank=True) # Field name made lowercase.
    precio_ultima_compra = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Ultima_Compra', blank=True) # Field name made lowercase.
    precio_medio_venta = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Medio_Venta', blank=True) # Field name made lowercase.
    cantidad_vendida = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Cantidad_Vendida', blank=True) # Field name made lowercase.
    precio_ultima_venta = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Ultima_Venta', blank=True) # Field name made lowercase.
    margen_objetivo = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Margen_Objetivo', blank=True) # Field name made lowercase.
    ean_scanner_def = models.BooleanField(db_column='EAN_Scanner_Def') # Field name made lowercase.
    ean_scanner = models.CharField(max_length=13, db_column='EAN_Scanner', blank=True) # Field name made lowercase.
    peso_tramo1 = models.IntegerField(null=True, db_column='Peso_Tramo1', blank=True) # Field name made lowercase.
    precio_tramo1 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Tramo1', blank=True) # Field name made lowercase.
    peso_tramo2 = models.IntegerField(null=True, db_column='Peso_Tramo2', blank=True) # Field name made lowercase.
    precio_tramo2 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Tramo2', blank=True) # Field name made lowercase.
    peso_tramo3 = models.IntegerField(null=True, db_column='Peso_Tramo3', blank=True) # Field name made lowercase.
    precio_tramo3 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Tramo3', blank=True) # Field name made lowercase.
    pesopreciotramo1_def = models.BooleanField(db_column='PesoPrecioTramo1_Def') # Field name made lowercase.
    pesopreciotramo2_def = models.BooleanField(db_column='PesoPrecioTramo2_Def') # Field name made lowercase.
    pesopreciotramo3_def = models.BooleanField(db_column='PesoPrecioTramo3_Def') # Field name made lowercase.
    oper_temp = models.IntegerField(null=True, db_column='Oper_temp', blank=True) # Field name made lowercase.
    pmedio_temp = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='PMedio_temp', blank=True) # Field name made lowercase.
    peso_temp = models.FloatField(null=True, db_column='Peso_temp', blank=True) # Field name made lowercase.
    peso_ult_temp = models.FloatField(null=True, db_column='Peso_Ult_temp', blank=True) # Field name made lowercase.
    modificado_precio = models.BooleanField(db_column='Modificado_Precio') # Field name made lowercase.
    modificado_tecla = models.BooleanField(db_column='Modificado_Tecla') # Field name made lowercase.
    carne = models.SmallIntegerField(null=True, db_column='Carne', blank=True) # Field name made lowercase.
    cod_vacuno = models.SmallIntegerField(null=True, db_column='Cod_Vacuno', blank=True) # Field name made lowercase.
    carne_def = models.SmallIntegerField(null=True, db_column='Carne_Def', blank=True) # Field name made lowercase.
    cod_vacuno_def = models.SmallIntegerField(null=True, db_column='Cod_Vacuno_Def', blank=True) # Field name made lowercase.
    fecha_envasado_def = models.SmallIntegerField(null=True, db_column='Fecha_Envasado_Def', blank=True) # Field name made lowercase.
    fecha_envasado = models.IntegerField(null=True, db_column='Fecha_Envasado', blank=True) # Field name made lowercase.
    tara_porcentual_def = models.SmallIntegerField(null=True, db_column='Tara_Porcentual_Def', blank=True) # Field name made lowercase.
    tara_porcentual = models.SmallIntegerField(null=True, db_column='Tara_Porcentual', blank=True) # Field name made lowercase.
    formato_ean128_def = models.SmallIntegerField(null=True, db_column='Formato_EAN128_Def', blank=True) # Field name made lowercase.
    formato_ean128 = models.SmallIntegerField(null=True, db_column='Formato_EAN128', blank=True) # Field name made lowercase.
    receta_def = models.SmallIntegerField(null=True, db_column='Receta_Def', blank=True) # Field name made lowercase.
    receta = models.SmallIntegerField(null=True, db_column='Receta', blank=True) # Field name made lowercase.
    logo_def = models.SmallIntegerField(null=True, db_column='Logo_Def', blank=True) # Field name made lowercase.
    logo = models.SmallIntegerField(null=True, db_column='Logo', blank=True) # Field name made lowercase.
    modificado_textos = models.SmallIntegerField(null=True, db_column='Modificado_Textos', blank=True) # Field name made lowercase.
    modificado_tramos = models.SmallIntegerField(null=True, db_column='Modificado_Tramos', blank=True) # Field name made lowercase.
    precio_libre_def = models.SmallIntegerField(null=True, db_column='Precio_Libre_Def', blank=True) # Field name made lowercase.
    precio_libre = models.SmallIntegerField(null=True, db_column='Precio_Libre', blank=True) # Field name made lowercase.
    clase_def = models.SmallIntegerField(null=True, db_column='Clase_Def', blank=True) # Field name made lowercase.
    clase = models.SmallIntegerField(null=True, db_column='Clase', blank=True) # Field name made lowercase.
    preciotarifa1_def = models.BooleanField(db_column='PrecioTarifa1_Def') # Field name made lowercase.
    preciotarifa1 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='PrecioTarifa1', blank=True) # Field name made lowercase.
    preciotarifa2_def = models.BooleanField(db_column='PrecioTarifa2_Def') # Field name made lowercase.
    preciotarifa2 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='PrecioTarifa2', blank=True) # Field name made lowercase.
    preciotarifa3_def = models.BooleanField(db_column='PrecioTarifa3_Def') # Field name made lowercase.
    preciotarifa3 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='PrecioTarifa3', blank=True) # Field name made lowercase.
    ndespiece_def = models.BooleanField(db_column='NDespiece_Def') # Field name made lowercase.
    ndespiece = models.SmallIntegerField(null=True, db_column='Ndespiece', blank=True) # Field name made lowercase.
    tipooferta_def = models.SmallIntegerField(null=True, db_column='TipoOferta_Def', blank=True) # Field name made lowercase.
    tipooferta = models.SmallIntegerField(null=True, db_column='TipoOferta', blank=True) # Field name made lowercase.
    numerounidades_def = models.SmallIntegerField(null=True, db_column='NumeroUnidades_Def', blank=True) # Field name made lowercase.
    numerounidades = models.SmallIntegerField(null=True, db_column='NumeroUnidades', blank=True) # Field name made lowercase.
    ean13_14_def = models.IntegerField(null=True, db_column='EAN13_14_Def', blank=True) # Field name made lowercase.
    ean13_14 = models.CharField(max_length=14, db_column='EAN13_14', blank=True) # Field name made lowercase.
    tipoean_def = models.IntegerField(null=True, db_column='TipoEan_Def', blank=True) # Field name made lowercase.
    tipoean = models.SmallIntegerField(null=True, db_column='TipoEan', blank=True) # Field name made lowercase.
    modificado_eans = models.SmallIntegerField(null=True, db_column='Modificado_EANs', blank=True) # Field name made lowercase.
    pesopieza_def = models.IntegerField(null=True, db_column='PesoPieza_Def', blank=True) # Field name made lowercase.
    pesopieza = models.FloatField(null=True, db_column='PesoPieza', blank=True) # Field name made lowercase.
    conservacion_def = models.IntegerField(null=True, db_column='Conservacion_Def', blank=True) # Field name made lowercase.
    conservacion = models.SmallIntegerField(null=True, db_column='Conservacion', blank=True) # Field name made lowercase.
    nivel1_def = models.IntegerField(null=True, db_column='Nivel1_Def', blank=True) # Field name made lowercase.
    nivel1 = models.SmallIntegerField(null=True, db_column='Nivel1', blank=True) # Field name made lowercase.
    nivel2_def = models.IntegerField(null=True, db_column='Nivel2_Def', blank=True) # Field name made lowercase.
    nivel2 = models.SmallIntegerField(null=True, db_column='Nivel2', blank=True) # Field name made lowercase.
    nivel3_def = models.IntegerField(null=True, db_column='Nivel3_Def', blank=True) # Field name made lowercase.
    nivel3 = models.SmallIntegerField(null=True, db_column='Nivel3', blank=True) # Field name made lowercase.
    umbraltrigger_def = models.IntegerField(null=True, db_column='UmbralTrigger_Def', blank=True) # Field name made lowercase.
    umbraltrigger = models.FloatField(null=True, db_column='UmbralTrigger', blank=True) # Field name made lowercase.
    tiempoestablecimiento_def = models.IntegerField(null=True, db_column='TiempoEstablecimiento_Def', blank=True) # Field name made lowercase.
    tiempoestablecimiento = models.SmallIntegerField(null=True, db_column='TiempoEstablecimiento', blank=True) # Field name made lowercase.
    tiempomedida_def = models.IntegerField(null=True, db_column='TiempoMedida_Def', blank=True) # Field name made lowercase.
    tiempomedida = models.SmallIntegerField(null=True, db_column='TiempoMedida', blank=True) # Field name made lowercase.
    velocidadcintas_def = models.IntegerField(null=True, db_column='VelocidadCintas_Def', blank=True) # Field name made lowercase.
    velocidadcintas = models.SmallIntegerField(null=True, db_column='VelocidadCintas', blank=True) # Field name made lowercase.
    centrado_def = models.IntegerField(null=True, db_column='Centrado_Def', blank=True) # Field name made lowercase.
    centrado = models.SmallIntegerField(null=True, db_column='Centrado', blank=True) # Field name made lowercase.
    glaseado = models.FloatField(null=True, db_column='Glaseado', blank=True) # Field name made lowercase.
    glaseado_def = models.SmallIntegerField(null=True, db_column='Glaseado_Def', blank=True) # Field name made lowercase.
    pesominimo = models.FloatField(null=True, db_column='PesoMinimo', blank=True) # Field name made lowercase.
    pesominimo_def = models.SmallIntegerField(null=True, db_column='PesoMinimo_Def', blank=True) # Field name made lowercase.
    pesomaximo = models.FloatField(null=True, db_column='PesoMaximo', blank=True) # Field name made lowercase.
    pesomaximo_def = models.SmallIntegerField(null=True, db_column='PesoMaximo_Def', blank=True) # Field name made lowercase.
    ean13_14_2 = models.CharField(max_length=14, db_column='EAN13_14_2', blank=True) # Field name made lowercase.
    ean13_14_2_def = models.SmallIntegerField(null=True, db_column='EAN13_14_2_Def', blank=True) # Field name made lowercase.
    tipoean_2 = models.SmallIntegerField(null=True, db_column='TipoEan_2', blank=True) # Field name made lowercase.
    tipoean_2_def = models.SmallIntegerField(null=True, db_column='TipoEan_2_Def', blank=True) # Field name made lowercase.
    formato_ean128_2 = models.SmallIntegerField(null=True, db_column='Formato_EAN128_2', blank=True) # Field name made lowercase.
    formato_ean128_2_def = models.SmallIntegerField(null=True, db_column='Formato_EAN128_2_Def', blank=True) # Field name made lowercase.
    formato_ean_2 = models.SmallIntegerField(null=True, db_column='Formato_EAN_2', blank=True) # Field name made lowercase.
    formato_ean_2_def = models.SmallIntegerField(null=True, db_column='Formato_EAN_2_Def', blank=True) # Field name made lowercase.
    codingredientes = models.IntegerField(null=True, db_column='CodIngredientes', blank=True) # Field name made lowercase.
    codingredientes_def = models.SmallIntegerField(null=True, db_column='CodIngredientes_Def', blank=True) # Field name made lowercase.
    codtara = models.IntegerField(null=True, db_column='CodTara', blank=True) # Field name made lowercase.
    codtara_def = models.SmallIntegerField(null=True, db_column='CodTara_Def', blank=True) # Field name made lowercase.
    diasemanaoferta_def = models.SmallIntegerField(null=True, db_column='DiaSemanaOferta_Def', blank=True) # Field name made lowercase.
    diasemanaoferta = models.SmallIntegerField(null=True, db_column='DiaSemanaOferta', blank=True) # Field name made lowercase.
    texto1_mod = models.SmallIntegerField(null=True, db_column='Texto1_mod', blank=True) # Field name made lowercase.
    texto2_mod = models.SmallIntegerField(null=True, db_column='Texto2_mod', blank=True) # Field name made lowercase.
    texto3_mod = models.SmallIntegerField(null=True, db_column='Texto3_mod', blank=True) # Field name made lowercase.
    texto4_mod = models.SmallIntegerField(null=True, db_column='Texto4_mod', blank=True) # Field name made lowercase.
    texto5_mod = models.SmallIntegerField(null=True, db_column='Texto5_mod', blank=True) # Field name made lowercase.
    texto6_mod = models.SmallIntegerField(null=True, db_column='Texto6_mod', blank=True) # Field name made lowercase.
    texto7_mod = models.SmallIntegerField(null=True, db_column='Texto7_mod', blank=True) # Field name made lowercase.
    texto8_mod = models.SmallIntegerField(null=True, db_column='Texto8_mod', blank=True) # Field name made lowercase.
    texto9_mod = models.SmallIntegerField(null=True, db_column='Texto9_mod', blank=True) # Field name made lowercase.
    texto10_mod = models.SmallIntegerField(null=True, db_column='Texto10_mod', blank=True) # Field name made lowercase.
    textog_mod = models.SmallIntegerField(null=True, db_column='TextoG_mod', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Articulo_Tienda'

class ArticuloTiendaParte2(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, primary_key=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    cod_familia = models.SmallIntegerField(null=True, db_column='Cod_Familia', blank=True) # Field name made lowercase.
    cod_subfamilia = models.SmallIntegerField(null=True, db_column='Cod_Subfamilia', blank=True) # Field name made lowercase.
    tipocw_def = models.SmallIntegerField(null=True, db_column='TipoCW_Def', blank=True) # Field name made lowercase.
    tipocw = models.SmallIntegerField(null=True, db_column='TipoCW', blank=True) # Field name made lowercase.
    pesoobjetivo = models.FloatField(null=True, db_column='PesoObjetivo', blank=True) # Field name made lowercase.
    pesoobjetivo_def = models.SmallIntegerField(null=True, db_column='PesoObjetivo_Def', blank=True) # Field name made lowercase.
    porcpesominimo = models.FloatField(null=True, db_column='PorcPesoMinimo', blank=True) # Field name made lowercase.
    porcpesominimo_def = models.SmallIntegerField(null=True, db_column='PorcPesoMinimo_Def', blank=True) # Field name made lowercase.
    porcpesomaximo = models.FloatField(null=True, db_column='PorcPesoMaximo', blank=True) # Field name made lowercase.
    porcpesomaximo_def = models.SmallIntegerField(null=True, db_column='PorcPesoMaximo_Def', blank=True) # Field name made lowercase.
    nrechazosmin = models.IntegerField(null=True, db_column='NRechazosMin', blank=True) # Field name made lowercase.
    nrechazosmin_def = models.SmallIntegerField(null=True, db_column='NRechazosMin_Def', blank=True) # Field name made lowercase.
    nrechazosmax = models.IntegerField(null=True, db_column='NRechazosMax', blank=True) # Field name made lowercase.
    nrechazosmax_def = models.SmallIntegerField(null=True, db_column='NRechazosMax_Def', blank=True) # Field name made lowercase.
    nmedias = models.SmallIntegerField(null=True, db_column='NMedias', blank=True) # Field name made lowercase.
    nmedias_def = models.SmallIntegerField(null=True, db_column='NMedias_Def', blank=True) # Field name made lowercase.
    modopesaje = models.SmallIntegerField(null=True, db_column='ModoPesaje', blank=True) # Field name made lowercase.
    modopesaje_def = models.SmallIntegerField(null=True, db_column='ModoPesaje_Def', blank=True) # Field name made lowercase.
    pesoclasificacion1 = models.FloatField(null=True, db_column='PesoClasificacion1', blank=True) # Field name made lowercase.
    pesoclasificacion1_def = models.IntegerField(null=True, db_column='PesoClasificacion1_Def', blank=True) # Field name made lowercase.
    nrechazos1 = models.IntegerField(null=True, db_column='NRechazos1', blank=True) # Field name made lowercase.
    nrechazos1_def = models.IntegerField(null=True, db_column='NRechazos1_Def', blank=True) # Field name made lowercase.
    nsalida1 = models.SmallIntegerField(null=True, db_column='NSalida1', blank=True) # Field name made lowercase.
    nsalida1_def = models.SmallIntegerField(null=True, db_column='NSalida1_Def', blank=True) # Field name made lowercase.
    pesoclasificacion2 = models.FloatField(null=True, db_column='PesoClasificacion2', blank=True) # Field name made lowercase.
    pesoclasificacion2_def = models.IntegerField(null=True, db_column='PesoClasificacion2_Def', blank=True) # Field name made lowercase.
    nrechazos2 = models.IntegerField(null=True, db_column='NRechazos2', blank=True) # Field name made lowercase.
    nrechazos2_def = models.IntegerField(null=True, db_column='NRechazos2_Def', blank=True) # Field name made lowercase.
    nsalida2 = models.SmallIntegerField(null=True, db_column='NSalida2', blank=True) # Field name made lowercase.
    nsalida2_def = models.SmallIntegerField(null=True, db_column='NSalida2_Def', blank=True) # Field name made lowercase.
    pesoclasificacion3 = models.FloatField(null=True, db_column='PesoClasificacion3', blank=True) # Field name made lowercase.
    pesoclasificacion3_def = models.SmallIntegerField(null=True, db_column='PesoClasificacion3_Def', blank=True) # Field name made lowercase.
    nrechazos3 = models.IntegerField(null=True, db_column='NRechazos3', blank=True) # Field name made lowercase.
    nrechazos3_def = models.SmallIntegerField(null=True, db_column='NRechazos3_Def', blank=True) # Field name made lowercase.
    nsalida3 = models.SmallIntegerField(null=True, db_column='NSalida3', blank=True) # Field name made lowercase.
    nsalida3_def = models.SmallIntegerField(null=True, db_column='NSalida3_Def', blank=True) # Field name made lowercase.
    pesoclasificacion4 = models.FloatField(null=True, db_column='PesoClasificacion4', blank=True) # Field name made lowercase.
    pesoclasificacion4_def = models.SmallIntegerField(null=True, db_column='PesoClasificacion4_Def', blank=True) # Field name made lowercase.
    nrechazos4 = models.IntegerField(null=True, db_column='NRechazos4', blank=True) # Field name made lowercase.
    nrechazos4_def = models.SmallIntegerField(null=True, db_column='NRechazos4_Def', blank=True) # Field name made lowercase.
    nsalida4 = models.SmallIntegerField(null=True, db_column='NSalida4', blank=True) # Field name made lowercase.
    nsalida4_def = models.SmallIntegerField(null=True, db_column='NSalida4_Def', blank=True) # Field name made lowercase.
    pesoclasificacion5 = models.FloatField(null=True, db_column='PesoClasificacion5', blank=True) # Field name made lowercase.
    pesoclasificacion5_def = models.SmallIntegerField(null=True, db_column='PesoClasificacion5_Def', blank=True) # Field name made lowercase.
    nrechazos5 = models.IntegerField(null=True, db_column='NRechazos5', blank=True) # Field name made lowercase.
    nrechazos5_def = models.SmallIntegerField(null=True, db_column='NRechazos5_Def', blank=True) # Field name made lowercase.
    nsalida5 = models.SmallIntegerField(null=True, db_column='NSalida5', blank=True) # Field name made lowercase.
    nsalida5_def = models.SmallIntegerField(null=True, db_column='NSalida5_Def', blank=True) # Field name made lowercase.
    pesoclasificacion6 = models.FloatField(null=True, db_column='PesoClasificacion6', blank=True) # Field name made lowercase.
    pesoclasificacion6_def = models.SmallIntegerField(null=True, db_column='PesoClasificacion6_Def', blank=True) # Field name made lowercase.
    nrechazos6 = models.IntegerField(null=True, db_column='NRechazos6', blank=True) # Field name made lowercase.
    nrechazos6_def = models.SmallIntegerField(null=True, db_column='NRechazos6_Def', blank=True) # Field name made lowercase.
    nsalida6 = models.SmallIntegerField(null=True, db_column='NSalida6', blank=True) # Field name made lowercase.
    nsalida6_def = models.SmallIntegerField(null=True, db_column='NSalida6_Def', blank=True) # Field name made lowercase.
    pesoclasificacion7 = models.FloatField(null=True, db_column='PesoClasificacion7', blank=True) # Field name made lowercase.
    pesoclasificacion7_def = models.SmallIntegerField(null=True, db_column='PesoClasificacion7_Def', blank=True) # Field name made lowercase.
    nrechazos7 = models.IntegerField(null=True, db_column='NRechazos7', blank=True) # Field name made lowercase.
    nrechazos7_def = models.SmallIntegerField(null=True, db_column='NRechazos7_Def', blank=True) # Field name made lowercase.
    nsalida7 = models.SmallIntegerField(null=True, db_column='NSalida7', blank=True) # Field name made lowercase.
    nsalida7_def = models.SmallIntegerField(null=True, db_column='NSalida7_Def', blank=True) # Field name made lowercase.
    pesoclasificacion8 = models.FloatField(null=True, db_column='PesoClasificacion8', blank=True) # Field name made lowercase.
    pesoclasificacion8_def = models.SmallIntegerField(null=True, db_column='PesoClasificacion8_Def', blank=True) # Field name made lowercase.
    nrechazos8 = models.IntegerField(null=True, db_column='NRechazos8', blank=True) # Field name made lowercase.
    nrechazos8_def = models.SmallIntegerField(null=True, db_column='NRechazos8_Def', blank=True) # Field name made lowercase.
    nsalida8 = models.SmallIntegerField(null=True, db_column='NSalida8', blank=True) # Field name made lowercase.
    nsalida8_def = models.SmallIntegerField(null=True, db_column='NSalida8_Def', blank=True) # Field name made lowercase.
    simbolopeso = models.SmallIntegerField(null=True, db_column='SimboloPeso', blank=True) # Field name made lowercase.
    simbolopeso_def = models.SmallIntegerField(null=True, db_column='SimboloPeso_Def', blank=True) # Field name made lowercase.
    simboloprecio = models.SmallIntegerField(null=True, db_column='SimboloPrecio', blank=True) # Field name made lowercase.
    simboloprecio_def = models.SmallIntegerField(null=True, db_column='SimboloPrecio_Def', blank=True) # Field name made lowercase.
    simboloimporte = models.SmallIntegerField(null=True, db_column='SimboloImporte', blank=True) # Field name made lowercase.
    simboloimporte_def = models.SmallIntegerField(null=True, db_column='SimboloImporte_Def', blank=True) # Field name made lowercase.
    logo1_def = models.SmallIntegerField(null=True, db_column='Logo1_Def', blank=True) # Field name made lowercase.
    logo1 = models.SmallIntegerField(null=True, db_column='Logo1', blank=True) # Field name made lowercase.
    logo2_def = models.SmallIntegerField(null=True, db_column='Logo2_Def', blank=True) # Field name made lowercase.
    logo2 = models.SmallIntegerField(null=True, db_column='Logo2', blank=True) # Field name made lowercase.
    logo3_def = models.SmallIntegerField(null=True, db_column='Logo3_Def', blank=True) # Field name made lowercase.
    logo3 = models.SmallIntegerField(null=True, db_column='Logo3', blank=True) # Field name made lowercase.
    logo4_def = models.SmallIntegerField(null=True, db_column='Logo4_Def', blank=True) # Field name made lowercase.
    logo4 = models.SmallIntegerField(null=True, db_column='Logo4', blank=True) # Field name made lowercase.
    logo5_def = models.SmallIntegerField(null=True, db_column='Logo5_Def', blank=True) # Field name made lowercase.
    logo5 = models.SmallIntegerField(null=True, db_column='Logo5', blank=True) # Field name made lowercase.
    numerolote_def = models.SmallIntegerField(null=True, db_column='NumeroLote_Def', blank=True) # Field name made lowercase.
    numerolote = models.CharField(max_length=24, db_column='NumeroLote', blank=True) # Field name made lowercase.
    formatofechaenvasado_def = models.SmallIntegerField(null=True, db_column='FormatoFechaEnvasado_Def', blank=True) # Field name made lowercase.
    formatofechaenvasado = models.SmallIntegerField(null=True, db_column='FormatoFechaEnvasado', blank=True) # Field name made lowercase.
    formatofechacaducidad_def = models.SmallIntegerField(null=True, db_column='FormatoFechaCaducidad_Def', blank=True) # Field name made lowercase.
    formatofechacaducidad = models.SmallIntegerField(null=True, db_column='FormatoFechaCaducidad', blank=True) # Field name made lowercase.
    formatofechaextra_def = models.SmallIntegerField(null=True, db_column='FormatoFechaExtra_Def', blank=True) # Field name made lowercase.
    formatofechaextra = models.SmallIntegerField(null=True, db_column='FormatoFechaExtra', blank=True) # Field name made lowercase.
    formatofechacongelacion_def = models.SmallIntegerField(null=True, db_column='FormatoFechaCongelacion_Def', blank=True) # Field name made lowercase.
    formatofechacongelacion = models.SmallIntegerField(null=True, db_column='FormatoFechaCongelacion', blank=True) # Field name made lowercase.
    totalpeso_def = models.SmallIntegerField(null=True, db_column='TotalPeso_Def', blank=True) # Field name made lowercase.
    totalpeso = models.FloatField(null=True, db_column='TotalPeso', blank=True) # Field name made lowercase.
    margenpeso_def = models.SmallIntegerField(null=True, db_column='MargenPeso_Def', blank=True) # Field name made lowercase.
    margenpeso = models.FloatField(null=True, db_column='MargenPeso', blank=True) # Field name made lowercase.
    tiempodecoccion_def = models.SmallIntegerField(null=True, db_column='TiempoDeCoccion_Def', blank=True) # Field name made lowercase.
    tiempodecoccion = models.SmallIntegerField(null=True, db_column='TiempoDeCoccion', blank=True) # Field name made lowercase.
    tiempofijo_def = models.SmallIntegerField(null=True, db_column='TiempoFijo_Def', blank=True) # Field name made lowercase.
    tiempofijo = models.SmallIntegerField(null=True, db_column='TiempoFijo', blank=True) # Field name made lowercase.
    controlstock_def = models.SmallIntegerField(null=True, db_column='ControlStock_Def', blank=True) # Field name made lowercase.
    controlstock = models.SmallIntegerField(null=True, db_column='ControlStock', blank=True) # Field name made lowercase.
    etiquetasstock_def = models.SmallIntegerField(null=True, db_column='EtiquetasStock_Def', blank=True) # Field name made lowercase.
    etiquetasstock = models.IntegerField(null=True, db_column='EtiquetasStock', blank=True) # Field name made lowercase.
    pesostock_def = models.SmallIntegerField(null=True, db_column='PesoStock_Def', blank=True) # Field name made lowercase.
    pesostock = models.FloatField(null=True, db_column='PesoStock', blank=True) # Field name made lowercase.
    ftoconsumo_def = models.SmallIntegerField(null=True, db_column='FtoConsumo_Def', blank=True) # Field name made lowercase.
    ftoconsumo = models.SmallIntegerField(null=True, db_column='FtoConsumo', blank=True) # Field name made lowercase.
    clasificacion1_def = models.SmallIntegerField(null=True, db_column='Clasificacion1_Def', blank=True) # Field name made lowercase.
    clasificacion1 = models.FloatField(null=True, db_column='Clasificacion1', blank=True) # Field name made lowercase.
    salida1_def = models.SmallIntegerField(null=True, db_column='Salida1_Def', blank=True) # Field name made lowercase.
    salida1 = models.SmallIntegerField(null=True, db_column='Salida1', blank=True) # Field name made lowercase.
    clasificacion2_def = models.SmallIntegerField(null=True, db_column='Clasificacion2_Def', blank=True) # Field name made lowercase.
    clasificacion2 = models.FloatField(null=True, db_column='Clasificacion2', blank=True) # Field name made lowercase.
    salida2_def = models.SmallIntegerField(null=True, db_column='Salida2_Def', blank=True) # Field name made lowercase.
    salida2 = models.SmallIntegerField(null=True, db_column='Salida2', blank=True) # Field name made lowercase.
    clasificacion3_def = models.SmallIntegerField(null=True, db_column='Clasificacion3_Def', blank=True) # Field name made lowercase.
    clasificacion3 = models.FloatField(null=True, db_column='Clasificacion3', blank=True) # Field name made lowercase.
    salida3_def = models.SmallIntegerField(null=True, db_column='Salida3_Def', blank=True) # Field name made lowercase.
    salida3 = models.SmallIntegerField(null=True, db_column='Salida3', blank=True) # Field name made lowercase.
    clasificacion4_def = models.SmallIntegerField(null=True, db_column='Clasificacion4_Def', blank=True) # Field name made lowercase.
    clasificacion4 = models.FloatField(null=True, db_column='Clasificacion4', blank=True) # Field name made lowercase.
    salida4_def = models.SmallIntegerField(null=True, db_column='Salida4_Def', blank=True) # Field name made lowercase.
    salida4 = models.SmallIntegerField(null=True, db_column='Salida4', blank=True) # Field name made lowercase.
    modoequipo_def = models.SmallIntegerField(null=True, db_column='ModoEquipo_Def', blank=True) # Field name made lowercase.
    modoequipo = models.SmallIntegerField(null=True, db_column='ModoEquipo', blank=True) # Field name made lowercase.
    formatoetiquetae1_def = models.SmallIntegerField(null=True, db_column='FormatoEtiquetaE1_Def', blank=True) # Field name made lowercase.
    formatoetiquetae1 = models.SmallIntegerField(null=True, db_column='FormatoEtiquetaE1', blank=True) # Field name made lowercase.
    formatoetiquetae2_def = models.SmallIntegerField(null=True, db_column='FormatoEtiquetaE2_Def', blank=True) # Field name made lowercase.
    formatoetiquetae2 = models.SmallIntegerField(null=True, db_column='FormatoEtiquetaE2', blank=True) # Field name made lowercase.
    formatototales_def = models.SmallIntegerField(null=True, db_column='FormatoTotales_Def', blank=True) # Field name made lowercase.
    formatototales = models.SmallIntegerField(null=True, db_column='FormatoTotales', blank=True) # Field name made lowercase.
    formatonivel1_def = models.SmallIntegerField(null=True, db_column='FormatoNivel1_Def', blank=True) # Field name made lowercase.
    formatonivel1 = models.SmallIntegerField(null=True, db_column='FormatoNivel1', blank=True) # Field name made lowercase.
    formatonivel2_def = models.SmallIntegerField(null=True, db_column='FormatoNivel2_Def', blank=True) # Field name made lowercase.
    formatonivel2 = models.SmallIntegerField(null=True, db_column='FormatoNivel2', blank=True) # Field name made lowercase.
    formatonivel3_def = models.SmallIntegerField(null=True, db_column='FormatoNivel3_Def', blank=True) # Field name made lowercase.
    formatonivel3 = models.SmallIntegerField(null=True, db_column='FormatoNivel3', blank=True) # Field name made lowercase.
    longitud_def = models.SmallIntegerField(null=True, db_column='Longitud_Def', blank=True) # Field name made lowercase.
    longitud = models.IntegerField(null=True, db_column='Longitud', blank=True) # Field name made lowercase.
    centradoe1_def = models.SmallIntegerField(null=True, db_column='CentradoE1_Def', blank=True) # Field name made lowercase.
    centradoe1 = models.SmallIntegerField(null=True, db_column='CentradoE1', blank=True) # Field name made lowercase.
    centradoe2_def = models.SmallIntegerField(null=True, db_column='CentradoE2_Def', blank=True) # Field name made lowercase.
    centradoe2 = models.SmallIntegerField(null=True, db_column='CentradoE2', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Articulo_Tienda_Parte2'

class ArticulosPea(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    direccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Direccion', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, primary_key=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    tipo = models.SmallIntegerField(null=True, db_column='Tipo', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=24, db_column='Nombre', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    operaciones = models.IntegerField(null=True, db_column='Operaciones', blank=True) # Field name made lowercase.
    peso = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Peso', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    nombre2 = models.CharField(max_length=24, db_column='Nombre2', blank=True) # Field name made lowercase.
    cod_rapido = models.SmallIntegerField(null=True, db_column='Cod_Rapido', blank=True) # Field name made lowercase.
    precio_oferta = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Oferta', blank=True) # Field name made lowercase.
    precio_costo = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Costo', blank=True) # Field name made lowercase.
    caducidad = models.IntegerField(null=True, db_column='Caducidad', blank=True) # Field name made lowercase.
    fecha_extra = models.IntegerField(null=True, db_column='Fecha_Extra', blank=True) # Field name made lowercase.
    tara = models.IntegerField(null=True, db_column='Tara', blank=True) # Field name made lowercase.
    formato = models.SmallIntegerField(null=True, db_column='Formato', blank=True) # Field name made lowercase.
    formato_ean = models.SmallIntegerField(null=True, db_column='Formato_EAN', blank=True) # Field name made lowercase.
    departamento = models.IntegerField(null=True, db_column='Departamento', blank=True) # Field name made lowercase.
    seccion = models.SmallIntegerField(null=True, db_column='Seccion', blank=True) # Field name made lowercase.
    iva = models.SmallIntegerField(null=True, db_column='IVA', blank=True) # Field name made lowercase.
    rentabilidad = models.SmallIntegerField(null=True, db_column='Rentabilidad', blank=True) # Field name made lowercase.
    carne = models.SmallIntegerField(null=True, db_column='Carne', blank=True) # Field name made lowercase.
    cod_vacuno = models.SmallIntegerField(null=True, db_column='Cod_Vacuno', blank=True) # Field name made lowercase.
    modificado = models.BooleanField(db_column='Modificado') # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado') # Field name made lowercase.
    cod_familia = models.SmallIntegerField(null=True, db_column='Cod_Familia', blank=True) # Field name made lowercase.
    cod_subfamilia = models.SmallIntegerField(null=True, db_column='Cod_Subfamilia', blank=True) # Field name made lowercase.
    modificado_textos = models.SmallIntegerField(null=True, db_column='Modificado_Textos', blank=True) # Field name made lowercase.
    clase = models.SmallIntegerField(null=True, db_column='Clase', blank=True) # Field name made lowercase.
    ean128 = models.IntegerField(null=True, db_column='EAN128', blank=True) # Field name made lowercase.
    ean13_14 = models.CharField(max_length=14, db_column='EAN13_14', blank=True) # Field name made lowercase.
    tipoean = models.SmallIntegerField(null=True, db_column='TipoEan', blank=True) # Field name made lowercase.
    modificado_eans = models.SmallIntegerField(null=True, db_column='Modificado_EANs', blank=True) # Field name made lowercase.
    receta = models.SmallIntegerField(null=True, db_column='Receta', blank=True) # Field name made lowercase.
    pesopieza = models.FloatField(null=True, db_column='PesoPieza', blank=True) # Field name made lowercase.
    conservacion = models.SmallIntegerField(null=True, db_column='Conservacion', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Articulos_Pea'

class CabeceraTicketBorrado(models.Model):
    cod_ticket = models.IntegerField(null=True, primary_key=True, db_column='Cod_Ticket', blank=True) # Field name made lowercase.
    tienda = models.SmallIntegerField(null=True, db_column='Tienda', blank=True) # Field name made lowercase.
    seccion = models.SmallIntegerField(null=True, db_column='Seccion', blank=True) # Field name made lowercase.
    balanza = models.SmallIntegerField(null=True, db_column='Balanza', blank=True) # Field name made lowercase.
    num_ticket = models.SmallIntegerField(null=True, db_column='Num_Ticket', blank=True) # Field name made lowercase.
    clave = models.CharField(max_length=1, db_column='Clave', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    vendedor = models.IntegerField(null=True, db_column='Vendedor', blank=True) # Field name made lowercase.
    nombre_vendedor = models.CharField(max_length=50, db_column='Nombre_Vendedor', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    hora = models.CharField(max_length=5, db_column='Hora', blank=True) # Field name made lowercase.
    num_operaciones = models.IntegerField(null=True, db_column='Num_Operaciones', blank=True) # Field name made lowercase.
    importe_dto = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Dto', blank=True) # Field name made lowercase.
    parametro20 = models.SmallIntegerField(null=True, db_column='Parametro20', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Cabecera_Ticket_Borrado'

class CabeceraTicketVenta(models.Model):
    cod_ticket = models.IntegerField(null=True, primary_key=True, db_column='Cod_Ticket', blank=True) # Field name made lowercase.
    tienda = models.SmallIntegerField(null=True, db_column='Tienda', blank=True) # Field name made lowercase.
    numtramo = models.SmallIntegerField(null=True, db_column='NumTramo', blank=True) # Field name made lowercase.
    seccion = models.SmallIntegerField(null=True, db_column='Seccion', blank=True) # Field name made lowercase.
    balanza = models.SmallIntegerField(null=True, db_column='Balanza', blank=True) # Field name made lowercase.
    num_ticket = models.IntegerField(null=True, db_column='Num_Ticket', blank=True) # Field name made lowercase.
    clave = models.CharField(max_length=1, db_column='Clave', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    vendedor = models.IntegerField(null=True, db_column='Vendedor', blank=True) # Field name made lowercase.
    nombre_vendedor = models.CharField(max_length=50, db_column='Nombre_Vendedor', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    hora = models.CharField(max_length=5, db_column='Hora', blank=True) # Field name made lowercase.
    num_operaciones = models.IntegerField(null=True, db_column='Num_Operaciones', blank=True) # Field name made lowercase.
    importe_dto = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Dto', blank=True) # Field name made lowercase.
    parametro20 = models.SmallIntegerField(null=True, db_column='Parametro20', blank=True) # Field name made lowercase.
    exportado = models.SmallIntegerField(null=True, db_column='Exportado', blank=True) # Field name made lowercase.
    findiatratado = models.SmallIntegerField(null=True, db_column='FinDiaTratado', blank=True) # Field name made lowercase.
    nummensajetramo = models.SmallIntegerField(null=True, db_column='NumMensajeTramo', blank=True) # Field name made lowercase.
    numerocliente = models.IntegerField(null=True, db_column='NumeroCliente', blank=True) # Field name made lowercase.
    modopago1 = models.SmallIntegerField(null=True, db_column='ModoPago1', blank=True) # Field name made lowercase.
    importemodopago1 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='ImporteModoPago1', blank=True) # Field name made lowercase.
    modopago2 = models.SmallIntegerField(null=True, db_column='ModoPago2', blank=True) # Field name made lowercase.
    importemodopago2 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='ImporteModoPago2', blank=True) # Field name made lowercase.
    chequeado = models.SmallIntegerField(null=True, db_column='Chequeado', blank=True) # Field name made lowercase.
    importepagado = models.FloatField(null=True, db_column='ImportePagado', blank=True) # Field name made lowercase.
    pagado = models.SmallIntegerField(null=True, db_column='Pagado', blank=True) # Field name made lowercase.
    fechapagado = models.DateTimeField(null=True, db_column='FechaPagado', blank=True) # Field name made lowercase.
    nalbaran = models.IntegerField(null=True, db_column='NAlbaran', blank=True) # Field name made lowercase.
    fechaalbaran = models.DateTimeField(null=True, db_column='FechaAlbaran', blank=True) # Field name made lowercase.
    descuentototal = models.IntegerField(null=True, db_column='DescuentoTotal', blank=True) # Field name made lowercase.
    redondeo = models.IntegerField(null=True, db_column='Redondeo', blank=True) # Field name made lowercase.
    ticket_fiscal = models.IntegerField(null=True, db_column='Ticket_Fiscal', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Cabecera_Ticket_Venta'

class CabecerasBalanzas(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    numcabecera = models.SmallIntegerField(null=True, primary_key=True, db_column='NumCabecera', blank=True) # Field name made lowercase.
    cabecera = models.CharField(max_length=50, db_column='Cabecera', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Cabeceras_Balanzas'

class Cliente(models.Model):
    codigo = models.IntegerField(null=True, primary_key=True, db_column='Codigo', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=48, db_column='Nombre', blank=True) # Field name made lowercase.
    nif = models.CharField(max_length=9, db_column='NIF', blank=True) # Field name made lowercase.
    direccion = models.CharField(max_length=48, db_column='Direccion', blank=True) # Field name made lowercase.
    poblacion = models.CharField(max_length=24, db_column='Poblacion', blank=True) # Field name made lowercase.
    provincia = models.CharField(max_length=24, db_column='Provincia', blank=True) # Field name made lowercase.
    cod_postal = models.IntegerField(null=True, db_column='Cod_Postal', blank=True) # Field name made lowercase.
    telefono = models.CharField(max_length=15, db_column='Telefono', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=15, db_column='Fax', blank=True) # Field name made lowercase.
    contacto1 = models.CharField(max_length=48, db_column='Contacto1', blank=True) # Field name made lowercase.
    contacto2 = models.CharField(max_length=48, db_column='Contacto2', blank=True) # Field name made lowercase.
    forma_pago = models.CharField(max_length=15, db_column='Forma_Pago', blank=True) # Field name made lowercase.
    ventas_actual = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Ventas_Actual', blank=True) # Field name made lowercase.
    ventas_anterior = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Ventas_Anterior', blank=True) # Field name made lowercase.
    observaciones = models.CharField(max_length=200, db_column='Observaciones', blank=True) # Field name made lowercase.
    ventas_tiendas = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Ventas_Tiendas', blank=True) # Field name made lowercase.
    oper_tiendas = models.IntegerField(null=True, db_column='Oper_Tiendas', blank=True) # Field name made lowercase.
    deuda_tiendas = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Deuda_Tiendas', blank=True) # Field name made lowercase.
    formapago = models.SmallIntegerField(null=True, db_column='FormaPago', blank=True) # Field name made lowercase.
    diasvcto = models.SmallIntegerField(null=True, db_column='DiasVcto', blank=True) # Field name made lowercase.
    nombrebanco = models.CharField(max_length=20, db_column='NombreBanco', blank=True) # Field name made lowercase.
    ncuenta = models.CharField(max_length=20, db_column='NCuenta', blank=True) # Field name made lowercase.
    pais = models.CharField(max_length=20, db_column='Pais', blank=True) # Field name made lowercase.
    codtarifa = models.IntegerField(null=True, db_column='CodTarifa', blank=True) # Field name made lowercase.
    nombrecorto = models.CharField(max_length=20, db_column='NombreCorto', blank=True) # Field name made lowercase.
    texto1 = models.CharField(max_length=50, db_column='Texto1', blank=True) # Field name made lowercase.
    texto2 = models.CharField(max_length=50, db_column='Texto2', blank=True) # Field name made lowercase.
    formato = models.SmallIntegerField(null=True, db_column='Formato', blank=True) # Field name made lowercase.
    ruta = models.SmallIntegerField(null=True, db_column='Ruta', blank=True) # Field name made lowercase.
    encargado = models.CharField(max_length=50, db_column='Encargado', blank=True) # Field name made lowercase.
    texto = models.CharField(max_length=50, db_column='Texto', blank=True) # Field name made lowercase.
    ean13 = models.CharField(max_length=12, db_column='EAN13', blank=True) # Field name made lowercase.
    recargoequivalencia = models.SmallIntegerField(null=True, db_column='RecargoEquivalencia', blank=True) # Field name made lowercase.
    puntosacumulados = models.IntegerField(null=True, db_column='PuntosAcumulados', blank=True) # Field name made lowercase.
    fechaultimaventa = models.DateTimeField(null=True, db_column='FechaUltimaVenta', blank=True) # Field name made lowercase.
    anularetiquetapedidocompleto = models.SmallIntegerField(null=True, db_column='AnularEtiquetaPedidoCompleto', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Cliente'

class ClientesBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    num_cliente = models.IntegerField(null=True, primary_key=True, db_column='Num_Cliente', blank=True) # Field name made lowercase.
    cod_cliente = models.IntegerField(null=True, db_column='Cod_Cliente', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    borrado = models.SmallIntegerField(null=True, db_column='Borrado', blank=True) # Field name made lowercase.
    num_oper = models.IntegerField(null=True, db_column='Num_Oper', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    peso = models.FloatField(null=True, db_column='Peso', blank=True) # Field name made lowercase.
    num_oper_ult = models.IntegerField(null=True, db_column='Num_Oper_Ult', blank=True) # Field name made lowercase.
    importe_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Ult', blank=True) # Field name made lowercase.
    peso_ult = models.FloatField(null=True, db_column='Peso_Ult', blank=True) # Field name made lowercase.
    clave_cliente = models.CharField(max_length=1, db_column='Clave_Cliente', blank=True) # Field name made lowercase.
    inventario = models.SmallIntegerField(null=True, db_column='Inventario', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Clientes_Balanza'

class DepartamentoBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    departamento0 = models.CharField(max_length=10, db_column='Departamento0', blank=True) # Field name made lowercase.
    departamento1 = models.CharField(max_length=10, db_column='Departamento1', blank=True) # Field name made lowercase.
    departamento2 = models.CharField(max_length=10, db_column='Departamento2', blank=True) # Field name made lowercase.
    departamento3 = models.CharField(max_length=10, db_column='Departamento3', blank=True) # Field name made lowercase.
    departamento4 = models.CharField(max_length=10, db_column='Departamento4', blank=True) # Field name made lowercase.
    departamento5 = models.CharField(max_length=10, db_column='Departamento5', blank=True) # Field name made lowercase.
    departamento6 = models.CharField(max_length=10, db_column='Departamento6', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Departamento_Balanza'

class DireccionBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    direccion = models.SmallIntegerField(null=True, db_column='Direccion', blank=True) # Field name made lowercase.
    dirtcpip = models.CharField(max_length=15, db_column='DirTCPIP', blank=True) # Field name made lowercase.
    cod_modelo = models.SmallIntegerField(null=True, db_column='Cod_Modelo', blank=True) # Field name made lowercase.
    num_serie = models.CharField(max_length=12, db_column='Num_Serie', blank=True) # Field name made lowercase.
    version = models.CharField(max_length=10, db_column='Version', blank=True) # Field name made lowercase.
    num_esclavas = models.SmallIntegerField(null=True, db_column='Num_Esclavas', blank=True) # Field name made lowercase.
    comunicar_rms = models.SmallIntegerField(null=True, db_column='Comunicar_RMS', blank=True) # Field name made lowercase.
    comunicarbalanza = models.SmallIntegerField(null=True, db_column='ComunicarBalanza', blank=True) # Field name made lowercase.
    almacenactual = models.IntegerField(null=True, db_column='AlmacenActual', blank=True) # Field name made lowercase.
    almacenfuturo = models.IntegerField(null=True, db_column='AlmacenFuturo', blank=True) # Field name made lowercase.
    dirbluetooth = models.CharField(max_length=17, db_column='DirBlueTooth', blank=True) # Field name made lowercase.
    puertotx = models.IntegerField(null=True, db_column='PuertoTX', blank=True) # Field name made lowercase.
    articulosporbalanza = models.SmallIntegerField(null=True, db_column='ArticulosPorBalanza', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Direccion_Balanza'

class Familia(models.Model):
    cod_familia = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Familia', blank=True) # Field name made lowercase.
    nombre_familia = models.CharField(max_length=24, db_column='Nombre_Familia', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Familia'

class FechaTicket(models.Model):
    cod_tienda = models.IntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.IntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    fecha_primero = models.DateTimeField(null=True, db_column='Fecha_Primero', blank=True) # Field name made lowercase.
    fecha_ultimo = models.DateTimeField(null=True, db_column='Fecha_Ultimo', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Fecha_Ticket'

class FinDia(models.Model):
    orden = models.IntegerField(null=True, primary_key=True, db_column='Orden', blank=True) # Field name made lowercase.
    cod_tienda = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    direccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Direccion', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, primary_key=True, db_column='Fecha', blank=True) # Field name made lowercase.
    hora = models.CharField(max_length=5, primary_key=True, db_column='Hora', blank=True) # Field name made lowercase.
    numeracion = models.CharField(max_length=4, db_column='Numeracion', blank=True) # Field name made lowercase.
    num_tickets_acum = models.IntegerField(null=True, db_column='Num_Tickets_Acum', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    completo = models.SmallIntegerField(null=True, db_column='Completo', blank=True) # Field name made lowercase.
    causa = models.SmallIntegerField(null=True, db_column='Causa', blank=True) # Field name made lowercase.
    texto_causa = models.CharField(max_length=80, db_column='Texto_Causa', blank=True) # Field name made lowercase.
    texto_causa_ventana = models.CharField(max_length=80, db_column='Texto_Causa_Ventana', blank=True) # Field name made lowercase.
    num_tickets = models.IntegerField(null=True, db_column='Num_Tickets', blank=True) # Field name made lowercase.
    importe_tickets = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Tickets', blank=True) # Field name made lowercase.
    exportado = models.SmallIntegerField(null=True, db_column='Exportado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Fin_Dia'

class FontsBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    cod_font = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Font', blank=True) # Field name made lowercase.
    cod_letra = models.SmallIntegerField(null=True, db_column='Cod_Letra', blank=True) # Field name made lowercase.
    font = models.CharField(max_length=50, db_column='Font', blank=True) # Field name made lowercase.
    ancho = models.SmallIntegerField(null=True, db_column='Ancho', blank=True) # Field name made lowercase.
    alto = models.SmallIntegerField(null=True, db_column='Alto', blank=True) # Field name made lowercase.
    posicion = models.SmallIntegerField(null=True, db_column='Posicion', blank=True) # Field name made lowercase.
    modificado = models.BooleanField(db_column='Modificado') # Field name made lowercase.
    class Meta:
        db_table = 'Fonts_Balanza'

class FormatoEtiqueta(models.Model):
    cod_etiqueta = models.SmallIntegerField(null=True, db_column='Cod_Etiqueta', blank=True) # Field name made lowercase.
    nombre_etiqueta = models.CharField(max_length=50, db_column='Nombre_Etiqueta', blank=True) # Field name made lowercase.
    ancho_etiqueta = models.SmallIntegerField(null=True, db_column='Ancho_Etiqueta', blank=True) # Field name made lowercase.
    largo_etiqueta = models.SmallIntegerField(null=True, db_column='Largo_Etiqueta', blank=True) # Field name made lowercase.
    campos_etiqueta = models.SmallIntegerField(null=True, db_column='Campos_Etiqueta', blank=True) # Field name made lowercase.
    unidades = models.FloatField(null=True, db_column='Unidades', blank=True) # Field name made lowercase.
    modelo = models.SmallIntegerField(null=True, db_column='Modelo', blank=True) # Field name made lowercase.
    fondo_etiqueta = models.CharField(max_length=200, db_column='Fondo_Etiqueta', blank=True) # Field name made lowercase.
    visible_etiqueta = models.FloatField(null=True, db_column='Visible_Etiqueta', blank=True) # Field name made lowercase.
    ajustar_etiqueta = models.FloatField(null=True, db_column='Ajustar_Etiqueta', blank=True) # Field name made lowercase.
    articulo_etiqueta = models.FloatField(null=True, db_column='Articulo_Etiqueta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Formato_Etiqueta'

class FormatoTicket(models.Model):
    cod_ticket = models.IntegerField(null=True, primary_key=True, db_column='Cod_ticket', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=50, db_column='Descripcion', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Formato_Ticket'

class Iva(models.Model):
    cod_iva = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_IVA', blank=True) # Field name made lowercase.
    porcentaje = models.FloatField(null=True, db_column='Porcentaje', blank=True) # Field name made lowercase.
    porcentajerecargo = models.FloatField(null=True, db_column='PorcentajeRecargo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'IVA'

class IvaBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    iva1 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='IVA1', blank=True) # Field name made lowercase.
    iva2 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='IVA2', blank=True) # Field name made lowercase.
    iva3 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='IVA3', blank=True) # Field name made lowercase.
    iva4 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='IVA4', blank=True) # Field name made lowercase.
    iva5 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='IVA5', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    iva_def = models.IntegerField(null=True, db_column='IVA_Def', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'IVA_Balanza'

class Ivaporfecha(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, primary_key=True, db_column='Fecha', blank=True) # Field name made lowercase.
    cod_iva = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_IVA', blank=True) # Field name made lowercase.
    iva = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='IVA', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    base = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Base', blank=True) # Field name made lowercase.
    importeiva = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='ImporteIVA', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'IVAporFecha'

class LineaPedidoCliente(models.Model):
    cod_pedido = models.IntegerField(null=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=24, db_column='Nombre', blank=True) # Field name made lowercase.
    pedido = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Pedido', blank=True) # Field name made lowercase.
    servido = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Servido', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Linea_Pedido_Cliente'

class LineaPedidoProveedor(models.Model):
    cod_pedido = models.IntegerField(null=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=24, db_column='Nombre', blank=True) # Field name made lowercase.
    pedido = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Pedido', blank=True) # Field name made lowercase.
    recibido = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Recibido', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Linea_Pedido_Proveedor'

class LineaTicket(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    linea = models.SmallIntegerField(null=True, primary_key=True, db_column='Linea', blank=True) # Field name made lowercase.
    tipo_letra = models.CharField(max_length=1, db_column='Tipo_Letra', blank=True) # Field name made lowercase.
    texto = models.CharField(max_length=26, db_column='Texto', blank=True) # Field name made lowercase.
    tamano = models.SmallIntegerField(null=True, db_column='Tamano', blank=True) # Field name made lowercase.
    centrado = models.SmallIntegerField(null=True, db_column='Centrado', blank=True) # Field name made lowercase.
    texto_l = models.CharField(max_length=52, db_column='Texto_L', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Linea_Ticket'

class LineaTicketBorrado(models.Model):
    cod_ticket = models.IntegerField(null=True, primary_key=True, db_column='Cod_Ticket', blank=True) # Field name made lowercase.
    cod_linea_ticket = models.IntegerField(null=True, primary_key=True, db_column='Cod_Linea_Ticket', blank=True) # Field name made lowercase.
    codigo = models.IntegerField(null=True, db_column='Codigo', blank=True) # Field name made lowercase.
    nombre_articulo = models.CharField(max_length=50, db_column='Nombre_Articulo', blank=True) # Field name made lowercase.
    peso = models.FloatField(null=True, db_column='Peso', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    tipo_operacion = models.CharField(max_length=1, db_column='Tipo_Operacion', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Linea_Ticket_Borrado'

class LineaTicketVenta(models.Model):
    cod_ticket = models.IntegerField(null=True, db_column='Cod_Ticket', blank=True) # Field name made lowercase.
    cod_linea_ticket = models.IntegerField(null=True, primary_key=True, db_column='Cod_Linea_Ticket', blank=True) # Field name made lowercase.
    codigo = models.IntegerField(null=True, db_column='Codigo', blank=True) # Field name made lowercase.
    nombre_articulo = models.CharField(max_length=50, db_column='Nombre_Articulo', blank=True) # Field name made lowercase.
    peso = models.FloatField(null=True, db_column='Peso', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    tipo_operacion = models.CharField(max_length=1, db_column='Tipo_Operacion', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    facturado = models.SmallIntegerField(null=True, db_column='Facturado', blank=True) # Field name made lowercase.
    chequeado = models.SmallIntegerField(null=True, db_column='Chequeado', blank=True) # Field name made lowercase.
    cod_pedido = models.IntegerField(null=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    tipoiva = models.SmallIntegerField(null=True, db_column='TipoIVA', blank=True) # Field name made lowercase.
    porcentajeiva = models.FloatField(null=True, db_column='PorcentajeIVA', blank=True) # Field name made lowercase.
    importeiva = models.FloatField(null=True, db_column='ImporteIVA', blank=True) # Field name made lowercase.
    preciocoste = models.FloatField(null=True, db_column='PrecioCoste', blank=True) # Field name made lowercase.
    stockold = models.FloatField(null=True, db_column='StockOld', blank=True) # Field name made lowercase.
    precioultcompra = models.FloatField(null=True, db_column='PrecioUltCompra', blank=True) # Field name made lowercase.
    baseimponible = models.FloatField(null=True, db_column='BaseImponible', blank=True) # Field name made lowercase.
    und_conv = models.FloatField(null=True, db_column='Und_Conv', blank=True) # Field name made lowercase.
    rev_conv = models.SmallIntegerField(null=True, db_column='Rev_Conv', blank=True) # Field name made lowercase.
    precio_balanza = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Balanza', blank=True) # Field name made lowercase.
    descuento = models.SmallIntegerField(null=True, db_column='Descuento', blank=True) # Field name made lowercase.
    codrapidoanimal = models.SmallIntegerField(null=True, db_column='CodRapidoAnimal', blank=True) # Field name made lowercase.
    codpedido = models.IntegerField(null=True, db_column='CodPedido', blank=True) # Field name made lowercase.
    numlote = models.CharField(max_length=24, db_column='NumLote', blank=True) # Field name made lowercase.
    tara = models.FloatField(null=True, db_column='Tara', blank=True) # Field name made lowercase.
    descuentounidades = models.SmallIntegerField(null=True, db_column='DescuentoUnidades', blank=True) # Field name made lowercase.
    numpedido = models.IntegerField(null=True, db_column='NumPedido', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Linea_Ticket_Venta'

class LineaTicketVentaAnulada(models.Model):
    cod_ticket = models.IntegerField(null=True, db_column='Cod_Ticket', blank=True) # Field name made lowercase.
    cod_linea_ticket = models.IntegerField(null=True, primary_key=True, db_column='Cod_Linea_Ticket', blank=True) # Field name made lowercase.
    codigo = models.IntegerField(null=True, db_column='Codigo', blank=True) # Field name made lowercase.
    nombre_articulo = models.CharField(max_length=50, db_column='Nombre_Articulo', blank=True) # Field name made lowercase.
    peso = models.FloatField(null=True, db_column='Peso', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    tipo_operacion = models.CharField(max_length=1, db_column='Tipo_Operacion', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    precio_balanza = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio_Balanza', blank=True) # Field name made lowercase.
    descuento = models.SmallIntegerField(null=True, db_column='Descuento', blank=True) # Field name made lowercase.
    iva = models.SmallIntegerField(null=True, db_column='IVA', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Linea_Ticket_Venta_Anulada'

class LineaTraspasoAlmacen(models.Model):
    cod_traspaso = models.IntegerField(null=True, db_column='Cod_Traspaso', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=24, db_column='Nombre', blank=True) # Field name made lowercase.
    pedido = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Pedido', blank=True) # Field name made lowercase.
    servido = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Servido', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Linea_Traspaso_Almacen'

class LineaTraspasoTienda(models.Model):
    cod_traspaso = models.IntegerField(null=True, db_column='Cod_Traspaso', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=24, db_column='Nombre', blank=True) # Field name made lowercase.
    pedido = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Pedido', blank=True) # Field name made lowercase.
    servido = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Servido', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Linea_Traspaso_Tienda'

class LineasConservacion(models.Model):
    cod_conservacion = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Conservacion', blank=True) # Field name made lowercase.
    cod_linea = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Linea', blank=True) # Field name made lowercase.
    texto_linea = models.CharField(max_length=100, db_column='Texto_Linea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Lineas_Conservacion'

class LineasPedido(models.Model):
    cod_pedido = models.IntegerField(null=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, primary_key=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    nombre_articulo = models.CharField(max_length=50, db_column='Nombre_Articulo', blank=True) # Field name made lowercase.
    tipo = models.SmallIntegerField(null=True, db_column='Tipo', blank=True) # Field name made lowercase.
    num_bandejas = models.FloatField(null=True, db_column='Num_Bandejas', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Lineas_Pedido'

class LineasPedidoCompleto(models.Model):
    cod_pedido = models.IntegerField(null=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    num_pedido = models.IntegerField(null=True, primary_key=True, db_column='Num_Pedido', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, primary_key=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    nombre_articulo = models.CharField(max_length=50, db_column='Nombre_Articulo', blank=True) # Field name made lowercase.
    tipo = models.SmallIntegerField(null=True, db_column='Tipo', blank=True) # Field name made lowercase.
    num_bandejas = models.FloatField(null=True, db_column='Num_Bandejas', blank=True) # Field name made lowercase.
    precio = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Precio', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Lineas_Pedido_Completo'

class LineasPedidoMaquina(models.Model):
    codigo = models.IntegerField(null=True, db_column='Codigo', blank=True) # Field name made lowercase.
    cod_linea = models.IntegerField(null=True, primary_key=True, db_column='Cod_Linea', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    nombre_articulo = models.CharField(max_length=50, db_column='Nombre_Articulo', blank=True) # Field name made lowercase.
    num_etiquetas = models.IntegerField(null=True, db_column='Num_Etiquetas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Lineas_Pedido_Maquina'

class PedidoBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    direccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Direccion', blank=True) # Field name made lowercase.
    cod_pedido = models.IntegerField(null=True, primary_key=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, primary_key=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    etiquetadas = models.IntegerField(null=True, db_column='Etiquetadas', blank=True) # Field name made lowercase.
    peso = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Peso', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    estado = models.SmallIntegerField(null=True, db_column='Estado', blank=True) # Field name made lowercase.
    modificado = models.BooleanField(db_column='Modificado') # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado') # Field name made lowercase.
    anadir = models.SmallIntegerField(null=True, db_column='Anadir', blank=True) # Field name made lowercase.
    ordenprioridad = models.IntegerField(null=True, db_column='OrdenPrioridad', blank=True) # Field name made lowercase.
    modificadoprioridad = models.BooleanField(db_column='ModificadoPrioridad') # Field name made lowercase.
    class Meta:
        db_table = 'Pedido_Balanza'

class PedidoBalanzaCompleto(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    direccion = models.SmallIntegerField(null=True, primary_key=True, db_column='Direccion', blank=True) # Field name made lowercase.
    cod_pedido = models.IntegerField(null=True, primary_key=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    num_pedido = models.IntegerField(null=True, primary_key=True, db_column='Num_Pedido', blank=True) # Field name made lowercase.
    cod_articulo = models.IntegerField(null=True, primary_key=True, db_column='Cod_Articulo', blank=True) # Field name made lowercase.
    etiquetadas = models.IntegerField(null=True, db_column='Etiquetadas', blank=True) # Field name made lowercase.
    peso = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Peso', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    estado = models.SmallIntegerField(null=True, db_column='Estado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Pedido_Balanza_Completo'

class PedidoCliente(models.Model):
    cod_pedido = models.IntegerField(null=True, primary_key=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    cod_cliente = models.IntegerField(null=True, db_column='Cod_Cliente', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=48, db_column='Nombre', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    observaciones = models.CharField(max_length=20, db_column='Observaciones', blank=True) # Field name made lowercase.
    servido = models.CharField(max_length=1, db_column='Servido', blank=True) # Field name made lowercase.
    completo = models.CharField(max_length=1, db_column='Completo', blank=True) # Field name made lowercase.
    numero = models.IntegerField(null=True, db_column='Numero', blank=True) # Field name made lowercase.
    dto = models.SmallIntegerField(null=True, db_column='Dto', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Pedido_Cliente'

class PedidoClienteGrupo(models.Model):
    cliente = models.IntegerField(null=True, primary_key=True, db_column='Cliente', blank=True) # Field name made lowercase.
    grupo = models.IntegerField(null=True, db_column='Grupo', blank=True) # Field name made lowercase.
    ruta = models.IntegerField(null=True, db_column='Ruta', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=50, db_column='Nombre', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Pedido_Cliente_Grupo'

class PedidoProveedor(models.Model):
    cod_pedido = models.IntegerField(null=True, primary_key=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    cod_proveedor = models.SmallIntegerField(null=True, db_column='Cod_Proveedor', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=48, db_column='Nombre', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    observaciones = models.CharField(max_length=20, db_column='Observaciones', blank=True) # Field name made lowercase.
    servido = models.CharField(max_length=1, db_column='Servido', blank=True) # Field name made lowercase.
    completo = models.CharField(max_length=1, db_column='Completo', blank=True) # Field name made lowercase.
    numero = models.IntegerField(null=True, db_column='Numero', blank=True) # Field name made lowercase.
    dto = models.SmallIntegerField(null=True, db_column='Dto', blank=True) # Field name made lowercase.
    pagado = models.SmallIntegerField(null=True, db_column='Pagado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Pedido_Proveedor'

class Pedidos(models.Model):
    cod_pedido = models.IntegerField(null=True, primary_key=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    cod_cliente = models.IntegerField(null=True, db_column='Cod_Cliente', blank=True) # Field name made lowercase.
    nombre_cliente = models.CharField(max_length=50, db_column='Nombre_Cliente', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    num_articulos = models.IntegerField(null=True, db_column='Num_Articulos', blank=True) # Field name made lowercase.
    operacion = models.CharField(max_length=1, db_column='Operacion', blank=True) # Field name made lowercase.
    estado = models.SmallIntegerField(null=True, db_column='Estado', blank=True) # Field name made lowercase.
    iden_pedido = models.CharField(max_length=20, db_column='Iden_Pedido', blank=True) # Field name made lowercase.
    generaficheroservido = models.SmallIntegerField(null=True, db_column='GeneraFicheroServido', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Pedidos'

class PedidosCompleto(models.Model):
    cod_pedido = models.IntegerField(null=True, primary_key=True, db_column='Cod_Pedido', blank=True) # Field name made lowercase.
    num_pedido = models.IntegerField(null=True, primary_key=True, db_column='Num_Pedido', blank=True) # Field name made lowercase.
    cod_cliente = models.IntegerField(null=True, db_column='Cod_Cliente', blank=True) # Field name made lowercase.
    nombre_cliente = models.CharField(max_length=50, db_column='Nombre_Cliente', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    num_articulos = models.IntegerField(null=True, db_column='Num_Articulos', blank=True) # Field name made lowercase.
    operacion = models.CharField(max_length=1, db_column='Operacion', blank=True) # Field name made lowercase.
    estado = models.SmallIntegerField(null=True, db_column='Estado', blank=True) # Field name made lowercase.
    iden_pedido = models.CharField(max_length=20, db_column='Iden_Pedido', blank=True) # Field name made lowercase.
    generaficheroservido = models.SmallIntegerField(null=True, db_column='GeneraFicheroServido', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Pedidos_Completo'

class PedidosMaquina(models.Model):
    codigo = models.IntegerField(null=True, primary_key=True, db_column='Codigo', blank=True) # Field name made lowercase.
    identificacion = models.CharField(max_length=50, db_column='Identificacion', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Pedidos_Maquina'

class PedidosMaquinaBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    num_pedido = models.SmallIntegerField(null=True, primary_key=True, db_column='Num_Pedido', blank=True) # Field name made lowercase.
    codigo = models.IntegerField(null=True, db_column='Codigo', blank=True) # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado') # Field name made lowercase.
    alta = models.BooleanField(db_column='Alta') # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Pedidos_Maquina_Balanza'

class Proveedor(models.Model):
    codigo = models.SmallIntegerField(null=True, primary_key=True, db_column='Codigo', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=48, db_column='Nombre', blank=True) # Field name made lowercase.
    nif = models.CharField(max_length=9, db_column='NIF', blank=True) # Field name made lowercase.
    direccion = models.CharField(max_length=48, db_column='Direccion', blank=True) # Field name made lowercase.
    poblacion = models.CharField(max_length=24, db_column='Poblacion', blank=True) # Field name made lowercase.
    provincia = models.CharField(max_length=24, db_column='Provincia', blank=True) # Field name made lowercase.
    cod_postal = models.IntegerField(null=True, db_column='Cod_Postal', blank=True) # Field name made lowercase.
    telefono = models.CharField(max_length=15, db_column='Telefono', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=15, db_column='Fax', blank=True) # Field name made lowercase.
    contacto1 = models.CharField(max_length=48, db_column='Contacto1', blank=True) # Field name made lowercase.
    contacto2 = models.CharField(max_length=48, db_column='Contacto2', blank=True) # Field name made lowercase.
    forma_pago = models.CharField(max_length=15, db_column='Forma_Pago', blank=True) # Field name made lowercase.
    compras_actual = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Compras_Actual', blank=True) # Field name made lowercase.
    compras_anterior = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Compras_Anterior', blank=True) # Field name made lowercase.
    observaciones = models.CharField(max_length=200, db_column='Observaciones', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Proveedor'
	cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    publicidad1 = models.CharField(max_length=119, db_column='Publicidad1', blank=True) # Field name made lowercase.
    ritmo1 = models.SmallIntegerField(null=True, db_column='Ritmo1', blank=True) # Field name made lowercase.
    publicidad2 = models.CharField(max_length=119, db_column='Publicidad2', blank=True) # Field name made lowercase.
    ritmo2 = models.SmallIntegerField(null=True, db_column='Ritmo2', blank=True) # Field name made lowercase.
    publicidad3 = models.CharField(max_length=119, db_column='Publicidad3', blank=True) # Field name made lowercase.
    ritmo3 = models.SmallIntegerField(null=True, db_column='Ritmo3', blank=True) # Field name made lowercase.
    publicidad4 = models.CharField(max_length=119, db_column='Publicidad4', blank=True) # Field name made lowercase.
    ritmo4 = models.SmallIntegerField(null=True, db_column='Ritmo4', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Publicidad'


    codigo = models.SmallIntegerField(null=True, primary_key=True, db_column='Codigo', blank=True) # Field name made lowercase.
    modo_titulo = models.SmallIntegerField(null=True, db_column='Modo_Titulo', blank=True) # Field name made lowercase.
    font_titulo = models.SmallIntegerField(null=True, db_column='Font_Titulo', blank=True) # Field name made lowercase.
    magnificacion_titulo = models.SmallIntegerField(null=True, db_column='Magnificacion_Titulo', blank=True) # Field name made lowercase.
    modo_lineas = models.SmallIntegerField(null=True, db_column='Modo_Lineas', blank=True) # Field name made lowercase.
    font_lineas = models.SmallIntegerField(null=True, db_column='Font_Lineas', blank=True) # Field name made lowercase.
    magnificacion_lineas = models.SmallIntegerField(null=True, db_column='Magnificacion_Lineas', blank=True) # Field name made lowercase.
    texto_titulo = models.CharField(max_length=32, db_column='Texto_Titulo', blank=True) # Field name made lowercase.
    modo_logo = models.SmallIntegerField(null=True, db_column='Modo_Logo', blank=True) # Field name made lowercase.
    num_logo = models.SmallIntegerField(null=True, db_column='Num_Logo', blank=True) # Field name made lowercase.
    rotacion_logo = models.SmallIntegerField(null=True, db_column='Rotacion_Logo', blank=True) # Field name made lowercase.
    texto_lp3xxx = models.TextField(db_column='Texto_LP3XXX', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'Recetas'

class RecetasBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    num_receta = models.SmallIntegerField(null=True, primary_key=True, db_column='Num_Receta', blank=True) # Field name made lowercase.
    cod_receta = models.SmallIntegerField(null=True, db_column='Cod_Receta', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    borrado = models.SmallIntegerField(null=True, db_column='Borrado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Recetas_Balanza'

class Seccion(models.Model):
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    nombre_seccion = models.CharField(max_length=24, db_column='Nombre_Seccion', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Seccion'

class SeccionBalanza(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    seccion0 = models.CharField(max_length=20, db_column='Seccion0', blank=True) # Field name made lowercase.
    seccion1 = models.CharField(max_length=20, db_column='Seccion1', blank=True) # Field name made lowercase.
    seccion2 = models.CharField(max_length=20, db_column='Seccion2', blank=True) # Field name made lowercase.
    seccion3 = models.CharField(max_length=20, db_column='Seccion3', blank=True) # Field name made lowercase.
    seccion4 = models.CharField(max_length=20, db_column='Seccion4', blank=True) # Field name made lowercase.
    seccion5 = models.CharField(max_length=20, db_column='Seccion5', blank=True) # Field name made lowercase.
    seccion6 = models.CharField(max_length=20, db_column='Seccion6', blank=True) # Field name made lowercase.
    seccion7 = models.CharField(max_length=20, db_column='Seccion7', blank=True) # Field name made lowercase.
    seccion8 = models.CharField(max_length=20, db_column='Seccion8', blank=True) # Field name made lowercase.
    seccion9 = models.CharField(max_length=20, db_column='Seccion9', blank=True) # Field name made lowercase.
    seccion10 = models.CharField(max_length=20, db_column='Seccion10', blank=True) # Field name made lowercase.
    seccion11 = models.CharField(max_length=20, db_column='Seccion11', blank=True) # Field name made lowercase.
    seccion12 = models.CharField(max_length=20, db_column='Seccion12', blank=True) # Field name made lowercase.
    seccion13 = models.CharField(max_length=20, db_column='Seccion13', blank=True) # Field name made lowercase.
    seccion14 = models.CharField(max_length=20, db_column='Seccion14', blank=True) # Field name made lowercase.
    seccion15 = models.CharField(max_length=20, db_column='Seccion15', blank=True) # Field name made lowercase.
    seccion16 = models.CharField(max_length=20, db_column='Seccion16', blank=True) # Field name made lowercase.
    seccion17 = models.CharField(max_length=20, db_column='Seccion17', blank=True) # Field name made lowercase.
    seccion18 = models.CharField(max_length=20, db_column='Seccion18', blank=True) # Field name made lowercase.
    seccion19 = models.CharField(max_length=20, db_column='Seccion19', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Seccion_Balanza'

class SeccionBalanzaL(models.Model):
    cod_tienda = models.IntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.IntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    nseccion = models.SmallIntegerField(null=True, primary_key=True, db_column='NSeccion', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=24, db_column='Descripcion', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    logo = models.SmallIntegerField(null=True, db_column='Logo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Seccion_Balanza_L'

class Subfamilia(models.Model):
    cod_familia = models.SmallIntegerField(null=True, db_column='Cod_Familia', blank=True) # Field name made lowercase.
    cod_subfamilia = models.SmallIntegerField(null=True, db_column='Cod_Subfamilia', blank=True) # Field name made lowercase.
    nombre_subfamilia = models.CharField(max_length=24, db_column='Nombre_Subfamilia', blank=True) # Field name made lowercase.
    coste = models.FloatField(null=True, db_column='Coste', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Subfamilia'

class Tara(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    tara1 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Tara1', blank=True) # Field name made lowercase.
    tara2 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Tara2', blank=True) # Field name made lowercase.
    tara3 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Tara3', blank=True) # Field name made lowercase.
    tara4 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Tara4', blank=True) # Field name made lowercase.
    tara5 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Tara5', blank=True) # Field name made lowercase.
    tara6 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Tara6', blank=True) # Field name made lowercase.
    tara7 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Tara7', blank=True) # Field name made lowercase.
    tara8 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Tara8', blank=True) # Field name made lowercase.
    tara9 = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Tara9', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Tara'

class TarasSeccion(models.Model):
    codseccion = models.SmallIntegerField(null=True, primary_key=True, db_column='CodSeccion', blank=True) # Field name made lowercase.
    codtara = models.IntegerField(null=True, primary_key=True, db_column='CodTara', blank=True) # Field name made lowercase.
    tara = models.FloatField(null=True, db_column='Tara', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Taras_Seccion'

class TicketBalanza(models.Model):
    cod_tienda = models.IntegerField(null=True, primary_key=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.IntegerField(null=True, primary_key=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    num_ticket = models.IntegerField(null=True, primary_key=True, db_column='Num_Ticket', blank=True) # Field name made lowercase.
    cod_ticket = models.IntegerField(null=True, db_column='Cod_Ticket', blank=True) # Field name made lowercase.
    modificado = models.SmallIntegerField(null=True, db_column='Modificado', blank=True) # Field name made lowercase.
    borrado = models.SmallIntegerField(null=True, db_column='Borrado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Ticket_Balanza'

class Tienda(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    nombre_tienda = models.CharField(max_length=24, db_column='Nombre_Tienda', blank=True) # Field name made lowercase.
    direccion = models.CharField(max_length=48, db_column='Direccion', blank=True) # Field name made lowercase.
    poblacion = models.CharField(max_length=24, db_column='Poblacion', blank=True) # Field name made lowercase.
    provincia = models.CharField(max_length=24, db_column='Provincia', blank=True) # Field name made lowercase.
    cod_postal = models.CharField(max_length=15, db_column='Cod_Postal', blank=True) # Field name made lowercase.
    telefono = models.CharField(max_length=15, db_column='Telefono', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=15, db_column='Fax', blank=True) # Field name made lowercase.
    modem = models.CharField(max_length=15, db_column='Modem', blank=True) # Field name made lowercase.
    encargado = models.CharField(max_length=48, db_column='Encargado', blank=True) # Field name made lowercase.
    texto = models.CharField(max_length=200, db_column='Texto', blank=True) # Field name made lowercase.
    marcacionpulsostonos = models.BooleanField(db_column='MarcacionPulsosTonos') # Field name made lowercase.
    velocidadcomunicacion = models.SmallIntegerField(null=True, db_column='VelocidadComunicacion', blank=True) # Field name made lowercase.
    testablecimientollamada = models.SmallIntegerField(null=True, db_column='TEstablecimientoLlamada', blank=True) # Field name made lowercase.
    tfindatos = models.SmallIntegerField(null=True, db_column='TFinDatos', blank=True) # Field name made lowercase.
    numintentos = models.SmallIntegerField(null=True, db_column='NumIntentos', blank=True) # Field name made lowercase.
    puerto = models.SmallIntegerField(null=True, db_column='Puerto', blank=True) # Field name made lowercase.
    bits = models.SmallIntegerField(null=True, db_column='Bits', blank=True) # Field name made lowercase.
    tpolling = models.SmallIntegerField(null=True, db_column='TPolling', blank=True) # Field name made lowercase.
    tesperamensaje = models.SmallIntegerField(null=True, db_column='TEsperaMensaje', blank=True) # Field name made lowercase.
    local = models.BooleanField(db_column='Local') # Field name made lowercase.
    paridad = models.SmallIntegerField(null=True, db_column='Paridad', blank=True) # Field name made lowercase.
    tipocomunicacion = models.IntegerField(null=True, db_column='TipoComunicacion', blank=True) # Field name made lowercase.
    tiendaauchan = models.BooleanField(db_column='TiendaAuchan') # Field name made lowercase.
    puertobluetooth = models.SmallIntegerField(null=True, db_column='PuertoBlueTooth', blank=True) # Field name made lowercase.
    adsl = models.SmallIntegerField(null=True, db_column='ADSL', blank=True) # Field name made lowercase.
    puertotx = models.IntegerField(null=True, db_column='PuertoTX', blank=True) # Field name made lowercase.
    puertorx = models.IntegerField(null=True, db_column='PuertoRX', blank=True) # Field name made lowercase.
    codepage = models.SmallIntegerField(null=True, db_column='CodePage', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Tienda'

class TiendaSeccion(models.Model):
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    cod_seccion = models.SmallIntegerField(null=True, db_column='Cod_Seccion', blank=True) # Field name made lowercase.
    peticion_ticket = models.BooleanField(db_column='Peticion_Ticket') # Field name made lowercase.
    comienzo_dia = models.BooleanField(db_column='Comienzo_Dia') # Field name made lowercase.
    fin_dia_sin_borrado = models.BooleanField(db_column='Fin_Dia_Sin_Borrado') # Field name made lowercase.
    fin_dia_con_borrado = models.BooleanField(db_column='Fin_Dia_Con_Borrado') # Field name made lowercase.
    borrado_ventas = models.BooleanField(db_column='Borrado_Ventas') # Field name made lowercase.
    inicializar_balanzas = models.BooleanField(db_column='Inicializar_Balanzas') # Field name made lowercase.
    envio_precios = models.BooleanField(db_column='Envio_Precios') # Field name made lowercase.
    seleccionado = models.BooleanField(db_column='Seleccionado') # Field name made lowercase.
    envio_ingredientes = models.BooleanField(db_column='Envio_Ingredientes') # Field name made lowercase.
    carga_articulos = models.BooleanField(db_column='Carga_Articulos') # Field name made lowercase.
    envio_vacuno = models.BooleanField(db_column='Envio_Vacuno') # Field name made lowercase.
    seleccion_ahold = models.BooleanField(db_column='Seleccion_Ahold') # Field name made lowercase.
    etiquetar_plu = models.BooleanField(db_column='Etiquetar_PLU') # Field name made lowercase.
    etiquetar_pedido = models.BooleanField(db_column='Etiquetar_Pedido') # Field name made lowercase.
    cambio_precio = models.SmallIntegerField(null=True, db_column='Cambio_Precio', blank=True) # Field name made lowercase.
    envio_logos = models.BooleanField(db_column='Envio_Logos') # Field name made lowercase.
    peticion_articulos = models.BooleanField(db_column='Peticion_Articulos') # Field name made lowercase.
    configurar_display = models.BooleanField(db_column='Configurar_Display') # Field name made lowercase.
    logos_display_azul = models.BooleanField(db_column='Logos_Display_Azul') # Field name made lowercase.
    envio_sms = models.BooleanField(db_column='Envio_SMS') # Field name made lowercase.
    envio_fonts_v = models.BooleanField(db_column='Envio_Fonts_V') # Field name made lowercase.
    prioridadpedidos = models.BooleanField(db_column='PrioridadPedidos') # Field name made lowercase.
    inicializar_precios = models.BooleanField(db_column='Inicializar_Precios') # Field name made lowercase.
    noenviarconfiguracion = models.BooleanField(db_column='NoEnviarConfiguracion') # Field name made lowercase.
    class Meta:
        db_table = 'Tienda_Seccion'

class TipoCodbarras(models.Model):
    cod_tipo = models.SmallIntegerField(null=True, primary_key=True, db_column='Cod_Tipo', blank=True) # Field name made lowercase.
    modelo = models.CharField(max_length=10, primary_key=True, db_column='Modelo', blank=True) # Field name made lowercase.
    altura = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Altura', blank=True) # Field name made lowercase.
    anchura = models.SmallIntegerField(null=True, db_column='Anchura', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Tipo_CodBarras'

class TipoLetra(models.Model):
    numero = models.SmallIntegerField(null=True, primary_key=True, db_column='Numero', blank=True) # Field name made lowercase.
    nombre_font = models.CharField(max_length=50, db_column='Nombre_Font', blank=True) # Field name made lowercase.
    font_ancho = models.SmallIntegerField(null=True, db_column='Font_Ancho', blank=True) # Field name made lowercase.
    font_alto = models.SmallIntegerField(null=True, db_column='Font_Alto', blank=True) # Field name made lowercase.
    por_ancho = models.SmallIntegerField(null=True, db_column='Por_Ancho', blank=True) # Field name made lowercase.
    por_alto = models.SmallIntegerField(null=True, db_column='Por_Alto', blank=True) # Field name made lowercase.
    etiq = models.SmallIntegerField(null=True, db_column='Etiq', blank=True) # Field name made lowercase.
    pea = models.SmallIntegerField(null=True, db_column='PEA', blank=True) # Field name made lowercase.
    a_k = models.SmallIntegerField(null=True, db_column='A_K', blank=True) # Field name made lowercase.
    m = models.SmallIntegerField(null=True, db_column='M', blank=True) # Field name made lowercase.
    l = models.SmallIntegerField(null=True, db_column='L', blank=True) # Field name made lowercase.
    lp3xxx = models.SmallIntegerField(null=True, db_column='LP3XXX', blank=True) # Field name made lowercase.
    k_standard = models.IntegerField(null=True, db_column='K_Standard', blank=True) # Field name made lowercase.
    k_australia = models.IntegerField(null=True, db_column='K_Australia', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Tipo_Letra'

class TraspasoAlmacen(models.Model):
    cod_traspaso = models.IntegerField(null=True, primary_key=True, db_column='Cod_Traspaso', blank=True) # Field name made lowercase.
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=48, db_column='Nombre', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    servido = models.CharField(max_length=1, db_column='Servido', blank=True) # Field name made lowercase.
    completo = models.CharField(max_length=1, db_column='Completo', blank=True) # Field name made lowercase.
    numero = models.IntegerField(null=True, db_column='Numero', blank=True) # Field name made lowercase.
    observaciones = models.CharField(max_length=20, db_column='Observaciones', blank=True) # Field name made lowercase.
    dto = models.SmallIntegerField(null=True, db_column='Dto', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Traspaso_Almacen'

class TraspasoTienda(models.Model):
    cod_traspaso = models.IntegerField(null=True, primary_key=True, db_column='Cod_Traspaso', blank=True) # Field name made lowercase.
    cod_tienda = models.SmallIntegerField(null=True, db_column='Cod_Tienda', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=48, db_column='Nombre', blank=True) # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    servido = models.CharField(max_length=1, db_column='Servido', blank=True) # Field name made lowercase.
    completo = models.CharField(max_length=1, db_column='Completo', blank=True) # Field name made lowercase.
    numero = models.IntegerField(null=True, db_column='Numero', blank=True) # Field name made lowercase.
    observaciones = models.CharField(max_length=20, db_column='Observaciones', blank=True) # Field name made lowercase.
    dto = models.SmallIntegerField(null=True, db_column='Dto', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Traspaso_Tienda'

class UltimoTicket(models.Model):
    tienda = models.SmallIntegerField(null=True, db_column='Tienda', blank=True) # Field name made lowercase.
    balanza = models.SmallIntegerField(null=True, primary_key=True, db_column='Balanza', blank=True) # Field name made lowercase.
    cod_ticket = models.IntegerField(null=True, db_column='Cod_Ticket', blank=True) # Field name made lowercase.
    num_ticket = models.IntegerField(null=True, db_column='Num_Ticket', blank=True) # Field name made lowercase.
    importebruto = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='ImporteBruto', blank=True) # Field name made lowercase.
    numoperaciones = models.IntegerField(null=True, db_column='NumOperaciones', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Ultimo_Ticket'

class UltimoTicketL(models.Model):
    tienda = models.SmallIntegerField(null=True, db_column='Tienda', blank=True) # Field name made lowercase.
    balanza = models.SmallIntegerField(null=True, primary_key=True, db_column='Balanza', blank=True) # Field name made lowercase.
    cod_vendedor = models.IntegerField(null=True, primary_key=True, db_column='Cod_Vendedor', blank=True) # Field name made lowercase.
    cod_ticket = models.IntegerField(null=True, db_column='Cod_Ticket', blank=True) # Field name made lowercase.
    num_ticket = models.IntegerField(null=True, db_column='Num_Ticket', blank=True) # Field name made lowercase.
    importebruto = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='ImporteBruto', blank=True) # Field name made lowercase.
    numoperaciones = models.IntegerField(null=True, db_column='NumOperaciones', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Ultimo_Ticket_L'

class Vendedor(models.Model):
    codigo = models.IntegerField(null=True, primary_key=True, db_column='Codigo', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=48, db_column='Nombre', blank=True) # Field name made lowercase.
    nif = models.CharField(max_length=9, db_column='NIF', blank=True) # Field name made lowercase.
    direccion = models.CharField(max_length=48, db_column='Direccion', blank=True) # Field name made lowercase.
    poblacion = models.CharField(max_length=24, db_column='Poblacion', blank=True) # Field name made lowercase.
    provincia = models.CharField(max_length=24, db_column='Provincia', blank=True) # Field name made lowercase.
    cod_postal = models.IntegerField(null=True, db_column='Cod_Postal', blank=True) # Field name made lowercase.
    telefono = models.CharField(max_length=15, db_column='Telefono', blank=True) # Field name made lowercase.
    telefono2 = models.CharField(max_length=15, db_column='Telefono2', blank=True) # Field name made lowercase.
    observaciones = models.CharField(max_length=200, db_column='Observaciones', blank=True) # Field name made lowercase.
    operaciones = models.IntegerField(null=True, db_column='Operaciones', blank=True) # Field name made lowercase.
    importe = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe', blank=True) # Field name made lowercase.
    operaciones_mayoristas = models.IntegerField(null=True, db_column='Operaciones_Mayoristas', blank=True) # Field name made lowercase.
    importe_mayoristas = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Mayoristas', blank=True) # Field name made lowercase.
    operaciones_negativas = models.IntegerField(null=True, db_column='Operaciones_Negativas', blank=True) # Field name made lowercase.
    importe_negativas = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Negativas', blank=True) # Field name made lowercase.
    operaciones_pesadas = models.IntegerField(null=True, db_column='Operaciones_Pesadas', blank=True) # Field name made lowercase.
    importe_pesadas = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Pesadas', blank=True) # Field name made lowercase.
    operaciones_nopesadas = models.IntegerField(null=True, db_column='Operaciones_NoPesadas', blank=True) # Field name made lowercase.
    importe_nopesadas = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_NoPesadas', blank=True) # Field name made lowercase.
    operaciones_devueltas = models.IntegerField(null=True, db_column='Operaciones_Devueltas', blank=True) # Field name made lowercase.
    importe_devueltas = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Devueltas', blank=True) # Field name made lowercase.
    tiempo_alta = models.IntegerField(null=True, db_column='Tiempo_Alta', blank=True) # Field name made lowercase.
    tiempo_atendiendo = models.IntegerField(null=True, db_column='Tiempo_Atendiendo', blank=True) # Field name made lowercase.
    importe_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Ult', blank=True) # Field name made lowercase.
    operaciones_ult = models.IntegerField(null=True, db_column='Operaciones_Ult', blank=True) # Field name made lowercase.
    operaciones_mayoristas_ult = models.IntegerField(null=True, db_column='Operaciones_Mayoristas_Ult', blank=True) # Field name made lowercase.
    importe_mayoristas_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Mayoristas_Ult', blank=True) # Field name made lowercase.
    operaciones_negativas_ult = models.IntegerField(null=True, db_column='Operaciones_Negativas_Ult', blank=True) # Field name made lowercase.
    importe_negativas_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Negativas_Ult', blank=True) # Field name made lowercase.
    operaciones_pesadas_ult = models.IntegerField(null=True, db_column='Operaciones_Pesadas_Ult', blank=True) # Field name made lowercase.
    importe_pesadas_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Pesadas_Ult', blank=True) # Field name made lowercase.
    operaciones_nopesadas_ult = models.IntegerField(null=True, db_column='Operaciones_NoPesadas_Ult', blank=True) # Field name made lowercase.
    importe_nopesadas_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_NoPesadas_Ult', blank=True) # Field name made lowercase.
    operaciones_devueltas_ult = models.IntegerField(null=True, db_column='Operaciones_Devueltas_Ult', blank=True) # Field name made lowercase.
    importe_devueltas_ult = models.DecimalField(decimal_places=4, null=True, max_digits=19, db_column='Importe_Devueltas_Ult', blank=True) # Field name made lowercase.
    tiempo_alta_ult = models.IntegerField(null=True, db_column='Tiempo_Alta_Ult', blank=True) # Field name made lowercase.
    tiempo_atendiendo_ult = models.IntegerField(null=True, db_column='Tiempo_Atendiendo_Ult', blank=True) # Field name made lowercase.
    pin = models.CharField(max_length=50, db_column='PIN', blank=True) # Field name made lowercase.
    nivelseguridad = models.SmallIntegerField(null=True, db_column='NivelSeguridad', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Vendedor'
