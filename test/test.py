import os
import unittest

import folium
import pandas as pd
from main import main
from src.e1_lectura_limpieza_datos import read_csv, clean_csv, rename_col
from src.e2_procesamiento_datos import breakdown_date, erase_month
from src.e3_agrupamiento_datos import print_biggest_handguns, print_biggest_longguns, groupby_state_and_year
from src.e4_analisis_temporal_datos import time_evolution
from src.e5_analisis_datos_estados import arreglar_Kentucky, clean_states, calculate_relative_values, merge_datasets, \
    groupby_state
from src.e6_mapas_coropleticos import crear_capa_coropletica


class Test_Main(unittest.TestCase):
    def test_main(self):
        """ Verifica que main se ejecuta sin dar excepciones """
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised an exception {e}")


class TestLecturaLimpiezaDatos(unittest.TestCase):
    @classmethod
    def setUp(cls):
        """ Uso setUp para algunos casos de prueba """
        print("Loading dataset")
        cls._df = pd.read_csv("../data/nics-firearm-background-checks.csv")
        cls._df2 = pd.read_csv("../data/us-state-populations.csv")

    def test_read_csv(self):
        """
                Prueba que la funcion read_csv carga correctamente los dos archivos de datos en CSV
                que dispone el paquete jacebal_PRDATOS y que los DataFrame  no estan vacios.
        """
        directorio_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        archivo_datos: str = os.path.join(directorio_proyecto, 'data', 'nics-firearm-background-checks.csv')
        df = read_csv(archivo_datos)
        archivo_datos2: str = os.path.join(directorio_proyecto, 'data', 'us-state-populations.csv')
        df2 = read_csv(archivo_datos2)

        self.assertIsNotNone(df)
        self.assertFalse(df.empty)
        self.assertIsNotNone(df2)
        self.assertFalse(df2.empty)
        self.assertIsNotNone(self._df)
        self.assertIsNotNone(self._df2)
        self.assertFalse(self._df.empty)
        self.assertFalse(self._df2.empty)

    def test_clean_csv(self):
        """ Verifica que limpia bien el csv y elimina las columnas que debe """
        df = pd.DataFrame({
            'month': ['2010-01'], 'state': ['Texas'], 'permit': [0], 'handgun': [0],
            'long_gun': [0], 'other': [0]
        })
        df = clean_csv(df)
        columnas = ['month', 'state', 'permit', 'handgun', 'long_gun']
        df_c = clean_csv(self._df)
        for columna in columnas:
            self.assertIn(columna, df.columns)
            self.assertIn(columna, df_c.columns)
        self.assertNotIn(not columnas, df.columns)
        self.assertNotIn(not columnas, df_c.columns)

    def test_rename_col(self):
        """ Verifica que cambia bien el nombre de la columna longgun cuando existe """
        df = pd.DataFrame({
            'longgun': [123], 'month': [12]
        })
        df2 = pd.DataFrame({
            'long_gun': [123], 'month': [12]
        })
        df = rename_col(df)
        df2 = rename_col(df2)

        self.assertIn('long_gun', df.columns)
        self.assertNotIn('longgun', df.columns)

        self.assertIn('long_gun', self._df.columns)
        self.assertNotIn('longgun', self._df.columns)

        self.assertIn('long_gun', df2.columns)
        self.assertNotIn('longgun', df2.columns)


class TestProcesamientoDatos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Loading dataset")
        cls._df = pd.read_csv("../data/nics-firearm-background-checks.csv")
        cls._df2 = pd.read_csv("../data/us-state-populations.csv")

    def test_breakdown_date(self):
        """ Verifica que separa bien year y month """
        df = pd.DataFrame({
            'month': ['2020-01']
        })
        df = breakdown_date(df)
        df_b = breakdown_date(self._df)
        self.assertIn('year', df.columns)
        self.assertIn('month', df.columns)
        self.assertTrue((df['year'] == '2020').any())
        self.assertTrue((df['month'] == '01').any())

        self.assertIn('year', df_b.columns)
        self.assertIn('month', df_b.columns)
        self.assertTrue((df_b['year'] == '2014').any())
        self.assertTrue((df_b['month'] == '09').any())

    def test_erase_month(self):
        """ Verifica que elimina month del dataframe """
        df = pd.DataFrame({
            'month': ['01'], 'year': ['2020']
        })
        df = erase_month(df)
        self.assertNotIn('month', df.columns)


