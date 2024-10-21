from django.urls import path
from .import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('novo', views.criar_cliente, name='criar_clientes'),
    path('editar/<int:id>/', views.atualizar_cliente, name='atualizar_cliente'),
    path('deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),
    path('exportar_clientes_pdf/', views.exportar_clientes_pdf, name='exportar_clientes_pdf'),

    path('pedidos', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/novo/', views.criar_pedido, name='criar_pedidos'),
    path('pedidos/editar/<int:id>/', views.atualizar_pedido, name='atualizar_pedido'),
    path('pedidos/deletar/<int:id>/', views.deletar_pedido, name='deletar_pedido'),
]
