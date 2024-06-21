import unittest

import pandas as pd

from jacebal_PRDATOS.src import print_biggest_handguns, print_biggest_longguns, groupby_state_and_year


class TestAgrupamientoDatos(unittest.TestCase):
    def test_groupby_state_and_year(self):
        """
            Verifica que agrupa por state y year
        """
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
        """
            Verifica que el mensaje salido en la terminal es el esperado para pistolas
        """
        df = pd.DataFrame([
            {'year': '2012', 'state': 'Florida', 'permit': 30, 'handgun': 26750, 'long_gun': 110},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 4560, 'long_gun': 4120}
        ])
        self.assertEqual(print('El estado con más compras de pistolas ha sido Florida, '
                               'el año 2012 con 26750 compras.'),
                         print_biggest_handguns(df))

    def test_print_biggest_longguns(self):
        """
            Verifica que el mensaje salido en la terminal es el esperado para armas largas
        """
        df = pd.DataFrame([
            {'year': '2012', 'state': 'Florida', 'permit': 30, 'handgun': 20, 'long_gun': 110},
            {'year': '2013', 'state': 'Texas', 'permit': 40, 'handgun': 30, 'long_gun': 4120}
        ])
        self.assertEqual(print('El estado con más compras de armas largas ha sido Texas, '
                               'el año 2013 con 4120 compras.'),
                         print_biggest_longguns(df))


# En el caso de querer ejecutar solo este modulo:
if __name__ == '__main__':
    import unittest

    unittest.main()
