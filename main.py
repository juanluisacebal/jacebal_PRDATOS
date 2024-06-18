import src.enunciado1_jacebal as e1jla
import src.enunciado2_jacebal as e2jla
import src.enunciado3_jacebal as e3jla
import src.enunciado4_jacebal as e4jla
import src.enunciado5_jacebal as e5jla


def main():
    # URL del archivo CSV
    url = 'data/nics-firearm-background-checks.csv'
    df = e1jla.read_csv(url)
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
    df2 = e1jla.read_csv('data/us-state-populations.csv')
    # df2.info()
    df = e5jla.clean_states(df)
    df.info()
    df_m=e5jla.merge_datasets(df,df2)
    print(df_m)
if __name__ == '__main__':
    main()
