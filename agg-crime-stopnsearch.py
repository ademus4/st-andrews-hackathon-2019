import glob
import os
import pandas as pd


def main():
    '''
    Script to merge all stop and search files into single dataframe
    '''
    
    df_list = []
    file_paths = glob.iglob('./Astraea/**/*stop-and-search*', recursive=True)

    for file_path in file_paths:
        df = pd.read_csv(file_path)
        force = file_path.replace('-stop-and-search.csv', '')[26:]  # works?
        df['force'] = force
        df_list.append(df)
        print(file_path)

    df_all = pd.concat(df_list)
    df_all.to_csv('crime_stopnsearch_all.csv')
        

if __name__=="__main__":
    main()
