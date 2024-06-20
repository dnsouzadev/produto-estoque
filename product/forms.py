from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, HTML
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'available', 'photo']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name', css_class='form-control mb-3'),
            Field('description', css_class='form-control mb-3'),
            Field('price', css_class='form-control mb-3'),
            Field('quantity', css_class='form-control mb-3'),
            Field('available', css_class='form-select mb-3'),
            Field('photo', css_class='form-control mb-3'),
            Submit('submit', 'Salvar', css_class='btn btn-primary'),
            HTML('<a href="{% url "list_products" %}" class="btn btn-secondary">Voltar</a>')
        )
