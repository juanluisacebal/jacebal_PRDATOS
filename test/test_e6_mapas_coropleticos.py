import os
import unittest
import folium
import pandas as pd
from src.e6_mapas_coropleticos import crear_capa_coropletica, hacer_todo_mapas, crear_y_guardar_mapa_html


class TestMapasCoropleticos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
            Uso este metodo de clase para tener un df y la url disponible para el resto de metodos
        """
        cls.df = pd.DataFrame({
            'code': ['Texas', 'Florida'],
            'permit_perc': [1000, 1500],
            'handgun_perc': [2000, 3000],
            'long_gun_perc': [1500, 2500]
        })
        cls.geojson_url = ("https://raw.githubusercontent.com/"
                           "python-visualization/folium/main/examples/data/us-states.json")

    def test_crear_capa_coropletica(self):
        """
            Verifica la existencia de una capa corocletica, objeto de tipo folium.Choropleth
        """
        capa = crear_capa_coropletica(
            df=self.df,
            columna='permit_perc',
            state_code='code',
            ruta_geojson=self.geojson_url,
            titulo='Test Map',
            color='OrRd',
            nombre='Test Layer'
        )
        self.assertIsInstance(capa, folium.Choropleth)

    def test_crear_y_guardar_mapa_html(self):
        """
            Verifica que se crea el mapa html (donde hay diferentes capas en el)
            Sin crear las imagenes PNG
        """
        capa1 = crear_capa_coropletica(self.df,
                                       'permit_perc',
                                       'code',
                                       self.geojson_url,
                                       'Test long_gun_perc',
                                       'OrRd',
                                       'Test permit_perc')
        capa2 = crear_capa_coropletica(self.df,
                                       'handgun_perc',
                                       'code',
                                       self.geojson_url,
                                       'Test handgun_perc',
                                       'BuGn',
                                       'Test handgun_perc')
        capa3 = crear_capa_coropletica(self.df,
                                       'long_gun_perc',
                                       'code',
                                       self.geojson_url,
                                       'Test long_gun_perc',
                                       'PuBu',
                                       'Test long_gun_perc')
        capas = [capa1, capa2, capa3]
        archivo_salida = 'mapa_test.html'
        crear_y_guardar_mapa_html(capas, archivo_salida)
        # Compruebo creacion del archivo
        self.assertTrue(os.path.exists(archivo_salida))
        # Borro el archivo
        os.remove(archivo_salida)

    def test_hacer_todo_mapas(self):
        """
            Verifica que se han creado los mapas, y luego los elimina
        """
        hacer_todo_mapas(self.df)
        # Sabiendo que hacer_todo_mapas guarda un archivo llamado 'mapa.html' y 3 imagenes png
        self.assertTrue(os.path.exists('mapa.html'))
        self.assertTrue(os.path.exists('long_gun_perc.png'))
        self.assertTrue(os.path.exists('permit_perc.png'))
        self.assertTrue(os.path.exists('handgun_perc.png'))

        # Limpieza después de la prueba
        os.remove('permit_perc.png')
        os.remove('long_gun_perc.png')
        os.remove('handgun_perc.png')
        os.remove('mapa.html')


if __name__ == '__main__':
    """ 
        n el caso de querer ejecutar solo este modulo.
    """
    import unittest
    unittest.main()
