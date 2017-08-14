from django import forms

from cliente.models import Ticket

class TicketForm (forms.ModelForm):

    class Meta:
        model = Ticket

        fields = [
            'fecha_emision',
            'origen',
            'destino',
            'precio',
            'adquiriente',
            'puesto',
        ]
        labels = {
            'fecha_emision': 'Fecha de emision',
            'origen': 'Origen',
            'destino': 'Destino',
            'precio': 'Precio',
            'adquiriente': 'Adquiriente',
            'puesto': 'Puesto',
        }
        widgets = {
            'fecha_emision': forms.DateInput(),
            'origen': forms.Select(),
            'destino': forms.Select(),
            'precio': forms.NumberInput(),
            'adquiriente': forms.NumberInput(),
            'puesto': forms.NumberInput(),
        }



        