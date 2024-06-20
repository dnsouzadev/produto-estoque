from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def list_products(request):
    return render(request, 'list_products.html')

def create_product(request):
    return render(request, 'create_product.html')

def update_product(request, id):
    return render(request, 'update_product.html')

def delete_product(request, id):
    return JsonResponse({'message': 'Produto excluído com sucesso!'})

def view_product(request, id):
    return render(request, 'view_product.html')
