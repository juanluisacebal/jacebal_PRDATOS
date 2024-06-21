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

- `main()`: Llama a cada una de las funciones disponibles en el directorio src

### Directorio `src/`: Contiene todos los scripts Python para manejar, procesar y visualizar los datos.

- `e1_lectura_limpieza_datos.py`:
    - `read_csv()`: Carga datos desde un archivo CSV.
    - `clean_csv()`: Limpia y prepara los datos para análisis.
    - rename_col(): Cambia el nombre de la columna longgun(si existe) por long_gun.

- `e2_procesamiento_datos.py`:
    - `breakdown_date()`: Divide en 2 columnas la fecha, teniendo como resultado year y month.
    - `erase_month()`: Elimina el mes (month) de nuestro dataframe.

- `e3_agrupamiento_datos.py`:
    - `groupby_state_and_year()`: Agrupa los datos por estado y año.
    - `print_biggest_handguns()`: Imprime por consola el estado y el año con mas ventas de pistolas.
    - `print_biggest_longguns()`: Imprime por consola el estado y el año con mas ventas de armas largas.

- `e4_analisis_temporal_datos.py`:
    - `time_evolution()`: Analiza tendencias de datos de armas (largas y cortas) y permisos a lo largo del tiempo.

- `e5_analisis_datos_estados.py`:
    - `groupby_state()`: Realiza un agrupamiento de los datos temporales por estado.
    - `clean_states()`: Limpia (si existen) los estaddos asociados de los que el dataset de poblacion no tiene datos de
      poblacion.
    - `merge_datasets()`:Fusiona el dataset de armas con el dataset de poblacion.
    - `calculate_relative_values()`: Crea 3 nuevas metricas en el dataset de armas largas, cortas y permisos cada 100000
      habitantes.
    - `arreglar_Kentucky()`:Arregla los datos sobre permisos de armas de Kentucky, ya que es outlier y puede generar
      falsas conclusiones. Lo sustituye por la media del dataset.

- `e6_mapas_coropleticos.py`:
    - `crear_capa_coropletica()`: Genera capas coropléticas para visualizar los datos geográficamente y genera el mapa
      en forma de imagen PNG para cada capa.
    - `crear_y_guardar_mapa_html()`: Recibe una lista de capas y genera un mapa html.
    - `hacer_todo_mapas()`: Crea 3 capas llamando a crear_capa_coropletica y genera un mapa llamando a
      crear_y_guardar_mapa_html.

- `__init__.py`: Definicion como modulo de carpeta src (vacio).

### Directorio `data/`:

- Directorio para almacenar los conjuntos de datos para el analisis y visualizacion:
    - `nics-firearm-background-checks.csv`: Datos de venta de armas y permisos (antecedentes) de armas.
    - `us-state-populations.csv`: Datos de poblacion por estado de 2014.

### Directorio `test/`:

- Contiene pruebas unitarias para asegurar la calidad y correcto funcionamiento de las funciones y módulos del proyecto:
    - ### `test.py`: Pruebas para ejecucion de todas las pruebas del paquete.
    - `test_main.py`: Pruebas para la función principal del proyecto.
    - `test_e1_lectura_limpieza_datos.py`: Pruebas para funciones de lectura y limpieza de datos.
    - `test_e2_procesamiento_datos.py`: Pruebas para funciones de procesamiento de datos.
    - `test_e3_agrupamiento_datos.py`: Pruebas para funciones de agrupamiento de datos.
    - `test_e4_analisis_temporal_datos.py`: Pruebas para análisis temporal de los datos.
    - `test_e5_analisis_datos_estados.py`: Pruebas para el análisis de datos por estado.
    - `test_e6_mapas_coropleticos.py`: Pruebas para la creación de mapas coropléticos.
    - `test_procesamiento_datos_completo.py`: Pruebas para el procesamiento completo de los datos.
    - `__init__.py`: Definicion como modulo de carpeta test (vacio).

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

``` Instalar paquete jacebal_PRDATOS modo editable (enlace simbolico a la carpeta del proyecto)
pip3 install -e .
```

``` Instalar paquete jacebal_PRDATOS copiandolo
pip3 install .
```

Estando dentro de la carpeta del proyecto este ultimo comando, y el de las dependencias

``` Instalar paquete jacebal_PRDATOS con la distribucion de tipo sdist
pip3 install jacebal_prdatos-0.0.1.tar.gz
```

``` Instalar paquete jacebal_PRDATOS con la distribucion de tipo wheel (.whl) binaria
pip3 install jacebal_PRDATOS-0.0.1-py3-none-any.whl
```

## Uso

``` Ejecucion
jacebal_PRDATOS
```

## Test unitarios

Ejecucion de la ruta de instalacion dentro de virtualenv (cd mi_virtualenv/lib/python3.11/site-packages/jacebal_PRDATOS)

```bash en la ruta
python -m unittest 
```

Ejecucion de todos los tests

```bash
python -m unittest test
```

Ejecución de un test específico

``` bash
python -m unittest test.test_e1_lectura_limpieza_datos.TestLecturaLimpiezaDatos.test_read_csv
python -m unittest test.test_e1_lectura_limpieza_datos.TestLecturaLimpiezaDatos.test_clean_csv
python -m unittest test.test_e1_lectura_limpieza_datos.TestLecturaLimpiezaDatos.test_rename_col
....
``` 

Las rutas a los archivos de datos son relativas y se han implementado para obtenerlas de forma absoluta al directorio
activo de la terminal donde se ejecuta el paquete, por tanto, no existen problemas para ejecutarlo desde cualquier
directorio siempre y cuando Python este puesto en el PATH del sistema operativo, y las imagenes se van a guardar en el
directorio activo.

# Licencia

- Licencia Creative Commons 1.0: Derecho a usar comercialmenmte, a modificar, distribuir y a uso privado. No hay derecho
  a uso como marca, a patentar ni se ofrece ningun tipo de garantia ni responsabilidad. Para mas informacion mirar el
  archivo de LICENSE.
- Debido a que esta en fase de evaluacion de la asignatura, una vez evaluada, dispondre publico el repositorio para
  compartirlo bajo licencia CC 1.0