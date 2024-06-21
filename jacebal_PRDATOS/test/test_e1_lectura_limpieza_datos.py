import os
import unittest

import pandas as pd

from jacebal_PRDATOS.src.e1_lectura_limpieza_datos import read_csv, clean_csv, rename_col


class TestLecturaLimpiezaDatos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
            Uso setUpClass para algunos casos de prueba
        """
        dir_padre = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_datos: str = os.path.join(dir_padre, 'data', 'nics-firearm-background-checks.csv')
        path_datos2: str = os.path.join(dir_padre, 'data', 'us-state-populations.csv')
        cls._df = read_csv(path_datos)
        cls._df2 = read_csv(path_datos2)

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
        """
            Verifica que limpia bien el csv y elimina las columnas que debe
        """
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
        """
            Verifica que cambia bien el nombre de la columna longgun cuando existe
        """
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


# En el caso de querer ejecutar solo este modulo:
if __name__ == '__main__':
    import unittest

    unittest.main()
