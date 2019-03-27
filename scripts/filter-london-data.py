import pandas as pd

def main():
    df = pd.read_excel("./london-lsoa-data.xls", skiprows=0)
    df[['Codes', 'Names']].to_csv('./lsoa-london.csv')


if __name__=="__main__":
    main()
