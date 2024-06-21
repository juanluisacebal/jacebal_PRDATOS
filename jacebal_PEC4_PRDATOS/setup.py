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
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.6',
    package_dir={'jacebal_PRDATOS': 'jacebal_PRDATOS'},
    entry_points={
        'console_scripts': [
            'jacebal_PRDATOS = jacebal_PRDATOS.main:main',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
