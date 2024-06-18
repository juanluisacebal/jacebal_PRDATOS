import src.enunciado1_jacebal as e1jla
import src.enunciado2_jacebal as e2jla
import src.enunciado3_jacebal as e3jla
import src.enunciado4_jacebal as e4jla


def main():
    # URL del archivo CSV
    url = 'data/nics-firearm-background-checks.csv'
    df = e1jla.read_csv(url)
    df.hist()
    df = e1jla.clean_csv(df)
    df = e1jla.rename_col(df)
    df.hist()
    #e4jla.time_evolution(df)
    print("parte 2\n")
    print(df.head(), "\n")
    df = e2jla.breakdown_date(df)
    df = e2jla.erase_month(df)
    print(df[df['year']==2020].head())
    df.hist()
    df = e3jla.groupby_state_and_year(df)
    print(df[df['year']==2020].head())
    e3jla.print_biggest_handguns(df)
    e3jla.print_biggest_longguns(df)
    e4jla.time_evolution(df)


if __name__ == '__main__':
    main()

