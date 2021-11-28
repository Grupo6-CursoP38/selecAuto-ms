from rest_framework import serializers
from selecAppAuto.models.solicitud import Solicitud

class solicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['tipo_de_vehiculo', 'lugarRecogida', 'fechaRecogida', 'lugarEntrega', 'fechaEntrega']