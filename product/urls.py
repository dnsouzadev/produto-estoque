from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_products, name='list_products'),
    path('create', views.create_product, name='create_product'),
    path('edit/<int:id>', views.update_product, name='update_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
    path('view/<int:id>', views.view_product, name='view_product')
]
