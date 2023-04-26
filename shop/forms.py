from django import forms
from .models import costumers
class CheckoutForm(forms.Form):
    class Meta:
        models = costumers
        fields = '__all__'