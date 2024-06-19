import unittest
import pandas as pd

from src.e4_analisis_temporal_datos import time_evolution


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


# En el caso de querer ejecutar solo este modulo:
if __name__ == '__main__':
    import unittest

    unittest.main()
