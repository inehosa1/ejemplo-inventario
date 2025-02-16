from celery import shared_task
from django.utils.timezone import now
from .models import Product
import logging

logger = logging.getLogger(__name__)


@shared_task
def check_product_alerts():
    """
    Tarea de Celery para revisar y notificar alertas sobre productos basadas en su fecha de vencimiento.

    La tarea recorre todos los productos y verifica:
      - Si faltan exactamente 10 o 5 días para que un producto caduque, se emite una alerta.
      - Si el producto ha caducado (days_left == 0), se notifica la caducidad.

    Nota:
      Actualmente, se utilizan declaraciones 'print' para notificar. En un entorno de producción,
      se recomienda utilizar un sistema de logging (por ejemplo, logger.info o logger.warning).
    """
    today = now().date()
    for product in Product.objects.all():
        days_left = (product.expiration_date - today).days
        if days_left in {10, 5}:
            print(f"🔔 Alerta: {product.name} está por caducar en {days_left} días")
        elif days_left == 0:
            print(f"🚨 {product.name} ha caducado")
