from datetime import date
from requerimiento5.models import Cliente, Pedido


def ejemplo_consulta_pedidos_cliente():
    """
    Consulta todos los pedidos realizados por un cliente específico
    en un rango de fechas determinado utilizando el ORM de Django.
    """

    # Obtener el cliente por nombre
    cliente = Cliente.objects.get(nombre="Álvaro")

    # Filtrar los pedidos por cliente y por rango de fechas
    pedidos = Pedido.objects.filter(
        cliente=cliente,
        fecha__range=(date(2024, 1, 1), date(2024, 2, 28))
    )

    # Imprimir resultados
    print("Pedidos realizados por el cliente:", cliente.nombre)
    print("Rango de fechas: 2024-01-01 a 2024-02-28\n")
    for p in pedidos:
        print(f"ID: {p.id} | Fecha: {p.fecha} | Total: {p.total}")

    return pedidos
