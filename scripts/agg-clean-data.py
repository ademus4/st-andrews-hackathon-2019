import glob
import os
import pandas as pd
from datetime import datetime


class AstraeaData:
    '''
    Class to load and clean the Astraea dataset
    '''

    def __init__(self, folder_path, file_string):
        self.df = []
        self.folder_path = folder_path
        self.file_string = file_string


    def load_data(self):
        self.df_list = []
        self.search_string = os.path.join(self.folder_path, '*'+self.file_string+'*')
        self.file_paths = glob.iglob(self.search_string, recursive=True)

        print('Loading files')
        for file_path in self.file_paths:
            df = pd.read_csv(file_path)
            self.df_list.append(df)
            print(file_path)

        self.df = pd.concat(self.df_list)

    def clean_data(self):
        columns = self.df.columns
              
        if "Date" in columns:
            print('Cleaning date')
            self.df['datetime'] = pd.to_datetime(self.df['Date'])
            self.df.drop('Date', axis=1, inplace=True)

        if "Month" in columns:
            print('Cleaning datetime')
            self.df['datetime'] = self.df.apply(lambda x: datetime.strptime(x['Month'], "%Y-%m"), axis=1)
            self.df.drop('Month', axis=1, inplace=True)

        if "Falls within" in columns:
            print('Cleaning forces')
            self.df['force'] = self.df.apply(lambda x: x["Falls within"].replace(' ', '-').lower()\
                                   .replace('-police', '').replace('-constabulary', ''), axis=1)
            self.df.drop('Falls within', axis=1, inplace=True)

        if "Reported by" in columns:
            print('Cleaning reported by')
            self.df.drop('Reported by', axis=1, inplace=True)

        if "Context" in columns:
            print('Cleaning context')
            self.df.drop('Context', axis=1, inplace=True)

    def write_data(self):
        output_string = "crime_" + self.file_string + '_test.csv'
        print('Writing data to {}'.format(output_string))
        self.df.to_csv(output_string)
        

if __name__=="__main__":
    values = [
        ('./Astraea/**/', 'outcomes'),
        ('./Astraea/**/', 'street'),
        ('./Astraea/**/', 'stop-and-search'),
    ]
    for fpath, name in values:
        a = AstraeaData(fpath, name)
        a.load_data()
        a.clean_data()
        a.write_data()

