import io

import folium
from folium.plugins import Fullscreen

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
    # Añado el layer coroplético
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

    # pongo el layer en el mapa solo para generar el archivo png
    # teniendo este mapa solo una capa
    mapa = folium.Map(location=[40, -95],
                      zoom_control=False,
                      zoom_start=4)
    capa.add_to(mapa)
    img_data = mapa._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(columna + '.png')
    mapa.save(columna + '.html')
    return capa


def crear_y_guardar_mapa_html(df: pd.DataFrame,
                              ruta_geojson: str,
                              capas: list,
                              archivo_salida: str):
    """
    Crea un mapa de la libreria Folium,
    agrega todas las capas creadas y guarda el mapa.

    Args:
        df (DataFrame): Df con los datos.
        capas (list): Lista de capas de folium.Choropleth a agregar.
        archivo_salida (str): Nombre del archivo HTML del mapa.
    """
    # El contexto es EEUU entonces pongo coordenadas de EEUU
    max_lat = 83.6341
    min_lat = 7.1920
    max_lon = -52.2330
    min_lon = -167.6502
    mapa = folium.Map(location=[37.8, -96],
                      max_bounds=True,
                      min_lat=min_lat,
                      max_lat=max_lat,
                      min_lon=min_lon,
                      max_lon=max_lon,
                      zoom_start=4)

    # Agrega en cada pasada del bucle la capa
    for capa in capas:
        capa.add_to(mapa)
    #########################
    data_dict_permit = df.set_index('code')['permit_perc'].apply(lambda x: round(x, 2)).to_dict()
    data_dict_handgun = df.set_index('code')['handgun_perc'].apply(lambda x: round(x, 2)).to_dict()
    data_dict_longgun = df.set_index('code')['long_gun_perc'].apply(lambda x: round(x, 2)).to_dict()

    geojson_layer = folium.GeoJson(
        data=ruta_geojson,
        name="Estados y sus tasas cada 100.000 habitantes",
        style_function=lambda feature: {
            'color': 'black',
            'weight': 0.5,
            'fillOpacity': 0
        },
        tooltip=folium.GeoJsonTooltip(
            fields=['name'],
            aliases=["Estado: "],
            localize=True,
            labels=True
        )
    )

    # Añadir los datos del DataFrame a las propiedades del GeoJSON
    for feature in geojson_layer.data['features']:
        state = feature['id']
        feature['properties']['permit_perc'] = data_dict_permit.get(state, 'N/A')
        feature['properties']['handgun_perc'] = data_dict_handgun.get(state, 'N/A')
        feature['properties']['long_gun_perc'] = data_dict_longgun.get(state, 'N/A')

    # Actualizar el tooltip para mostrar los datos combinados
    geojson_layer.add_child(
        folium.features.GeoJsonTooltip(
            fields=['name', 'permit_perc', 'handgun_perc', 'long_gun_perc'],
            aliases=["Estado: ", "Permisos cada 100000 hab: ", "Pistolas cada 100000 hab: ",
                     "Armas largas cada 100000 hab: "],
            localize=True,
            sticky=False
        )
    )

    geojson_layer.add_to(mapa)
    #########################
    custom_zoom_js = '''
    function addZoomControl(map) {
        L.control.zoom({
            position: 'bottomleft'
        }).addTo(map);
    }
    addZoomControl(map);
    '''
    mapa.get_root().html.add_child(folium.Element(f'<script>{custom_zoom_js}</script>'))
    folium.LayerControl(position='bottomright').add_to(mapa)
    # guarda el mapa en html
    folium.plugins.Fullscreen(position='bottomright').add_to(mapa)
    mapa.save(archivo_salida)


def hacer_todo_mapas(df: pd.DataFrame):
    """
        Args:
            df (DataFrame): Df con los datos.
    """
    url_geo = (
        "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    )
    ruta_geojson = f"{url_geo}/us-states.json"
    capa1 = crear_capa_coropletica(df,
                                   'permit_perc',
                                   'code',
                                   ruta_geojson,
                                   'Permisos de Armas cada 100.000 habitantes',
                                   'OrRd',
                                   'Peticiones de antecedentes '
                                   'cada 100.000 habitantes')
    capa2 = crear_capa_coropletica(df,
                                   'handgun_perc',
                                   'code',
                                   ruta_geojson,
                                   'Venta de pistolas cada 100.000 habitantes',
                                   "BuGn",
                                   'Venta de pistolas cada 100.000 habitantes')
    capa3 = crear_capa_coropletica(df,
                                   'long_gun_perc',
                                   'code',
                                   ruta_geojson,
                                   'Venta de Armas largas cada 100.000 habitantes',
                                   "PuBu",
                                   'Venta de Armas largas cada 100.000 habitantes')
    capas = [capa1, capa2, capa3]

    crear_y_guardar_mapa_html(df, ruta_geojson, capas, 'mapa.html')
