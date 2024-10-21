from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from .models import Pedidos
from .forms import PedidosForm
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})


def criar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')

    else:
        form = ClienteForm()
    return render(request, 'clientes/criar_clientes.html', {'form': form})


def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/atualizar_cliente.html', {'form': form})


def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/deletar_cliente.html', {'cliente': cliente})


def listar_pedidos(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'pedidos/listar_pedidos.html', {'pedidos': pedidos})


def criar_pedido(request):
    if request.method == "POST":
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidosForm()
    return render(request, 'pedidos/criar_pedidos.html', {'form': form})


def atualizar_pedido(request, id):
    pedido = get_object_or_404(Pedidos, id=id)
    if request.method == "POST":
        form = PedidosForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidosForm(instance=pedido)
    return render(request, 'pedidos/atualizar_pedido.html', {'form': form})


def deletar_pedido(request, id):
    pedido = get_object_or_404(Pedidos, id=id)
    if request.method == "POST":
        pedido.delete()
        # Redireciona para a lista de pedidos
        return redirect('listar_pedidos')
    return render(request, 'pedidos/deletar_pedido.html', {'pedido': pedido})

def exportar_clientes_pdf(request):
    # Buscando todos os usuários
    clientes = Cliente.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('clientes/clientes_pdf.html', {'clientes': clientes})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="clientes.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response