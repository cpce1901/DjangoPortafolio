from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from django.urls import reverse
from .models import Place, Sensor


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuario",
        required=True, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingresa usuario",
                "class": "text-input",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Ingresa contraseña",
                "class": "text-input",
            }
        ),
    )

class SensorForm(forms.Form):

    place = forms.ModelChoiceField(
        queryset=Place.objects.all(),
        widget=forms.Select(
            attrs={
                "class" : "",
                "hx-get": "/sensors/place/",
                "hx-target": "#id_sensor"
            }
        ))

    sensor = forms.ModelChoiceField(queryset=Sensor.objects.none())

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        if "place" in self.data:
            place_id = int(self.data.get('place'))
            self.fields['sensor'].queryset = Sensor.objects.filter(place_id=place_id)


    