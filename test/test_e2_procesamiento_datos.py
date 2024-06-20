import unittest
import pandas as pd

from src.e2_procesamiento_datos import breakdown_date, erase_month


class TestProcesamientoDatos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
            Uso este metodo de clase para tener los dos df disponible para el resto de metodos
        """
        cls._df = pd.read_csv("../data/nics-firearm-background-checks.csv")
        cls._df2 = pd.read_csv("../data/us-state-populations.csv")

    def test_breakdown_date(self):
        """
            Verifica que separa bien year y month
        """
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
        """
            Verifica que elimina month del dataframe
        """
        df = pd.DataFrame({
            'month': ['01'], 'year': ['2020']
        })
        df = erase_month(df)
        self.assertNotIn('month', df.columns)


# En el caso de querer ejecutar solo este modulo:
if __name__ == '__main__':
    import unittest

    unittest.main()
