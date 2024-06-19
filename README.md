# jacebal_PRDATOS

# Proyecto de Visualización de datos

Este proyecto extrae, procesa, agrupa, analiza y visualiza el uso de armas de fuego en los Estados Unidos utilizando
datos de uso de armas de fuego largas y pistolas, y tambien las peticiones de permisos (comprobaciones de antecedentes)
por estado. El objetivo es visualizar el uso de armas de fuego en EEUU en el contexto de la PEC4 de programacion en
ciencia de datos en la Universitat Oberta de Catalunya (UOC). Autor: Juan Luis Acebal Rico.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

### `main.py`

Archivo y funcion principal del proyecto que ejecuta todos los modulos:
- `main()`

### Directorio `src/`: Contiene todos los scripts Python para manejar, procesar y visualizar los datos.

- `e1_lectura_limpieza_datos.py`:
    - `leer_datos()`: Carga datos desde un archivo CSV.
    - `limpiar_datos()`: Limpia y prepara los datos para análisis.

- `e2_procesamiento_datos.py`:
    - `procesar_datos()`: .

- `e3_agrupamiento_datos.py`:
    - `agrupar_datos()`: Agrupa los datos por estado y año para analisis detallado.

- `e4_analisis_temporal_datos.py`:
    - `analizar_tendencias_temporales()`: Analiza tendencias de datos a lo largo del tiempo.

- `e5_analisis_datos_estados.py`:
    - `analizar_datos_estados()`: Realiza un análisis específico por estado, utilizando cálculos estadísticos.

- `e6_mapas_coropleticos.py`:
    - `crear_mapa_coropletico()`: Genera mapas coropléticos para visualizar los datos geográficamente.

- `__init__.py`:

- `test/`:
- `e1_test()`:


- `data/`: Directorio para almacenar los conjuntos de datos

## Instalacion de dependencias

Para instalar las dependencias necesarias, tienes el documento dentro del proyecto, lo tienes que usar tanto uses un
entorno virtual como si usas el que tengas instalado (no recomendado).
usa

```bash
pip3 install -r requirements.txt
```

Ejecucion del proyecto con virtualenv e instalacion manual.

```bash
pip3 install virtualenv
```

```Creacion entorno virtual en bash
virtualenv mi_virtualenv
```

```Activar el entorno virtual
source mi_virtualenv/bin/activate
```

```Instalacion de dependencias dentro del entorno virtual
pip3 install -r requirements.txt
```

``` Instalar paquete jacebal_PRDATOS
pip3 install -e .
```

Estando dentro de la carpeta del proyecto este ultimo comando, y el de las dependencais