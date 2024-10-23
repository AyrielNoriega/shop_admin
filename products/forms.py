
from django import forms

from products.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=255, label="Nombre")
    description = forms.CharField(widget=forms.Textarea, max_length=200, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)


    def save(self):
        data = self.cleaned_data # nos devuelve un diccionario con los datos limpios que vienen del formulario cuando el usuaario hace submit en el navegador
        product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            available=data['available'],
            photo=data['photo']
        )
        return product
