import src.enunciado1_jacebal as e1

def main():
    # URL del archivo CSV
    url = 'data/nics-firearm-background-checks.csv'
    df = e1.read_csv(url)
    df = e1.clean_csv(df)
    df = e1.rename_col(df)

if __name__ == '__main__':
    main()
