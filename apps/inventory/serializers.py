from rest_framework import serializers
from .models import Product, Alert


class AlertSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Alert.

    Este serializer incluye todos los campos del modelo y añade el campo calculado 'status'
    basado en la propiedad correspondiente del modelo Alert.
    """
    class Meta:
        model = Alert
        fields = '__all__'

    def to_representation(self, instance):
        """
        Extiende la representación del objeto serializado para incluir el campo 'status'.

        Args:
            instance (Alert): Instancia del modelo Alert.

        Returns:
            dict: Representación serializada de la instancia, incluyendo el campo 'status'.
        """
        representation = super().to_representation(instance)
        representation['status'] = instance.status
        return representation


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Product.

    Incluye todos los campos del modelo Product, además de incorporar de forma anidada
    las alertas asociadas utilizando AlertSerializer en modo de solo lectura.
    """
    alerts = AlertSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
