import src.enunciado1_jacebal as e1
import src.enunciado2_jacebal as e2


def main():
    # URL del archivo CSV
    url = 'data/nics-firearm-background-checks.csv'
    df = e1.read_csv(url)
    df = e1.clean_csv(df)
    df = e1.rename_col(df)
    print("parte 2\n")
    print(df.head(), "\n")
    df = e2.breakdown_date(df)
    df = e2.erase_month(df)
    print(df.head())


if __name__ == '__main__':
    main()
