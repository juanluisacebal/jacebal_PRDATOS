import pandas as pd


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupar por state y year, y suma valores de: permit, handgun y long_gun

    Args:
        df (DataFrame): DataFrame que contenga
        year, state, permit, handgun, y long_gun como columnas

    Returns:
        DataFrame: DataFrame agrupado por state y year y la suma de los valores.
    """
    # Cambio a int year para agrupar correctamente
    df['year'] = df['year'].astype(int)
    df_agrupado = df.groupby(['state', 'year']).agg({'permit': 'sum',
                                                     'handgun': 'sum',
                                                     'long_gun': 'sum'}).reset_index()
    return df_agrupado


def print_biggest_handguns(df: pd.DataFrame):
    """
    Encuentra el estado y año con mas numero de solicitudes de pistolas

    Args:
        df (DataFrame): Df con las columnas state, year, y handgun.
    """
    resultado = df[df['handgun'] == df['handgun'].max()]
    print(f"El estado con más solicitudes de pistolas ha sido "
          f"{resultado.iloc[0]['state']}, el año {resultado.iloc[0]['year']} "
          f"con {resultado.iloc[0]['handgun']} solicitudes.")

def print_biggest_longguns(df: pd.DataFrame):
    """
    Encuentra el estado y año con mas numero de solicitudes de armas largas

    Args:
        df (DataFrame): Df con las columnas state, year, y long_gun.
    """
    resultado = df[df['long_gun'] == df['long_gun'].max()]
    print(f"El estado con más solicitudes de pistolas ha sido "
          f"{resultado.iloc[0]['state']}, el año {resultado.iloc[0]['year']} "
          f"con {resultado.iloc[0]['long_gun']} solicitudes.")
