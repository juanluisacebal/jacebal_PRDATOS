import os
import unittest

import numpy as np
import pandas as pd

from main import main
from src.e1_lectura_limpieza_datos import read_csv, clean_csv, rename_col
from src.e2_procesamiento_datos import breakdown_date, erase_month
from src.e3_agrupamiento_datos import print_biggest_handguns, print_biggest_longguns, groupby_state_and_year


class Test_main(unittest.TestCase):
    def test_main(self):
        """ Verifica que main se ejecuta sin dar excepciones """
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised an exception {e}")

    # pd.DataFrame({'month': ['2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03', '2020-03'], 'state': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana'], 'permit': [31205.0, 143.0, 5685.0, 2424.0, 27792.0, 5654.0, 4852.0, 227.0, 474.0, 16713.0, 16741.0, 0.0, 1842.0, 8647.0, 39780.0, 585.0, 9606.0, 898.0, 2394.0, 1620.0], 'permit_recheck': [606.0, 4.0, 958.0, 673.0, 0.0, 0.0, 335.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 3.0, 541682.0, 53551.0, 8668.0, 4.0, 182977.0, 220.0], 'handgun': [34897.0, 4657.0, 46377.0, 15304.0, 81543.0, 43322.0, 9196.0, 4936.0, 148.0, 117900.0, 44107.0, 170.0, 0.0, 11611.0, 44112.0, 45695.0, 378.0, 16715.0, 28268.0, 25038.0], 'long_gun': [17850.0, 3819.0, 19346.0, 8968.0, 48616.0, 22756.0, 3290.0, 2323.0, 5.0, 38365.0, 16807.0, 80.0, 0.0, 8193.0, 17127.0, 22724.0, 5778.0, 8964.0, 15315.0, 10278.0], 'other': [1583.0, 487.0, 2433.0, 600.0, 5041.0, 2086.0, 5421.0, 190.0, 0.0, 5017.0, 1245.0, 11.0, 0.0, 716.0, 0.0, 2613.0, 91.0, 889.0, 937.0, 1258.0], 'multiple': [1744, 386, 4846, 885, 0, 3242, 0, 196, 1, 6073, 2305, 9, 0, 714, 2408, 2311, 13, 952, 1615, 1342], 'admin': [0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 9.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 18.0, 0.0, 0.0, 2.0, 0.0], 'prepawn_handgun': [36.0, 0.0, 18.0, 27.0, 0.0, 0.0, 0.0, 3.0, 0.0, 26.0, 31.0, 0.0, 0.0, 6.0, 0.0, 12.0, 0.0, 8.0, 32.0, 16.0], 'prepawn_long_gun': [23.0, 0.0, 19.0, 25.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.0, 18.0, 0.0, 0.0, 6.0, 0.0, 9.0, 0.0, 8.0, 27.0, 21.0], 'prepawn_other': [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 2.0, 2.0], 'redemption_handgun': [3035.0, 210.0, 2011.0, 1301.0, 957.0, 0.0, 0.0, 16.0, 0.0, 4912.0, 2011.0, 1.0, 0.0, 507.0, 0.0, 817.0, 3.0, 832.0, 2145.0, 1319.0], 'redemption_long_gun': [1564.0, 177.0, 908.0, 1407.0, 539.0, 0.0, 0.0, 14.0, 0.0, 1602.0, 1292.0, 0.0, 0.0, 520.0, 0.0, 492.0, 61.0, 444.0, 1520.0, 845.0], 'redemption_other': [19.0, 0.0, 9.0, 5.0, 9.0, 0.0, 0.0, 0.0, 0.0, 13.0, 10.0, 0.0, 0.0, 0.0, 0.0, 16.0, 0.0, 7.0, 5.0, 12.0], 'returned_handgun': [13.0, 13.0, 110.0, 0.0, 0.0, 206.0, 0.0, 71.0, 1.0, 853.0, 3.0, 0.0, 1.0, 40.0, 0.0, 31.0, 43.0, 52.0, 9.0, 0.0], 'returned_long_gun': [0.0, 16.0, 12.0, 0.0, 0.0, 36.0, 0.0, 0.0, 0.0, 93.0, 0.0, 0.0, 0.0, 11.0, 0.0, 3.0, 9.0, 17.0, 5.0, 0.0], 'returned_other': [0.0, 0.0, 2.0, 0.0, 0.0, 3.0, 0.0, 2.0, 63.0, 5.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'rentals_handgun': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'rentals_long_gun': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'private_sale_handgun': [42.0, 14.0, 21.0, 11.0, 0.0, 0.0, 0.0, 97.0, 0.0, 316.0, 19.0, 0.0, 0.0, 6.0, 0.0, 60.0, 0.0, 17.0, 32.0, 18.0], 'private_sale_long_gun': [23.0, 13.0, 11.0, 10.0, 0.0, 0.0, 0.0, 43.0, 0.0, 184.0, 7.0, 0.0, 0.0, 5.0, 0.0, 35.0, 1.0, 5.0, 16.0, 17.0], 'private_sale_other': [8.0, 0.0, 5.0, 3.0, 0.0, 0.0, 0.0, 4.0, 0.0, 37.0, 1.0, 0.0, 0.0, 2.0, 0.0, 40.0, 1.0, 2.0, 1.0, 9.0], 'return_to_seller_handgun': [2.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 54.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 'return_to_seller_long_gun': [2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 60.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 1.0, 2.0, 0.0], 'return_to_seller_other': [0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 'totals': [92652, 9939, 82771, 31651, 164497, 77305, 23103, 8123, 692, 192234, 84601, 271, 1843, 30989, 645109, 129016, 24652, 29816, 235305, 42015]})


