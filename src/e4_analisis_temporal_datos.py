import matplotlib.pyplot as plt
import pandas as pd


def time_evolution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creacion de grafico mostrando la evolucion de las licencias,
    handguns y long guns en un periodo de tiempo.

    Args:
        df (DataFrame): DataFrame con columnas year, permit, handgun, y long_gun.
    Returns:
        DataFrame: DataFrame agrupado por year
    """
    df_agrupado = df.groupby('year').agg({
        'permit': 'sum',
        'handgun': 'sum',
        'long_gun': 'sum'
    }).reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(df_agrupado['year'], df_agrupado['permit'], label='Permits', marker='o')
    plt.plot(df_agrupado['year'], df_agrupado['handgun'], label='Handguns', marker='o')
    plt.plot(df_agrupado['year'], df_agrupado['long_gun'], label='Long Guns', marker='o')

    plt.title('Evolucion en el tiempo de permisos y armas de fuego')
    plt.xlabel('Year')
    plt.ylabel('Total')
    plt.legend()
    plt.grid(True)
    plt.show()

    return df_agrupado


if __name__ == '__main__':
    print("enunciado 4")
