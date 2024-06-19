import os
from src.e1_lectura_limpieza_datos import read_csv, clean_csv, rename_col
from src.e2_procesamiento_datos import breakdown_date, erase_month
from src.e3_agrupamiento_datos import groupby_state_and_year, print_biggest_handguns, print_biggest_longguns
from src.e4_analisis_temporal_datos import time_evolution
from src.e5_analisis_datos_estados import groupby_state, clean_states, merge_datasets, calculate_relative_values, \
    arreglar_Kentucky
from src.e6_mapas_coropleticos import hacer_todo_mapas


def main():
    # URL del archivo CSV con ruta relativa
    # en el momento de la ejecucion
    # para poder usar como paquete python
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_datos = os.path.join(directorio_actual, 'data', 'nics-firearm-background-checks.csv')

    df = read_csv(archivo_datos)
    representation = "pd.DataFrame(" + str(df.head(20).to_dict(orient='list')) + ")"
    print(representation)

    df.hist()
    df = clean_csv(df)
    df = rename_col(df)
    df.hist()
    # e4jla.time_evolution(df)
    print("parte 2\n")
    print(df.head(), "\n")
    df = breakdown_date(df)
    df = erase_month(df)
    print(df[df['year'] == 2020].head())
    # df.hist()
    df = groupby_state_and_year(df)
    print(df[df['year'] == 2020].head())
    print_biggest_handguns(df)
    print_biggest_longguns(df)
    time_evolution(df)
    print(df[['long_gun']].sum(axis=0))
    # Comentario del grafico:
    # muestra la evolucion a largo plazo de ventas
    # y permisos de armas.Se ve como desde 1998 se
    # ha disparado la venta y permisos de armas, y
    # como las ventas hasta 2007 eran mayores que
    # los permisos de armas. En 2014 los permisos
    # superaron la venta conjunta de armas cortas
    # y armas largas, y por ultimo cuando llego el
    # covid, las ventas y permisos fueron los de
    # 15 añoa antes
    df.info()
    df = groupby_state(df)
    df.info()
    archivo_pop = os.path.join(directorio_actual, 'data', 'us-state-populations.csv')
    df2 = read_csv(archivo_pop)
    # df2.info()
    df = clean_states(df)
    df.info()
    df_m = merge_datasets(df, df2)
    print(df_m)
    df_m = calculate_relative_values(df_m)
    print(df_m.sort_values(by=['permit_perc'], ascending=False).head(), '\n\n')
    df_m = arreglar_Kentucky(df_m)
    hacer_todo_mapas(df_m)


if __name__ == '__main__':
    main()