class TestLecturaLimpiezaDatos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        df = pd.DataFrame({
            'longgun': [123], 'month': [12]
        })
        df2 = pd.DataFrame({
            'long_gun': [123], 'month': [12]
        })
        df = rename_col(df)
        df2 = rename_col(df2)
        df_r = rename_col(self._df)
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
        df = pd.DataFrame({
            'month': ['01'], 'year': ['2020']
        })
        df = erase_month(df)
        self.assertNotIn('month', df.columns)


class TestAgrupamientoDatos(unittest.TestCase):
    def test_groupby_state_and_year(self):
        df = pd.DataFrame([
            {'year': '2012', 'state': 'Florida', 'permit': 30, 'handgun': 26750, 'long_gun': 110},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120},
        ])
        df = groupby_state_and_year(df)
        esperado = pd.DataFrame({
            'state': ['Florida', 'Texas'],
            'year': ['2012', '2013'],
            'permit': [30, 200],
            'handgun': [26750, 22800],
            'long_gun': [110, 20600]
        })
        print(df)
        texas = df[(df['state'] == 'Texas') & (df['year'] == '2013')]['handgun']
        texas_handgun = df[(df['state'] == 'Texas') & (df['year'] == '2013')]['handgun'].sum()
        print(texas)
        print(texas_handgun)
        pass
        # self.assertEqual(texas_handgun, 22800)
        # self.assertEquals(df, esperado)

    def test_print_biggest_handguns(self):
        df = pd.DataFrame([
            {'year': '2012', 'state': 'Florida', 'permit': 30, 'handgun': 26750, 'long_gun': 110},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120}
        ])
        self.assertEqual(print('El estado con más solicitudes de pistolas ha sido Florida, '
                               'el año 2012 con 26750 solicitudes.'),
                         print_biggest_handguns(df))

    def test_print_biggest_longguns(self):
        df = pd.DataFrame([
            {'year': '2012', 'state': 'Florida', 'permit': 30, 'handgun': 20, 'long_gun': 110},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 30, 'long_gun': 4120}
        ])
        self.assertEqual(print('El estado con más solicitudes de pistolas ha sido Texas, '
                               'el año 2013 con 4120 solicitudes.'),
                         print_biggest_longguns(df))


class TestAnalisisTemporalDatos(unittest.TestCase):
    def test_time_evolution(self):
        pass


class TestAnalisisDatosEstados(unittest.TestCase):
    def test_groupby_state(self):
        pass

    def test_clean_states(self):
        pass

    def test_merge_datasets(self):
        pass

    def test_calculate_relative_values(self):
        pass

    def test_arreglar_Kentucky(self):
        pass


class TestMapasCoropleticos(unittest.TestCase):
    def test_crear_capa_coropletica(self):
        pass

    def test_crear_y_guardar_mapa_html(self):
        pass

    def test_hacer_todo_mapas(self):
        pass


if __name__ == '__main__':
    unittest.main()
    #unittest.TestSuite()
