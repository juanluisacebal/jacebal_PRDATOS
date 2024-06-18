import pandas as pd
from pandas import DataFrame


def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa y suma  valores por estado.

    Args:
        df (DataFrame): Df y columnas state, permit, handgun y long_gun

    Returns:
        DataFrame: Df con valores totales por estado.
    """
    grouped_df = df.groupby('state').agg({
        'permit': 'sum',
        'handgun': 'sum',
        'long_gun': 'sum'
    }).reset_index()
    return grouped_df


def clean_states(df: DataFrame) -> pd.DataFrame:
    """
    Elimina registros de territorios americanos de los que
    no tenemos datos de poblacion.
    Args:
        df (DataFrame): DataFrame que tiene estados y despues
        de comprobar si estan, hay que eliminarlos.

    Returns:
        DataFrame: DF sin los territorios.
    """
    territorios_a_eliminar = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    for territorio in territorios_a_eliminar:
        if df['state'].str.contains(territorio).any():
            df = df.drop(df[df['state'] == territorio].index)
    return df


def merge_datasets(df1: DataFrame, df2: DataFrame) -> DataFrame:
    """
    Fusiona los datos de armas con los datos de poblacion.

    Args:
        df1 (DataFrame): DataFrame con datos de armas por estado.
        df2 (DataFrame): DataFrame con poblacion por estado.

    Returns:
        DataFrame: DataFrame con la union.
    """
    df_m = pd.merge(df1, df2, on='state', how='left')
    return df_m