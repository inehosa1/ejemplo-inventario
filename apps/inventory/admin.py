from django.contrib import admin
from .models import Product, Alert

class AlertInline(admin.TabularInline):
    """
    Interfaz inline en el panel de administración para mostrar las alertas asociadas a un producto.
    """
    model = Alert
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    """
    Configuración personalizada del panel de administración para el modelo Product.
    
    Muestra campos relevantes, permite búsquedas y filtros, e incorpora las alertas como inline.
    """
    list_display = ('name', 'quantity', 'expiration_date', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('expiration_date', 'created_at')
    inlines = [AlertInline]

class AlertAdmin(admin.ModelAdmin):
    """
    Configuración personalizada del panel de administración para el modelo Alert.
    
    Permite visualizar información clave de cada alerta, filtrar por estado y fecha de creación, y realizar búsquedas.
    """
    list_display = ('id', 'product', 'days_before_expiration', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('product__name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Alert, AlertAdmin)
