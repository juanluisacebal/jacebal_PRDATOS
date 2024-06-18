from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="jacebal_PRDATOS",
    version="0.0.1",
    packages=find_packages(),
    #package_dir={"": "src"},
    scripts=['main.py'],
    package_data={
        '': ['data/*.csv'],
    },
    install_requires=required,
    entry_points={
        'console_scripts': [
            'jacebal_PRDATOS=main:main',
        ],
    },

    python_requires='>=3.6',
)
