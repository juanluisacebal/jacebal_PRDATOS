import pandas as pd


def read_csv(url: str) -> pd.DataFrame:
    """
    Lee un archivo CSV a la URL dada, muestra 5 filas del DF,
    y la estructura del DataFrame.

    Args:
        url (str): URL del archivo CSV que se desea leer.

    Returns:
        DataFrame: El DataFrame cargado desde el archivo CSV.
    """
    df = pd.read_csv(url)
    print(df.head())
    print(df.info())
    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el DataFrame, manteniendo solo las columnas específicas y muestra las columnas restantes.

    Args:
        df (DataFrame): El DataFrame original a limpiar.

    Returns:
        DataFrame: El DataFrame limpiado con solo las columnas requeridas.
    """
    columnas = ['month', 'state', 'permit', 'handgun', 'long_gun']
    df_limpio = df[columnas]
    print("Columnas conservadas:", df_limpio.columns)
    return df_limpio


def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cambio del nombre de la columna 'longgun' a 'long_gun' en el DataFrame, si existe.

    Args:
        df (DataFrame): El DataFrame que podría tener la columna a renombrar.

    Returns:
        DataFrame: El DataFrame con la columna renombrada.
    """
    print("Columnas antes del cambio:", df.columns)
    if 'longgun' in df.columns:
        df = df.rename(columns={'longgun': 'long_gun'})
    print("Columnas después del cambio:", df.columns)
    return df
