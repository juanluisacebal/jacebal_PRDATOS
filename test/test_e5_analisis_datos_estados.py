import unittest
import pandas as pd
from src.e5_analisis_datos_estados import arreglar_kentucky, clean_states, calculate_relative_values, merge_datasets, \
    groupby_state


class TestAnalisisDatosEstados(unittest.TestCase):
    def test_groupby_state(self):
        """
            Verifica que agrupa correctamente por estado
        """
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
        """
            Verifica que limpia bien los estados sin datos de poblacion eliminandolos.
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
        """
            Verifica que fusiona correctamente los dataset
        """
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
        """
            Verifica que calcula correctamente la tasa por caada 1000000 habitantes.
        """
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
        """
            Verifica que sustituye correctamente en Kentucky su permit_perc por la media del dataset
        """
        df = pd.DataFrame({
            'state': ['Kentucky', 'Florida'],
            'permit_perc': [200.0, 100.0]
        })
        df_resultado = arreglar_kentucky(df)
        df_esperado = pd.DataFrame({
            'state': ['Kentucky', 'Florida'],
            'permit_perc': [150.0, 100.0]
        })
        pd.testing.assert_frame_equal(df_resultado, df_esperado)


# En el caso de querer ejecutar solo este modulo:
if __name__ == '__main__':
    import unittest

    unittest.main()
