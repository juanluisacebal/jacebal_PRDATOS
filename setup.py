from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="jacebal_PRDATOS",
    version="0.0.1",
    author="Juan Luis Acebal Rico",
    author_email="data@juanluisacebal.com",
    description="Paquete de PEC4 de programacion para la ciencia de datos.",
    url="juanluisacebal.com",
    # package_dir={'': '.'},
    packages=find_packages(),
    # scripts=['jacebal_PRDATOS/src/main.py'],
    # package_data={
    #    'data': ['/*.csv'],
    # },
    # data_files=[
    #    ('data', ['jacebal_PRDATOS/data/nics-firearm-background-checks.csv', 'jacebal_PRDATOS/data/us-state-populations.csv'])
    # ],
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.6',
    package_dir={'jacebal_PRDATOS': 'jacebal_PRDATOS'},
    # packages=['jacebal_PRDATOS','jacebal_PRDATOS.data','jacebal_PRDATOS.src', 'jacebal_PRDATOS.test'],
    # packages=['mypkg'],
    #     package_dir={'mypkg': 'src/mypkg'},
    #    package_data={'mypkg': ['data/*.dat']},

    entry_points={
        'console_scripts': [
            'jacebal_PRDATOS = jacebal_PRDATOS.main:main',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
