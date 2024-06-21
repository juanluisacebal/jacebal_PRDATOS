import os
import unittest

import pandas as pd

from jacebal_PRDATOS.main import main
from jacebal_PRDATOS.src.e1_lectura_limpieza_datos import rename_col, clean_csv, read_csv
from jacebal_PRDATOS.src.e2_procesamiento_datos import erase_month, breakdown_date
from jacebal_PRDATOS.src.e3_agrupamiento_datos import groupby_state_and_year
from jacebal_PRDATOS.src.e5_analisis_datos_estados import (merge_datasets, calculate_relative_values,
                                                           arreglar_kentucky, clean_states, groupby_state)


class TestMain(unittest.TestCase):
    def test_main(self):
        """
            Verifica que main se ejecuta sin dar excepciones
        """
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised an exception {e}")
        os.remove('permit_perc.png')
        os.remove('long_gun_perc.png')
        os.remove('handgun_perc.png')
        os.remove('mapa.html')


class TestProcesamientoDatosCompleto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
            Hace todas las transformaciones que hace main()
            Sobre los datos, no incluye graficos (enunciado 4)
        """
        # Cargo datos de los CSV
        # Uso 2 veces dirname para ir de test a jacebal_PRDATOS (como hacer 2 veces cd.. )
        dir_test = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_datos: str = os.path.join(dir_test, 'data', 'nics-firearm-background-checks.csv')
        path_datos_pop: str = os.path.join(dir_test, 'data', 'us-state-populations.csv')
        cls.df = read_csv(path_datos)
        cls.df_pop = read_csv(path_datos_pop)

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
        cls.df_fusion = arreglar_kentucky(cls.df_fusion)

    def test_dataframe_final(self):
        """
            Verifica que algunos datos coinciden con lo esperado
        """
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


# En el caso de querer ejecutar solo este modulo:
if __name__ == '__main__':
    import unittest

    unittest.main()
