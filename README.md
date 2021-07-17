## HardGamers Monitor

Aplicación para mostrar el mejor precio de una lista de productos, junto con la tienda que lo vende. Además, notifica con un sonido cuando el precio de un producto baja.

### Requerimientos

- Python 3.8
- Una útilidad para descomprimir archivos ZIP, como 7zip o Winrar

### Uso

1. Descargar el último release.
2. Descomprimir el contenido del archivo
3. Instalar las librarias requeridas: `python3 -m pip install requirements.txt`
4. Ejecutar el binario usando python3, especificando los terminos de busqueda a trackear. Ejemplo: `PRODUCTS='rtx 2060,ssd 512gb,motherboard' python3 main.py`
