
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Alert


@receiver(post_save, sender=Product)
def create_product_alerts(sender, instance, created, **kwargs):
    """
    Señal que se ejecuta después de guardar una instancia de Product.
    
    Si la instancia es recién creada (created=True), se crean dos alertas asociadas:
      - Una alerta con 5 días antes de la expiración.
      - Una alerta con 10 días antes de la expiración.
    """
    if created:
        # Se crean las alertas correspondientes
        Alert.objects.create(product=instance, days_before_expiration=5)
        Alert.objects.create(product=instance, days_before_expiration=10)
        
        