class TestAgrupamientoDatos(unittest.TestCase):
    def test_groupby_state_and_year(self):
        """ Verifica que agrupa por state y year """
        df = pd.DataFrame([
            {'year': '2012', 'state': 'Florida', 'permit': 30, 'handgun': 26750, 'long_gun': 110},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
        ])
        df_agrupado = groupby_state_and_year(df)
        esperado = pd.DataFrame({
            'state': ['Florida', 'Texas'],
            'year': ['2012', '2013'],
            'permit': [30, 200],
            'handgun': [26750, 22800],
            'long_gun': [110, 20600]
        })
        print(esperado)

        texas_2013 = df_agrupado[(df_agrupado['state'] == 'Texas') & (df_agrupado['year'] == 2013)]
        florida_2012 = df_agrupado[(df_agrupado['state'] == 'Florida') & (df_agrupado['year'] == 2012)]

        self.assertEqual(texas_2013['handgun'].iloc[0], 22800)
        self.assertEqual(texas_2013['long_gun'].iloc[0], 20600)
        self.assertEqual(texas_2013['permit'].iloc[0], 200)

        self.assertEqual(florida_2012['handgun'].iloc[0], 26750)
        self.assertEqual(florida_2012['long_gun'].iloc[0], 110)
        self.assertEqual(florida_2012['permit'].iloc[0], 30)

    def test_print_biggest_handguns(self):
        """ Verifica que el mensaje salido en la terminal es el esperado para pistolas"""
        df = pd.DataFrame([
            {'year': '2012', 'state': 'Florida', 'permit': 30, 'handgun': 26750, 'long_gun': 110},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120}
        ])
        self.assertEqual(print('El estado con más solicitudes de pistolas ha sido Florida, '
                               'el año 2012 con 26750 solicitudes.'),
                         print_biggest_handguns(df))

    def test_print_biggest_longguns(self):
        """ Verifica que el mensaje salido en la terminal es el esperado para armas largas"""
        df = pd.DataFrame([
            {'year': '2012', 'state': 'Florida', 'permit': 30, 'handgun': 20, 'long_gun': 110},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 30, 'long_gun': 4120}
        ])
        self.assertEqual(print('El estado con más solicitudes de pistolas ha sido Texas, '
                               'el año 2013 con 4120 solicitudes.'),
                         print_biggest_longguns(df))


class TestAnalisisTemporalDatos(unittest.TestCase):
    def test_time_evolution(self):
        """ Verifica que el df utilizado en el grafico es el esperado y ha sido agrupado correctamente teniendo en
            cuenta que time_evolution devuelve el df utilizado para hacer el grafico.
        """
        datos = {
            'year': [2020, 2020, 2021, 2021],
            'permit': [100, 150, 200, 250],
            'handgun': [60, 40, 80, 120],
            'long_gun': [70, 30, 50, 150]
        }
        df = pd.DataFrame(datos)
        df_procesado = time_evolution(df)
        esperado = pd.DataFrame({
            'year': [2020, 2021],
            'permit': [250, 450],
            'handgun': [100, 200],
            'long_gun': [100, 200]})
        pd.testing.assert_frame_equal(df_procesado, esperado)


