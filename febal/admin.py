from django.contrib import admin
from febal.models import *
from febal.acciones import *
class ClienteAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        q = Cliente.objects.all().filter(importacion__usuario = request.user)
        return q
admin.site.register(Cliente,ClienteAdmin)

class VendedorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        q = Vendedor.objects.all().filter(importacion__usuario = request.user)
        return q

admin.site.register(Vendedor,VendedorAdmin)

class ArticuloAdmin(admin.ModelAdmin):
    '''Contruido a partir de parts de diferentes origenes
    '''
    def get_queryset(self, request):
        q = Articulo.objects.all().filter(importacion__usuario = request.user)
        return q

    ordering = ('cod_articulo',)
    list_filter = ['cod_familia','cod_subfamilia','tipo']
    search_fields = ['nombre']

admin.site.register(Articulo,ArticuloAdmin)

admin.site.register(LineaTicketVentaFebal)
class LineaTicketVentaFebalInline(admin.TabularInline):
    model =  LineaTicketVentaFebal

class CabeceraTicketVentaAdmin(admin.ModelAdmin):
    actions = ['crearAgrupadoTickets_Lista']
    def crearAgrupadoTickets_Lista(self, request, queryset):
	    return crearAgrupadoTickets_Lista(request,queryset)
    
    '''Contruido a partir de parts de diferentes origenes
    '''
    def get_queryset(self, request):
        q = CabeceraTicketVentaFebal.objects.all().filter(importacion__usuario = request.user)
        return q

    
    
    inlines = [ LineaTicketVentaFebalInline ]
    ordering = ('cod_ticket',)
    list_filter = ['fecha','vendedor','numerocliente']
    search_fields = ['fecha']
admin.site.register(CabeceraTicketVentaFebal,CabeceraTicketVentaAdmin)


admin.site.register(AgrupadoLineaTicket)

class AgrupadoLineaTicketInline(admin.TabularInline):
    def get_queryset(self, request):
        q = AgrupadoLineaTicket.objects.all().filter(importacion__usuario = request.user)
        return q
    
    raw_id_fields = ("cod_linea_ticket",)
    model = AgrupadoLineaTicket

class AgrupadoCabeceraTicketAdmin(admin.ModelAdmin):
    '''Contruido a partir de parts de diferentes origenes
    '''
    def get_queryset(self, request):
        q = AgrupadoCabeceraTicket.objects.all().filter(importacion__usuario = request.user)
        return q    
    
    inlines = [ AgrupadoLineaTicketInline ]
    #ordering = ('cod_ticket',)
    #list_filter = ['fecha','vendedor','numerocliente']
    #search_fields = ['fecha']
    raw_id_fields = ("tickets",)
    models = AgrupadoCabeceraTicket
admin.site.register(AgrupadoCabeceraTicket,AgrupadoCabeceraTicketAdmin)
