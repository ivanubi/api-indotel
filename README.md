# REST API Indotel
📞 REST API para obtener información de un teléfono móvil dominicano: Chequea el tipo de número (local o móvil), si es local te ofrece la ciudad. También retorna el Proveedor de Servicio que otorgó el número.

## Requisitos:
 - MySQL
 - Python3

## Ejemplo:
localhost:port/number/8092412222 retornará:

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

- Instalar las dependencias con `pip install -r requirements.txt`.
- Debe correr el archivo *step1_excel_to_mysql.py* (`python step1_excel_to_mysql.py`) la cual llenará la base de datos con la información que está en el archivo *excel_numbers.xlsx* descargada de INDOTEL. 
- El próximo paso es ejecutar el código *step2_scrap_locations.py* (`python step2_excel_to_mysql.py`) la cual va a hacer un scraping de las locaciones de cada número telefónico local, esto podrá relacionar los números con su localidad en la base de datos.
- Finalmente `python application.py` y probar que funciona entrando a la URL localhost:port/number/[numero telefonico] (sustituir puerto y número telefónico por el puerto que estás usando y el número que quieras).

## A tener en cuenta:

Esta aplicación sólo nos dirá quién fue la compañía que originalmente otorgó el número, si el número telefónico cambia de compañía entonces no habrá forma de saber su proveedor actual.