class TestAnalisisDatosEstados(unittest.TestCase):
    def test_groupby_state(self):
        """ Verifica que agrupa correctamente por estado"""
        df = pd.DataFrame({
            'state': ['Texas', 'Texas', 'Florida', 'Florida'],
            'permit': [20, 30, 10, 15],
            'handgun': [100, 150, 50, 60],
            'long_gun': [200, 300, 80, 90]
        })
        df_resultado = groupby_state(df)
        df_esperado = pd.DataFrame({
            'state': ['Florida', 'Texas'],
            'permit': [25, 50],
            'handgun': [110, 250],
            'long_gun': [170, 500]
        })
        pd.testing.assert_frame_equal(df_resultado, df_esperado)

    def test_clean_states(self):
        """ Verifica que limpia bien los estados sin datos de poblacion eliminandolos.
            Estos son Guam, Mariana Islands, Puerto Rico y Virgin Islands
        """
        df = pd.DataFrame({
            'state': ['Texas', 'Florida', 'Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
        })
        df_resultado = clean_states(df)
        df_esperado = pd.DataFrame({
            'state': ['Texas', 'Florida']
        })
        pd.testing.assert_frame_equal(df_resultado, df_esperado)

    def test_merge_datasets(self):
        """ Verifica que fusiona correctamente los dataset"""
        df_armas = pd.DataFrame({
            'state': ['Texas', 'Florida'],
            'permit': [20, 10]
        })
        df_poblacion = pd.DataFrame({
            'state': ['Texas', 'Florida'],
            'pop_2014': [1000, 500]
        })
        df_resultado = merge_datasets(df_armas, df_poblacion)
        df_esperado = pd.DataFrame({
            'state': ['Texas', 'Florida'],
            'permit': [20, 10],
            'pop_2014': [1000, 500]
        })
        pd.testing.assert_frame_equal(df_resultado, df_esperado)

    def test_calculate_relative_values(self):
        """ Verifica que calcula correctamente la tasa por caada 1000000 habitantes."""
        df = pd.DataFrame({
            'state': ['Texas', 'Florida'],
            'permit': [200, 100],
            'handgun': [1000, 500],
            'long_gun': [800, 400],
            'pop_2014': [1000000, 500000]
        })
        df_resultado = calculate_relative_values(df)
        df_esperado = pd.DataFrame({
            'state': ['Texas', 'Florida'],
            'permit': [200, 100],
            'handgun': [1000, 500],
            'long_gun': [800, 400],
            'pop_2014': [1000000, 500000],
            'permit_perc': [20.0, 20.0],
            'handgun_perc': [100.0, 100.0],
            'long_gun_perc': [80.0, 80.0]
        })
        pd.testing.assert_frame_equal(df_resultado, df_esperado)

    def test_arreglar_Kentucky(self):
        """ Verifica que sustituye correctamente en Kentucky su permit_perc por la media del dataset"""
        df = pd.DataFrame({
            'state': ['Kentucky', 'Florida'],
            'permit_perc': [200.0, 100.0]
        })
        df_resultado = arreglar_Kentucky(df)
        df_esperado = pd.DataFrame({
            'state': ['Kentucky', 'Florida'],
            'permit_perc': [150.0, 100.0]
        })
        pd.testing.assert_frame_equal(df_resultado, df_esperado)

class TestMapasCoropleticos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame({
            'code': ['TX', 'CA'],
            'permit_perc': [1000, 1500],
            'handgun_perc': [2000, 3000],
            'long_gun_perc': [1500, 2500]
        })
        cls.geojson_url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"

    def test_crear_capa_coropletica(self):
        # Probar la creación de una capa coroplética
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


class TestProcesamientoDatosCompleto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Hace todas las transformaciones que hace main()"""
        # Cargo datos de los CSV
        cls.df = pd.read_csv("../data/nics-firearm-background-checks.csv")
        cls.df_pop = pd.read_csv("../data/us-state-populations.csv")

        # Hago todas las modificaciones del df en main.py
        cls.df = clean_csv(cls.df)
        cls.df = rename_col(cls.df)
        cls.df = breakdown_date(cls.df)
        cls.df = erase_month(cls.df)
        cls.df = groupby_state_and_year(cls.df)
        cls.df = groupby_state(cls.df)
        cls.df = clean_states(cls.df)

        # merge con df_pop tal y como esta en main.py
        cls.df_fusion = merge_datasets(cls.df, cls.df_pop)
        cls.df_fusion = calculate_relative_values(cls.df_fusion)
        cls.df_fusion = arreglar_Kentucky(cls.df_fusion)

    def test_dataframe_final(self):
        """ Verifica que algunos datos coinciden con lo esperado"""
        self.assertFalse(self.df_fusion.empty)
        self.assertIsNotNone(self.df_fusion)
        # Comparo unos registros
        # Usando esto en main, he obtenido la cabecera de df_m
        # lo dejo aqui para entender la logica de la prueba:
        # representation = "pd.DataFrame(" + str(df_m.head(10).to_dict(orient='list')) + ")"
        # print (representation)
        # y he copiado la cadena resultante para hacer las pruebas:
        df_m_head = pd.DataFrame({'state': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
                                            'Connecticut', 'Delaware', 'District of Columbia', 'Florida'],
                                  'permit': [1831707.0, 20022.0, 898033.0, 619978.0, 7711985.0, 654345.0, 1787517.0,
                                             34035.0,
                                             8887.0, 1634210.0],
                                  'handgun': [2577822.0, 518066.0, 2208229.0, 1151534.0, 7060424.0, 3106384.0,
                                              1036570.0, 262124.0,
                                              7408.0, 7520891.0],
                                  'long_gun': [2905635.0, 652905.0, 1727865.0, 1857047.0, 6738900.0, 3135015.0,
                                               700088.0, 289063.0,
                                               707.0, 4468507.0],
                                  'code': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL'],
                                  'pop_2014': [4849377, 736732, 6731484, 2966369, 38802500, 5355866, 3596677, 935614,
                                               658893,
                                               19893297],
                                  'permit_perc': [37772.00658971245, 2717.6775272419277, 13340.787855991337,
                                                  20900.23189967263,
                                                  19874.969396301785, 12217.351965116379, 49699.12505348687,
                                                  3637.7181187968545,
                                                  1348.7774190953614, 8214.877604250316],
                                  'handgun_perc': [53157.79738304529, 70319.46488003779, 32804.49006489505,
                                                   38819.647859049226,
                                                   18195.796662586174, 57999.6586919837, 28820.213769543385,
                                                   28016.254566519954,
                                                   1124.3100169526767, 37806.156515935996],
                                  'long_gun_perc': [59917.69664433184, 88621.77834002052, 25668.41130425327,
                                                    62603.37132703315,
                                                    17367.179949745507, 58534.23143894937, 19464.856032387674,
                                                    30895.540254848685,
                                                    107.30118547321037, 22462.375140732078]})

        pd.testing.assert_frame_equal(self.df_fusion.head(10), df_m_head)


if __name__ == '__main__':
    import unittest
    unittest.main()
