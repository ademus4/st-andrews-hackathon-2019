import pandas as pd

def main():
    df_lon = pd.read_csv("./data/lsoa-london.csv", index_col=0)
    df_pop = pd.read_csv("./population-density.csv", index_col=0)
    df_lon.set_index('Codes', inplace=True)

    df_joined = df_pop.join(df_lon, how='left')
    df_joined['london'] = ~df_joined['Names'].isna()
    df_joined['london'].to_csv('./lsoa-london-index.csv')


if __name__=="__main__":
    main()
