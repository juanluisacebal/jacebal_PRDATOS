from test_e1_lectura_limpieza_datos import *
from test_e2_procesamiento_datos import *
from test_e3_agrupamiento_datos import *
from test_e4_analisis_temporal_datos import *
from test_e5_analisis_datos_estados import *
from test_e6_mapas_coropleticos import *
from test_main import *

if __name__ == '__main__':
    # Busca todas las pruebas que hay en carpeta test
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='test', pattern='test*.py')

    # Hacer las pruebas
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
