from ..mpesa.models import MpesaPay
from django.forms import ModelForm

class MpesaForm(ModelForm):
    class Meta:
        model = MpesaPay  
        fields = '__all__'