# REST API Indotel
📞 REST API para obtener información de un teléfono móvil dominicano: Chequea el tipo de número (local o móvil), si es local te ofrece la ciudad. También retorna el Proveedor de Servicio que otorgó el número.

## Requisitos:
 - MySQL
 - Python3

## Ejemplo:
www.example.com/number/8092412222 retornará:

```
[
  {
    "localidad": "Santiago",
    "npa": 809,
    "nxx": 241,
    "prestadora": "CODETEL",
    "tipo": "LINEA FIJA"
  }
]
```

## Instalación:

Pendiente.
