from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    """
    Modelo base abstracto que proporciona un campo de marca de tiempo para la fecha de creación.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Product(BaseModel):
    """
    Modelo que representa un producto con detalles como nombre, descripción, cantidad y fecha de vencimiento.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
   
    def __str__(self):
        """
        Retorna una representación en cadena del producto.
        """
        return self.name


class Alert(BaseModel):
    """
    Modelo que representa una alerta asociada a un producto, basada en su fecha de vencimiento.
    
    Atributos:
        product: Relación con el producto al que aplica la alerta.
        days_before_expiration: Días antes del vencimiento en que se debe activar la alerta.
        is_active: Indica si la alerta está activa.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="alerts")
    days_before_expiration = models.IntegerField()
    is_active = models.BooleanField(default=True)

    @property
    def status(self):
        """
        Calcula y retorna el estado actual de la alerta basado en la fecha de vencimiento del producto.
        
        Retorna:
            - "Expirado": Si el producto ya venció o vence hoy.
            - "Alerta: Menos de 5 días": Si quedan menos de 5 días para el vencimiento.
            - "Alerta: Menos de 10 días": Si quedan entre 5 y 10 días para el vencimiento.
            - "Vigente": Si quedan 10 o más días para el vencimiento.
        """
        today = now().date()
        days_left = (self.product.expiration_date - today).days

        if days_left <= 0:
            return "Expirado"
        elif days_left < 5:
            return "Alerta: Menos de 5 días"
        elif days_left < 10:
            return "Alerta: Menos de 10 días"
        else:
            return "Vigente"

    def __str__(self):
        """
        Retorna una representación en cadena de la alerta, incluyendo el ID, el nombre del producto y el estado de la alerta.
        """
        return f"{self.id} - Alerta para: {self.product.name} - {self.status}"
