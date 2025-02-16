from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """
    Clase de paginación personalizada que extiende la funcionalidad de PageNumberPagination de DRF.

    Configura la paginación permitiendo al cliente especificar el tamaño de la página mediante el parámetro 'page_size'.
    
    Atributos:
        page_size (int): Número predeterminado de elementos por página.
        page_size_query_param (str): Parámetro de consulta para modificar el tamaño de la página.
        max_page_size (int): Número máximo permitido de elementos por página.
    """
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100
