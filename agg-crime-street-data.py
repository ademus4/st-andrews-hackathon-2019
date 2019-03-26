import glob
import os
import pandas as pd


def main():
    '''
    Script to merge all street files into single dataframe
    '''
    
    df_list = []
    file_paths = glob.iglob('./Astraea/**/*street*', recursive=True)

    for file_path in file_paths:
        df = pd.read_csv(file_path)
        df_list.append(df)
        print(file_path)

    df_all = pd.concat(df_list)
    df_all.to_csv('crime_street_all.csv')
        

if __name__=="__main__":
    main()
