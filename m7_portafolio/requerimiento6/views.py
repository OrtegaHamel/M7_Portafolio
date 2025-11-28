from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# LISTAR
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, "requerimiento6/producto_list.html", {"productos": productos})

# CREAR
def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto_list")
    else:
        form = ProductoForm()

    return render(request, "requerimiento6/producto_form.html", {"form": form})

# EDITAR
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("producto_list")
    else:
        form = ProductoForm(instance=producto)

    return render(request, "requerimiento6/producto_form.html", {"form": form})

# ELIMINAR
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        producto.delete()
        return redirect("producto_list")

    return render(request, "requerimiento6/producto_confirm_delete.html", {"producto": producto})
