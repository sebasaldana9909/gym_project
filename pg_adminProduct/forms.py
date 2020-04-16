from django import forms
from pg_adminProduct.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'priceSale', 'size', 'productImg']
        labels = {'name': 'Nombre', 'price': 'Precio', 'priceSale': 'Precio/Venta', 'size': 'Unidades', 'productImg': 'Imágen'}
        widgets = {'name': forms.TextInput(), 'price': forms.TextInput(), 'priceSale': forms.TextInput(), 'size': forms.TextInput()}


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
