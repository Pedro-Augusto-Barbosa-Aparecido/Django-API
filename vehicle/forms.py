from django.forms import ModelForm
from vehicle.models import Vehicle


class VehicleFormCreateView(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
