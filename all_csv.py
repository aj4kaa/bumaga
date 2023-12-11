import json
import csv
import os
import pandas as pd
import pathlib

path = f'data_csv/'

directory = r'data_csv/'
file = r'*.csv'

df = pd.concat([pd.read_csv(path) for path in pathlib.Path(directory).rglob(file)], ignore_index=True)
df.drop_duplicates(keep='first', inplace=True)
df.to_csv(f"data_csv/all.csv", index=False)

