from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from .forms import ProductForm

# Create your views here.
def list_products(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'list_products.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')
        return render(request, 'create_product.html', {'form': form})
    form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products')
        return render(request, 'update_product.html', {'form': form})
    form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def delete_product(request, id):
    product = Product.objects.get(id=id)
    if product:
        product.delete()
        return JsonResponse({'message': 'Produto excluído com sucesso!'})
    return JsonResponse({'message': 'Produto não encontrado!'}, status=404)


def view_product(request, id):
    product = Product.objects.get(id=id)
    if product:
        return render(request, 'view_product.html', {'product': product})
    return render(request, 'view_product.html')
