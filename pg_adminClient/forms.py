from django import forms
from pg_adminClient.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'telefono', 'monto']
        labels = {'name': 'Nombre', 'email': 'E-Mail', 'telefono': 'Telefono', 'monto': 'Monto Mensual'}
        widgets = {'name': forms.TextInput(), 'email': forms.TextInput(), 'telefono': forms.TextInput(), 'monto': forms.TextInput()}


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
