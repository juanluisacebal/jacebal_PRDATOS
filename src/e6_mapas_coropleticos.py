import io

import folium
import pandas as pd
from PIL import Image


def crear_capa_coropletica(df: pd.DataFrame,
                           columna: str,
                           state_code: str,
                           ruta_geojson: str, titulo: str,
                           color: str,
                           nombre: str) -> folium.Choropleth:
    """
    Crea un mapa coropletico basado en una columna del df.

    Args:
        df (DataFrame): Df con los datos.
        columna (str): Columna del df a visualizar.
        state_code (str) : columna del df con los codigos de estado,
        ruta_geojson (str): Ruta al archivo GeoJSON que describe los límites de los estados o regiones.
        titulo (str): Nombre del mapa.
        color (str): Color mapa
        nombre (str): Nombre del mapa para el selector de mapas.
    Returns:
        folium.Choropleth:  capa para agregar al mapa despues.
    """
    # Añadir el layer coroplético
    capa = folium.Choropleth(
        geo_data=ruta_geojson,
        name=nombre,
        data=df,
        columns=[state_code, columna],
        key_on='feature.id',
        fill_color=color,
        fill_opacity=0.7,
        line_opacity=.1,
        legend_name=titulo
    )
    mapa = folium.Map(location=[40, -95], zoom_start=4)
    capa.add_to(mapa)
    folium.LayerControl().add_to(mapa)
    img_data = mapa._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(columna + '.png')
    return capa


def crear_y_guardar_mapa_html(capas: list, archivo_salida: str):
    """
    Crea un mapa de la libreria Folium,
    agrega todas las capas creadas y guarda el mapa.

    Args:
        capas (list): Lista de capas de folium.Choropleth a agregar.
        archivo_salida (str): Nombre del archivo HTML del mapa.
    """
    # El contexto es EEUU entonces pongo coordenadas de EEUU
    mapa = folium.Map(location=[37.8, -96], zoom_start=4)

    # Agrega en cada pasada del bucle la capa
    for capa in capas:
        capa.add_to(mapa)
    folium.LayerControl().add_to(mapa)
    # guarda el mapa en html
    mapa.save(archivo_salida)


def hacer_todo_mapas(df: pd.DataFrame):
    url_geo = (
        "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    )
    ruta_geojson = f"{url_geo}/us-states.json"
    capa1 = crear_capa_coropletica(df,
                                   'permit_perc',
                                   'code',
                                   f"{url_geo}/us-states.json",
                                   'Permisos de Armas cada 100.000 habitantes',
                                   'OrRd',
                                   'Permisos cada 100000hab')
    capa2 = crear_capa_coropletica(df,
                                   'handgun_perc',
                                   'code',
                                   ruta_geojson,
                                   'Venta de pistolas cada 100.000 habitantes',
                                   "BuGn",
                                   'Ventas de pistolas cada 100000hab')
    capa3 = crear_capa_coropletica(df,
                                   'long_gun_perc',
                                   'code',
                                   ruta_geojson,
                                   'Venta de Armas largas cada 100.000 habitantes',
                                   "PuBu",
                                   'Ventas de armas largas cada 100000hab')
    capas = [capa1, capa2, capa3]

    crear_y_guardar_mapa_html(capas, 'mapa.html')
