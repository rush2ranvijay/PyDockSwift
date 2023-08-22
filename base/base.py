import os
import pandas as pd


class AcquireDataJob:
    def __init__(self, name):
        self.file_name = name

    def load_raw_data(self) -> pd.DataFrame:
        print(f"Current Working Directory: {os.getcwd()}")
        df = pd.read_csv(f"../resources/{self.file_name}.csv")
        print(f"Total Records in the file [ {self.file_name}.csv ] : {df.size}")
        return df
