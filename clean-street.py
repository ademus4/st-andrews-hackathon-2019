import pandas as pd
from datetime import datetime

def main():
    df = pd.read_csv('./crime_street_all.csv', index_col=0)

    df['datetime'] = df.apply(lambda x: datetime.strptime(x['Month'], "%Y-%m"), axis=1)
    df['force'] = df.apply(lambda x: x["Falls within"].replace(' ', '-').lower(), axis=1)

    df.drop(['Month', 'Falls within', 'Reported by', 'Context'], axis=1, inplace=True)
    df.to_csv('./crime_street_all_clean.csv')

if __name__=="__main__":
    main()
