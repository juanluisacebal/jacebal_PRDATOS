import src.enunciado1_jacebal as e1jla
import src.enunciado2_jacebal as e2jla
import src.enunciado3_jacebal as e3jla


def main():
    # URL del archivo CSV
    url = 'data/nics-firearm-background-checks.csv'
    df = e1jla.read_csv(url)
    df = e1jla.clean_csv(df)
    df = e1jla.rename_col(df)
    print("parte 2\n")
    print(df.head(), "\n")
    df = e2jla.breakdown_date(df)
    df = e2jla.erase_month(df)
    print(df.head())

    df = e3jla.groupby_state_and_year(df)
    e3jla.print_biggest_handguns(df)
    e3jla.print_biggest_longguns(df)

if __name__ == '__main__':
    main()

