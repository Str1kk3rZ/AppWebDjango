from django.contrib import admin
from .models import categoriaProd, Producto

# Register your models here.

class categoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(categoriaProd, categoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)
