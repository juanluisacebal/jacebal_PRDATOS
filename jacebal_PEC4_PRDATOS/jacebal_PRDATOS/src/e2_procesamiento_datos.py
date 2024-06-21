import pandas as pd


def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Divide la información de la columna 'month' en dos nuevas columnas: 'year' y 'month'.

    Args:
        df (DataFrame): El DataFrame original que contiene la columna 'month'.

    Returns:
        DataFrame: El DataFrame con las columnas 'year' y 'month' actualizadas.
    """
    df['month'] = df['month'].astype(str)
    # Creo la columna 'year' extrayendo los primeros 4 caracteres de 'month'
    df['year'] = df['month'].str.slice(0, 4)
    #  columna 'month' actualizada con los caracteres restantes después del guión
    df['month'] = df['month'].str.split('-').str[1]
    return df


def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina la columna 'month' del DataFrame.

    Args:
        df (DataFrame): El DataFrame del cual se eliminará la columna 'month'.

    Returns:
        DataFrame: El DataFrame sin la columna 'month'.
    """
    df.drop('month', axis=1, inplace=True)
    return df
