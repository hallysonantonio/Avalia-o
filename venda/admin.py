from django.contrib import admin

from .models import Cliente, Pedidos

admin.site.register(Cliente)
admin.site.register(Pedidos)