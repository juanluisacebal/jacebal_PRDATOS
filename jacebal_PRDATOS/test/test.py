import unittest

if __name__ == '__main__':
    """
                    Busca todas las pruebas que hay en carpeta test
                """
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='test', pattern='test*.py')
    # Hacer las pruebas
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)
