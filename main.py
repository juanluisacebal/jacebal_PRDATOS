import os

import src.e1_lectura_limpieza_datos as e1jla
import src.e2_procesamiento_datos as e2jla
import src.e3_agrupamiento_datos as e3jla
import src.e4_analisis_temporal_datos as e4jla
import src.e5_analisis_datos_estados as e5jla
import src.e6_mapas_coropleticos as e6jla


def main():
    # URL del archivo CSV con ruta relativa
    # en el momento de la ejecucion
    # para poder usar como paquete python
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_datos = os.path.join(directorio_actual, 'data', 'nics-firearm-background-checks.csv')

    df = e1jla.read_csv(archivo_datos)
    df.hist()
    df = e1jla.clean_csv(df)
    df = e1jla.rename_col(df)
    df.hist()
    # e4jla.time_evolution(df)
    print("parte 2\n")
    print(df.head(), "\n")
    df = e2jla.breakdown_date(df)
    df = e2jla.erase_month(df)
    print(df[df['year'] == 2020].head())
    # df.hist()
    df = e3jla.groupby_state_and_year(df)
    print(df[df['year'] == 2020].head())
    e3jla.print_biggest_handguns(df)
    e3jla.print_biggest_longguns(df)
    e4jla.time_evolution(df)
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
    df = e5jla.groupby_state(df)
    df.info()
    archivo_pop = os.path.join(directorio_actual, 'data', 'us-state-populations.csv')
    df2 = e1jla.read_csv(archivo_pop)
    # df2.info()
    df = e5jla.clean_states(df)
    df.info()
    df_m = e5jla.merge_datasets(df, df2)
    print(df_m)
    df_m = e5jla.calculate_relative_values(df_m)
    print(df_m.sort_values(by=['permit_perc'], ascending=False).head(), '\n\n')
    # Enunciado 5.5
    print(df_m['permit_perc'].mean())
    print(df_m[df_m['state'] == 'Kentucky'])
    df_m.loc[df_m['state'] == 'Kentucky', 'permit_perc'] = round(df_m['permit_perc'].mean(), 2)
    print(df_m[df_m['state'] == 'Kentucky'])
    print(df_m['permit_perc'].mean())

    e6jla.hacer_todo_mapas(df_m)


if __name__ == '__main__':
    main()
